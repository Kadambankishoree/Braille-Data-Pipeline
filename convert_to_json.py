import os
import json

# Folder containing the .txt files
input_folder = 'C:\\Users\\ABC\\Music\\extracted_text'

# Output JSON file
output_file = 'C:\\Users\\ABC\\Music\\final_output.json'

# List to hold all page data
data = []

# Go through all .txt files in the folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        filepath = os.path.join(input_folder, filename)

        # Read text content
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_text = f.read()

        # 🧽 Clean the text
        cleaned_text = raw_text.strip().replace('\n', ' ')
        cleaned_text = ' '.join(cleaned_text.split())  # Removes extra spaces

        # 📦 Prepare JSON object
        page_data = {
            "filename": filename.replace('.txt', ''),
            "text": cleaned_text,
            "metadata": {
                "source": "scanned_book",
                "language": "English"
            }
        }

        data.append(page_data)

# 💾 Save all page data into one JSON file
with open(output_file, 'w', encoding='utf-8') as out_file:
    json.dump(data, out_file, indent=4, ensure_ascii=False)

print("✅ All text cleaned and saved to JSON!")
