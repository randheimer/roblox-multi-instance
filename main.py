import tkinter as tk
from tkinter import messagebox
import win32event
import win32api
import subprocess
import psutil
import os
import pystray
from PIL import Image, ImageDraw
import threading


class RobloxMultiInstance:
    def __init__(self):
        self.mutexes = []
        self.processes = []
        self.cookie_lock = None
        self.initialized = False
        
    def initialize(self):
        """Create mutexes before launching Roblox"""
        if self.initialized:
            return True
            
        try:
            # Create the singleton mutexes
            mutex1 = win32event.CreateMutex(None, True, "ROBLOX_singletonMutex")
            mutex2 = win32event.CreateMutex(None, True, "ROBLOX_singletonEvent")
            self.mutexes = [mutex1, mutex2]
            
            # Lock cookie file to prevent Error 773
            cookie_path = os.path.join(
                os.getenv('LOCALAPPDATA'),
                'Roblox', 'LocalStorage', 'RobloxCookies.dat'
            )
            try:
                if os.path.exists(cookie_path):
                    self.cookie_lock = open(cookie_path, 'r')
            except Exception as e:
                print(f"Cookie lock warning: {e}")
            
            self.initialized = True
            return True
        except Exception as e:
            print(f"Initialization error: {e}")
            return False
    
    def launch_instance(self):
        """Launch a new Roblox instance"""
        roblox_path = self.find_roblox_exe()
        
        if not roblox_path:
            return False
            
        try:
            process = subprocess.Popen([roblox_path])
            self.processes.append(process)
            return True
        except Exception as e:
            print(f"Launch error: {e}")
            return False
    
    def find_roblox_exe(self):
        """Locate RobloxPlayerBeta.exe"""
        base_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Roblox', 'Versions')
        
        if not os.path.exists(base_path):
            return None
            
        for folder in os.listdir(base_path):
            exe_path = os.path.join(base_path, folder, 'RobloxPlayerBeta.exe')
            if os.path.exists(exe_path):
                return exe_path
        return None
    
    def get_roblox_instances(self):
        """Get all running Roblox processes"""
        instances = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] == 'RobloxPlayerBeta.exe':
                    instances.append(proc)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return instances
    
    def kill_all_roblox(self):
        """Terminate all Roblox instances"""
        count = 0
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] == 'RobloxPlayerBeta.exe':
                    proc.kill()
                    count += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return count
    
    def cleanup(self):
        """Release mutexes and locks"""
        if self.cookie_lock:
            try:
                self.cookie_lock.close()
            except:
                pass
        
        for mutex in self.mutexes:
            try:
                win32api.CloseHandle(mutex)
            except:
                pass
        
        self.mutexes = []
        self.initialized = False


class RobloxMultiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roblox Multi-Instance Launcher")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        self.manager = RobloxMultiInstance()
        self.tray_icon = None
        self.is_hidden = False
        
        # Setup UI
        self.setup_ui()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_ui(self):
        """Create the GUI layout"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="Roblox Multi-Instance Launcher",
            font=("Arial", 14, "bold")
        )
        title_label.pack(pady=20)
        
        # Toggle button
        self.toggle_btn = tk.Button(
            self.root,
            text="Enable Multi-Instance",
            command=self.toggle_multi_instance,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            width=25,
            height=3
        )
        self.toggle_btn.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Multi-Instance: Disabled",
            font=("Arial", 11),
            fg="red"
        )
        self.status_label.pack(pady=20)
        
        # Minimize to tray button
        self.tray_btn = tk.Button(
            self.root,
            text="Minimize to Tray",
            command=self.minimize_to_tray,
            bg="#9E9E9E",
            fg="white",
            font=("Arial", 10),
            width=20
        )
        self.tray_btn.pack(pady=10)
    
    def toggle_multi_instance(self):
        """Toggle multi-instance mode on/off"""
        if self.manager.initialized:
            # Disable mode
            self.manager.cleanup()
            self.toggle_btn.config(
                text="Enable Multi-Instance",
                bg="#4CAF50"
            )
            self.status_label.config(
                text="Multi-Instance: Disabled",
                fg="red"
            )
        else:
            # Enable mode
            # Check if Roblox is installed
            if not self.manager.find_roblox_exe():
                messagebox.showerror(
                    "Error", 
                    "Roblox not found!\n\nPlease install Roblox first."
                )
                return
            
            if self.manager.initialize():
                self.toggle_btn.config(
                    text="Disable Multi-Instance",
                    bg="#f44336"
                )
                self.status_label.config(
                    text="Multi-Instance: Enabled",
                    fg="green"
                )
                messagebox.showinfo(
                    "Enabled", 
                    "Multi-instance mode is now active!\n\nYou can launch multiple Roblox instances."
                )
            else:
                messagebox.showerror("Error", "Failed to enable multi-instance mode")
    
    def create_tray_icon(self):
        """Create system tray icon"""
        # Create a simple icon image
        image = Image.new('RGB', (64, 64), color='blue')
        draw = ImageDraw.Draw(image)
        draw.rectangle([16, 16, 48, 48], fill='white')
        
        # Create menu
        menu = pystray.Menu(
            pystray.MenuItem("Show", self.show_window),
            pystray.MenuItem("Exit", self.quit_app)
        )
        
        # Create icon
        self.tray_icon = pystray.Icon("roblox_multi", image, "Roblox Multi-Instance", menu)
    
    def minimize_to_tray(self):
        """Minimize window to system tray"""
        if not self.tray_icon:
            self.create_tray_icon()
            # Run tray icon in separate thread
            threading.Thread(target=self.tray_icon.run, daemon=True).start()
        
        self.root.withdraw()
        self.is_hidden = True
    
    def show_window(self, icon=None, item=None):
        """Show window from tray"""
        self.root.deiconify()
        self.root.lift()
        self.is_hidden = False
    
    def quit_app(self, icon=None, item=None):
        """Quit application from tray"""
        if self.tray_icon:
            self.tray_icon.stop()
        if self.manager.initialized:
            self.manager.cleanup()
        self.root.quit()
    
    def on_closing(self):
        """Handle window close event"""
        if self.manager.initialized:
            self.manager.cleanup()
        if self.tray_icon:
            self.tray_icon.stop()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = RobloxMultiApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
