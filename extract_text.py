from PIL import Image
import pytesseract
import os

# Path to where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to your image folder
image_folder = r'C:\Users\ABC\Music\scanned_images'

# Folder where text files will be saved
output_folder = 'extracted_text'
os.makedirs(output_folder, exist_ok=True)

# Loop through each image in the folder
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.jpg', '.png')):
        image_path = os.path.join(image_folder, filename)
        img = Image.open(image_path)

        # Extract text from image
        text = pytesseract.image_to_string(img)

        # Save the text to a .txt file
        txt_filename = filename.rsplit('.', 1)[0] + '.txt'
        with open(os.path.join(output_folder, txt_filename), 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"✅ Text extracted from: {filename}")
