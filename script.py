from pathlib import Path
import re, shutil

def reorganize_folders(source_dir):
    source_path = Path(source_dir).resolve()

    if not source_path.exists():
        print(f"Error: Source directory '{source_path}' does not exist.")
        return

    pattern = re.compile(r"^(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})$")

    for item in source_path.iterdir():
        if item.is_dir():
            match = pattern.match(item.name)

            if match:
                yy, mo, dd, hh, mi  = match.groups()
                year                = f"20{yy}"
                new_parent_dir      = source_path / year / mo
                new_folder_name     = f"{dd}-{hh}{mi}"
                destination_path    = new_parent_dir / new_folder_name

                print(f"Found: {item.name} -> Moving to {year}/{mo}/{new_folder_name}")
                new_parent_dir.mkdir(parents = True, exist_ok = True)

                if destination_path.exists():
                    print(f"[!] Destination already exists, skipping")
                    continue

                shutil.move(str(item), str(destination_path))

if __name__ == "__main__":
    TARGET_DIRECTORY = Path(__file__).resolve().parent
    print(f"[?] Reorganizing {TARGET_DIRECTORY}")
    reorganize_folders(TARGET_DIRECTORY)
    print("[✓] Reorganizing completed")