import argparse
import shutil
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

FILE_TYPES = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "documents": [".pdf", ".docx", ".txt"],
    "scripts": [".py", ".js", ".sh"],
    "audio": [".mp3", ".wav"],
    "videos": [".mp4", ".mkv"]
}

def organize(source,dry_run=False):

    for file in source.iterdir():

        if file.is_file():

            suffix = file.suffix.lower()

            for folder, extensions in FILE_TYPES.items():

                if suffix in extensions:

                    target_dir = source / folder
                    target_dir.mkdir(exist_ok=True)

                    # shutil.move(str(file), target_dir / file.name)
                    if dry_run:
                        logger.info(f"[DRY RUN] Would move {file.name} → {folder}")
                    else:
                        shutil.move(str(file), target_dir / file.name)

                        logger.info(f"Moved {file.name} → {folder}")

                        break

def main():

    parser = argparse.ArgumentParser(description="File Organizer Tool")
    parser.add_argument("--source", required=True)
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()

    source = Path(args.source)

    organize(source)


if __name__ == "__main__":
    main()