import sys
from colorama import Fore
from pathlib import Path

def list_files_and_directories(directory_path, indent=0):
    try:
        directory_path = Path(directory_path)
        if not directory_path.is_dir():
            raise FileNotFoundError
    except FileNotFoundError:
        print(Fore.RED + f"Error: {directory_path} is not a valid directory.")
        return

    for item in directory_path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + "  " * indent + f"{item.name}/")
            list_files_and_directories(item, indent + 1)
        else:
            print(Fore.GREEN + "  " * indent + item.name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    list_files_and_directories(directory_path)
