import os
import shutil
import sys
from rich import print

def color_text(text, color):
    return f"[{color}]{text}[/{color}]"

def prompt_day():
    try:
        d = int(input("What day is it? ").strip())
    except ValueError:
        print("Please enter a valid integer day.")
        sys.exit(1)
    if d < 0:
        print("Day must be non-negative.")
        sys.exit(1)
    return f"{d:02d}"

def confirm_remove(path):
    a = input(f"Destination '{path}' already exists. Remove it and continue? [y/N]: ").strip().lower()
    return a == "y"

def copy_and_replace(template_dir, target_dir, token="template", replacement:str="dayXX"):
    # Copy tree
    shutil.copytree(template_dir, target_dir)
    # Walk and rename directories/files, and replace contents where possible
    for root, dirs, files in os.walk(target_dir, topdown=True):
        # Rename dirs in-place so os.walk descends into new names
        for i, d in enumerate(list(dirs)):
            if token in d:
                old_path = os.path.join(root, d)
                new_name = d.replace(token, replacement)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                dirs[i] = new_name  # update so walk continues into renamed dir

        # Rename files
        for f in files:
            old_file = os.path.join(root, f)
            new_name = f
            if token in f:
                new_name = f.replace(token, replacement)
                new_file = os.path.join(root, new_name)
                os.rename(old_file, new_file)
                file_path = new_file
            else:
                file_path = old_file

            # Try to replace token inside text files
            try:
                with open(file_path, "r", encoding="utf-8") as fh:
                    data = fh.read()
            except (UnicodeDecodeError, PermissionError):
                # skip binary or unreadable files
                continue

            if token in data:
                new_data = data.replace(token, replacement)
                with open(file_path, "w", encoding="utf-8") as fh:
                    fh.write(new_data)

def main():
    day = prompt_day()
    token = "template"
    replacement = f"day{day}"
    cwd = os.getcwd()
    template_dir = os.path.join(cwd, token)
    if not os.path.isdir(template_dir):
        print(f"No '{token}' directory found in {cwd}.")
        sys.exit(1)
    target_dir = os.path.join(cwd, replacement)
    if os.path.exists(target_dir):
        if confirm_remove(target_dir):
            shutil.rmtree(target_dir)
        else:
            print("Aborted.")
            sys.exit(1)

    try:
        copy_and_replace(template_dir, target_dir, token=token, replacement=replacement)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

    print(f"Created {color_text(target_dir, 'yellow')} from {color_text(template_dir, 'magenta')} with '{token}' -> '{replacement}' replacements.")

if __name__ == "__main__":
    main()