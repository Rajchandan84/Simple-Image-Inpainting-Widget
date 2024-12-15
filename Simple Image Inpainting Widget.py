#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
from PIL import Image, ImageDraw
from IPython.display import display  # For showing images in Jupyter Notebook

# Main function
def main():
    # Step 1: Use a predefined image path (simulate sandbox environment)
    image_path = Path("image.png").resolve()  # Replace 'image.png' with your actual image file name
    print("Resolved Image Path:", image_path)

    try:
        # Open the predefined image
        original_image = Image.open(image_path).convert("RGB")
        print("Uploaded Image:")
        display(original_image)  # Display the original image in the notebook

        # Initialize mask
        def initialize_mask(image):
            return Image.new("L", image.size, 0)

        mask_image = initialize_mask(original_image)
        print("Mask initialized successfully!")

        # Step 2: Get user input for coordinates
        print("Enter coordinates as x1,y1,x2,y2 separated by spaces. Example: 10,10,100,100 150,150,200,200")
        coords = input("Coordinates: ")

        if coords:
            try:
                parsed_coords = []
                for pair in coords.split(" "):
                    parsed_coords.append(tuple(map(int, pair.split(","))))

                # Draw on the mask
                def draw_mask(mask, coords):
                    draw = ImageDraw.Draw(mask)
                    draw.line(coords, fill=255, width=10)

                draw_mask(mask_image, parsed_coords)
                print("Mask Image:")
                display(mask_image)  # Display the mask image in the notebook
            except ValueError:
                print("Invalid input format. Please enter coordinates as x1,y1,x2,y2 separated by spaces.")

        # Step 3: Export the images
        save_original = input("Save original image? (y/n): ").lower() == 'y'
        save_mask = input("Save mask image? (y/n): ").lower() == 'y'

        if save_original or save_mask:
            if save_original:
                original_image.save("original_image.png")
                print("Original image saved as 'original_image.png'")
            if save_mask:
                mask_image.save("mask_image.png")
                print("Mask image saved as 'mask_image.png'")
    except FileNotFoundError:
        print("Sample image not found in the sandbox environment. Ensure 'image.png' is available.")

# Entry point for the script
if __name__ == "__main__":
    main()


# In[ ]:




