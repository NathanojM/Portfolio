import os

def replace_href_in_files(folder_path):
    # Walk through all files in the given folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                # Open each HTML file for reading
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                # Open the same file for writing
                with open(file_path, 'w', encoding='utf-8') as f:
                    for line in lines:
                        # Replace the href if found
                        updated_line = line.replace('href="Portfolio/', 'href="https://nathanojm.github.io/GIS/')
                        f.write(updated_line)
                print(f"Updated {file_path}")

# Specify the folder path containing your HTML files
folder_path = 'path_to_your_folder'  # Replace with your folder path

replace_href_in_files("/home/j/Documents/Jobs/Portfolio")
