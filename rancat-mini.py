import os
import random
import subprocess

folder_path = '/path/to/your/folder'

def pick_random_txt_file(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    if files:
        return random.choice(files)

def run_cat_on_file(file_path):
    subprocess.run(['cat', file_path], check=True, text=True, capture_output=True)

def main():
    selected_file = pick_random_txt_file(folder_path)
    if selected_file:
        file_path = os.path.join(folder_path, selected_file)
        run_cat_on_file(file_path)

if __name__ == "__main__":
    main()
