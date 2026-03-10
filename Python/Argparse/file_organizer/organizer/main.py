import argparse
import shutil
import logging
import yaml
import hashlib

from pathlib import Path
from multiprocessing import Pool
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def load_config(path):

    with open(path) as f:
        return yaml.safe_load(f)


def file_hash(path):

    h = hashlib.md5()

    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)

    return h.hexdigest()


def process_file(args):

    file, source, file_types = args

    suffix = file.suffix.lower()

    for folder, extensions in file_types.items():

        if suffix in extensions:

            target = source / folder
            target.mkdir(exist_ok=True)

            shutil.move(str(file), target / file.name)

            return


def main():

    parser = argparse.ArgumentParser(description="Production File Organizer")

    parser.add_argument("--source", required=True)
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--workers", type=int, default=4)

    args = parser.parse_args()

    source = Path(args.source)

    config = load_config(args.config)

    file_types = config["file_types"]

    files = [f for f in source.rglob("*") if f.is_file()]

    tasks = [(f, source, file_types) for f in files]

    with Pool(args.workers) as pool:

        list(tqdm(pool.imap(process_file, tasks), total=len(tasks)))


if __name__ == "__main__":
    main()