# organizer/worker.py

import shutil
import hashlib
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def calculate_hash(file_path):

    """
    Generate MD5 hash for duplicate detection
    """

    hasher = hashlib.md5()

    with open(file_path, "rb") as f:

        while chunk := f.read(8192):
            hasher.update(chunk)

    return hasher.hexdigest()


def process_file(args):

    """
    Worker function used by multiprocessing
    """

    file_path, source_dir, file_types = args

    suffix = file_path.suffix.lower()

    for folder, extensions in file_types.items():

        if suffix in extensions:

            target_dir = source_dir / folder
            target_dir.mkdir(exist_ok=True)

            destination = target_dir / file_path.name

            try:

                shutil.move(str(file_path), destination)

                logger.info(f"Moved {file_path.name} → {folder}")

            except Exception as e:

                logger.error(f"Failed to move {file_path}: {e}")

            break