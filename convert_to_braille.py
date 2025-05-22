import json
import subprocess

# Paths to Liblouis executable and table
louis_exe = r'C:\Users\ABC\Downloads\liblouis-3.33.0-win32\bin\lou_translate.exe'
table = r'C:\Users\ABC\Downloads\liblouis-3.33.0-win32\share\liblouis\tables\en-us-g2.ctb'


# Load JSON file with OCR extracted text
with open(r'C:\Users\ABC\Music\final_output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

braille_data = []

for entry in data:
    original_text = entry['text']  # use 'text' key, not 'original_text'
    
    # Run Liblouis for Braille conversion
    result = subprocess.run(
        [louis_exe, '-f', table],
        input=original_text.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    braille_text = result.stdout.decode('utf-8').strip()

    # Print debug info (to check if conversion works)
    print("Original text snippet:", original_text[:60])
    print("Braille text snippet:", braille_text[:60])
    print("-" * 40)
    
    new_entry = {
        "filename": entry['filename'],
        "original_text": original_text,
        "braille_text": braille_text,
        "metadata": entry['metadata']
    }
    braille_data.append(new_entry)

# Save new JSON file with braille text
with open(r'C:\Users\ABC\Music\braille_output.json', 'w', encoding='utf-8') as f:
    json.dump(braille_data, f, indent=4, ensure_ascii=False)

print("✅ Braille conversion done, output saved to braille_output.json")
