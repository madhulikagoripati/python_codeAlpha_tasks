import argparse
import shutil
from pathlib import Path


FILE_GROUPS = {
	"Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
	"Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf"},
	"Spreadsheets": {".xls", ".xlsx", ".csv"},
	"Videos": {".mp4", ".mkv", ".mov", ".avi"},
	"Audio": {".mp3", ".wav", ".aac", ".flac"},
	"Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
	"Python": {".py"},
}


def get_destination_folder(file_path):
	suffix = file_path.suffix.lower()
	for folder_name, extensions in FILE_GROUPS.items():
		if suffix in extensions:
			return folder_name
	return "Other"


def get_unique_path(destination):
	if not destination.exists():
		return destination

	counter = 1
	while True:
		numbered_name = f"{destination.stem}_{counter}{destination.suffix}"
		numbered_path = destination.with_name(numbered_name)
		if not numbered_path.exists():
			return numbered_path
		counter += 1


def organize_folder(folder, dry_run=False):
	folder = folder.resolve()
	script_path = Path(__file__).resolve()
	moved_count = 0

	for file_path in folder.iterdir():
		if not file_path.is_file() or file_path.resolve() == script_path:
			continue

		destination_folder = folder / get_destination_folder(file_path)
		destination = get_unique_path(destination_folder / file_path.name)
		print(f"{file_path.name} -> {destination_folder.name}/{destination.name}")

		if not dry_run:
			destination_folder.mkdir(exist_ok=True)
			shutil.move(str(file_path), str(destination))
		moved_count += 1

	action = "would be moved" if dry_run else "moved"
	print(f"{moved_count} file(s) {action}.")


def main():
	parser = argparse.ArgumentParser(
		description="Organize files in a folder by their file type."
	)
	parser.add_argument(
		"folder",
		nargs="?",
		default=".",
		help="Folder to organize (default: current folder)",
	)
	parser.add_argument(
		"--dry-run",
		action="store_true",
		help="Show planned moves without changing files",
	)
	args = parser.parse_args()

	folder = Path(args.folder)
	if not folder.is_dir():
		parser.error(f"Folder not found: {folder}")

	organize_folder(folder, args.dry_run)


if __name__ == "__main__":
	main()
