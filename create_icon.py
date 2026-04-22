from PIL import Image, ImageDraw

# Create a simple icon for the application
def create_icon():
    # Create 256x256 image
    img = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a blue circle background
    draw.ellipse([20, 20, 236, 236], fill='#2196F3', outline='#1976D2', width=8)
    
    # Draw white "R" letter
    draw.text((80, 60), "R", fill='white', font=None)
    
    # Draw multiple squares to represent multiple instances
    square_size = 40
    spacing = 10
    
    # Top squares
    draw.rectangle([60, 120, 60+square_size, 120+square_size], fill='white', outline='#1976D2', width=3)
    draw.rectangle([60+square_size+spacing, 120, 60+2*square_size+spacing, 120+square_size], fill='white', outline='#1976D2', width=3)
    
    # Bottom squares
    draw.rectangle([60, 120+square_size+spacing, 60+square_size, 120+2*square_size+spacing], fill='white', outline='#1976D2', width=3)
    draw.rectangle([60+square_size+spacing, 120+square_size+spacing, 60+2*square_size+spacing, 120+2*square_size+spacing], fill='white', outline='#1976D2', width=3)
    
    # Save as ICO
    img.save('icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    print("Icon created: icon.ico")

if __name__ == "__main__":
    create_icon()
