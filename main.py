from PIL import Image, ImageFont, ImageDraw
import os
import pandas as pd

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/Swansea-Q3pd.ttf', 40)  # Use Swansea-Q3pd font and set a smaller font size
FONT_COLOR = "#000000"  # Black text color

template = Image.open(r'template.png')  # Ensure template.png exists
WIDTH, HEIGHT = template.size

# Function to read names from a .txt file
def read_names_from_txt(file_path):
    with open(file_path, 'r') as file:
        names = file.readlines()
    return [name.strip() for name in names]  # Remove leading/trailing whitespaces

# Function to read names from a .csv file
def read_names_from_csv(file_path):
    df = pd.read_csv(file_path)
    # Assuming the column with names is called 'Name', adjust if needed
    return df['Name'].tolist()

# Function to create and save certificates
def make_certificates(name):
    '''Function to save certificates as a .png file'''
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text using textbbox (recommended over textsize)
    name_bbox = draw.textbbox((0, 0), name, font=FONT_FILE)
    name_width, name_height = name_bbox[2] - name_bbox[0], name_bbox[3] - name_bbox[1]

    # Placing it at the new coordinates (107, 457)
    draw.text((107, 457), name, fill=FONT_COLOR, font=FONT_FILE)

    # Save the certificate in the 'out' directory
    if not os.path.exists("./out"):
        os.makedirs("./out")  # Create the output directory if it doesn't exist

    image_source.save(f"./out/{name}.png")
    print('Saving Certificate of:', name)

if __name__ == "__main__":

    # Path to the input file (either .txt or .csv)
    input_file_path = "names.txt"  # Change this to your file name (e.g., "names.csv")

    # Read names from the file based on its extension
    if input_file_path.endswith('.txt'):
        names = read_names_from_txt(input_file_path)
    elif input_file_path.endswith('.csv'):
        names = read_names_from_csv(input_file_path)
    else:
        print("Unsupported file format. Please provide a .txt or .csv file.")
        exit()

    # Generate certificates for each name
    for name in names:
        make_certificates(name)

    print(len(names), "certificates done.")
