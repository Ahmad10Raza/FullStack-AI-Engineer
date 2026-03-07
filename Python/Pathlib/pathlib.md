## Python `pathlib` (Modern File Path Handling)

`pathlib` is the  **modern and recommended way to work with file paths in Python** .
It was introduced in **Python 3.4** to replace the older `os.path` module.

It provides an  **object-oriented interface for file system paths** .

Example difference:

Old way (`os.path`):

```python
import os

path = os.path.join("folder", "file.txt")
```

Modern way (`pathlib`):

```python
from pathlib import Path

path = Path("folder") / "file.txt"
```

`pathlib` makes file operations  **cleaner and easier to read** .

### 1. Importing `pathlib`

```python
from pathlib import Path
```

`Path` is the main class used to represent file system paths.

### 2. Creating a Path Object

Example:

```python
from pathlib import Path

p = Path("data.txt")

print(p)
```

Output:

```
data.txt
```

A `Path` object represents a  **file or directory path** .

### Example

```python
p = Path("/home/user/file.txt")
```

This creates a path object.

### Path Object Structure

```
Path
   |
   |-- file path
   |-- directory path
```

### 3. Joining Paths

`pathlib` uses `/` operator to join paths.

Example:

```python
from pathlib import Path

folder = Path("data")

file = folder / "input.txt"

print(file)
```

Output:

```
data/input.txt
```

This is equivalent to:

```
os.path.join("data","input.txt")
```

### 4. Checking File or Directory

Example:

```python
p = Path("data.txt")

print(p.exists())
```

Returns:

```
True / False
```

Check file:

```python
p.is_file()
```

Check directory:

```python
p.is_dir()
```

### Example

```python
from pathlib import Path

p = Path("example.txt")

if p.exists():
    print("File exists")
```

### 5. Getting File Information

Example:

```python
p = Path("report.pdf")

print(p.name)
```

Output:

```
report.pdf
```

Other attributes:

| Attribute    | Meaning                |
| ------------ | ---------------------- |
| `p.name`   | file name              |
| `p.stem`   | name without extension |
| `p.suffix` | file extension         |
| `p.parent` | parent directory       |

Example:

```python
p = Path("data/report.pdf")

print(p.name)
print(p.stem)
print(p.suffix)
print(p.parent)
```

Output:

```
report.pdf
report
.pdf
data
```

### 6. Getting Absolute Path

Example:

```python
p = Path("file.txt")

print(p.resolve())
```

Output example:

```
/home/user/file.txt
```

### 7. Creating Directories

Example:

```python
from pathlib import Path

p = Path("new_folder")

p.mkdir()
```

Create nested folders:

```python
p.mkdir(parents=True, exist_ok=True)
```

Parameters:

```
parents=True → create parent directories
exist_ok=True → avoid error if exists
```

### 8. Creating Files

Example:

```python
p = Path("test.txt")

p.touch()
```

This creates an empty file.

### 9. Reading Files

Example:

```python
p = Path("data.txt")

content = p.read_text()

print(content)
```

Equivalent old code:

```python
with open("data.txt") as f:
    content = f.read()
```

### 10. Writing Files

Example:

```python
p = Path("output.txt")

p.write_text("Hello world")
```

Append example:

```python
with p.open("a") as f:
    f.write("More text")
```

### 11. Listing Directory Files

Example:

```python
from pathlib import Path

folder = Path("data")

for file in folder.iterdir():
    print(file)
```

Output:

```
data/file1.txt
data/file2.txt
```

### 12. Searching Files (Glob)

`glob()` finds files matching patterns.

Example:

```python
folder = Path("data")

for file in folder.glob("*.txt"):
    print(file)
```

Find recursively:

```python
folder.rglob("*.txt")
```

This searches  **all subfolders** .

### Example

```
data/
   file1.txt
   file2.txt
   images/
        img1.txt
```

`rglob("*.txt")` returns all `.txt` files.

### 13. Deleting Files

Example:

```python
p = Path("temp.txt")

p.unlink()
```

Delete directory:

```python
p.rmdir()
```

### 14. Renaming Files

Example:

```python
p = Path("old.txt")

p.rename("new.txt")
```

### 15. File Size

Example:

```python
p = Path("data.txt")

print(p.stat().st_size)
```

Returns file size in  **bytes** .

### 16. Iterating Through Directories

Example:

```python
folder = Path("data")

for path in folder.rglob("*"):
    print(path)
```

This lists  **all files and folders recursively** .

### 17. Path Parts

Example:

```python
p = Path("/home/user/file.txt")

print(p.parts)
```

Output:

```
('/', 'home', 'user', 'file.txt')
```

### Path Object Example

```
Path("data/report.pdf")
     |
     |-- name → report.pdf
     |-- stem → report
     |-- suffix → .pdf
     |-- parent → data
```

### Why `pathlib` is Better than `os.path`

| Feature      | `os.path`        | `pathlib`     |
| ------------ | ------------------ | --------------- |
| Style        | Functional         | Object-oriented |
| Path joining | `os.path.join()` | `/`operator   |
| Readability  | Lower              | Higher          |
| Modern usage | Legacy             | Recommended     |

Example:

```
Path("data") / "file.txt"
```

is cleaner than:

```
os.path.join("data","file.txt")
```

### Real Use Cases

`pathlib` is used in:

```
data pipelines
file processing scripts
machine learning dataset loaders
ETL systems
automation scripts
```

Example ML dataset loader:

```python
dataset = Path("dataset")

for img in dataset.rglob("*.jpg"):
    process_image(img)
```

### Key `pathlib` Methods

```
exists()
is_file()
is_dir()
mkdir()
touch()
read_text()
write_text()
iterdir()
glob()
rglob()
rename()
unlink()
stat()
```

---

We will cover:

1. Advanced Path Manipulation
2. Advanced File Traversal
3. Filtering Files Efficiently
4. Combining `pathlib` with Generators
5. Using `pathlib` with Multiprocessing
6. Real Project: Dataset Organizer

## 1. Advanced Path Manipulation

`pathlib` allows easy manipulation of paths without string operations.

Example path:

```python
from pathlib import Path

p = Path("/home/user/project/data/file.txt")
```

Extract parts:

```python
print(p.name)
print(p.stem)
print(p.suffix)
print(p.parent)
```

Output

```
file.txt
file
.txt
/home/user/project/data
```

Get parent directories:

```python
print(p.parent)
print(p.parent.parent)
```

Output

```
/home/user/project/data
/home/user/project
```

### Changing File Extension

Example:

```python
p = Path("report.csv")

new_path = p.with_suffix(".json")

print(new_path)
```

Output

```
report.json
```

### Changing File Name

```python
p = Path("report.csv")

new_path = p.with_name("summary.csv")

print(new_path)
```

Output

```
summary.csv
```

## 2. Advanced File Traversal

Instead of manually walking directories, `pathlib` provides powerful traversal methods.

Example directory:

```
data/
   images/
        img1.jpg
        img2.jpg
   text/
        file1.txt
        file2.txt
```

### List all files

```python
from pathlib import Path

folder = Path("data")

for p in folder.rglob("*"):
    print(p)
```

Output

```
data/images/img1.jpg
data/images/img2.jpg
data/text/file1.txt
data/text/file2.txt
```

### List only files

```python
for p in folder.rglob("*"):
    if p.is_file():
        print(p)
```

### List only directories

```python
for p in folder.rglob("*"):
    if p.is_dir():
        print(p)
```

## 3. Filtering Files Efficiently

Example: find only `.jpg` images.

```python
images = Path("dataset")

for img in images.rglob("*.jpg"):
    print(img)
```

Example: find only `.csv` files.

```python
for file in Path("data").glob("*.csv"):
    print(file)
```

Difference:

```
glob()  → current folder
rglob() → recursive search
```

## 4. Combining `pathlib` with Generators

Generators allow  **memory-efficient file processing** .

Example large log processor.

```python
from pathlib import Path

def read_logs(folder):

    for file in Path(folder).rglob("*.log"):
        with file.open() as f:
            for line in f:
                yield line
```

Usage:

```python
for line in read_logs("logs"):
    print(line)
```

Benefits:

```
low memory usage
process files lazily
```

Used in:

```
data pipelines
log processing
stream processing
```

## 5. Using `pathlib` with Multiprocessing

Suppose we want to process thousands of files.

Example:

```
dataset/
   image1.jpg
   image2.jpg
   image3.jpg
```

Parallel processing:

```python
from pathlib import Path
from multiprocessing import Pool

def process_file(path):
    print("Processing", path)

files = list(Path("dataset").rglob("*.jpg"))

with Pool(4) as p:
    p.map(process_file, files)
```

This uses  **multiple CPU cores** .

Common use cases:

```
image processing
dataset preparation
video frame extraction
```

## 6. Real Project: Dataset Organizer

Suppose we have messy dataset:

```
dataset/
   a.jpg
   b.png
   c.jpg
   d.txt
```

Goal:

```
dataset/
   images/
   text/
```

### Implementation

```python
from pathlib import Path

dataset = Path("dataset")

images = dataset / "images"
text = dataset / "text"

images.mkdir(exist_ok=True)
text.mkdir(exist_ok=True)

for file in dataset.iterdir():

    if file.suffix in [".jpg", ".png"]:
        file.rename(images / file.name)

    elif file.suffix == ".txt":
        file.rename(text / file.name)
```

Result:

```
dataset/
   images/
       a.jpg
       b.png
       c.jpg
   text/
       d.txt
```

## 7. Large Dataset Processing Example

Example: counting lines across all `.txt` files.

```python
from pathlib import Path

total = 0

for file in Path("data").rglob("*.txt"):

    with file.open() as f:
        total += sum(1 for _ in f)

print(total)
```

This is used in:

```
data engineering
log analytics
ETL pipelines
```

## 8. Path Comparison

Example:

```python
p1 = Path("data/file.txt")
p2 = Path("data/file.txt")

print(p1 == p2)
```

Output

```
True
```

Resolve symbolic paths:

```python
p.resolve()
```

## 9. Checking Permissions

Example:

```python
p = Path("data.txt")

print(p.exists())
print(p.is_file())
print(p.is_dir())
```

## 10. Best Practices with `pathlib`

Use `pathlib` instead of `os.path`.

Example:

Bad:

```python
os.path.join("data","file.txt")
```

Better:

```python
Path("data") / "file.txt"
```

Use `Path` everywhere in  **modern Python projects** .

## Real Systems Using `pathlib`

`pathlib` is used heavily in:

```
data engineering scripts
machine learning dataset loaders
automation pipelines
ETL frameworks
file processing systems
```

Example ML dataset loader:

```python
dataset = Path("dataset")

for image in dataset.rglob("*.jpg"):
    load_image(image)
```

## Key Mental Model

```
Path object
     |
     |-- represent file/directory
     |-- manipulate path safely
     |-- perform filesystem operations
```

---

## Python `shutil` Module (File & Directory Operations)

`shutil` stands for  **Shell Utilities** .
It is used for **high-level file operations** like:

```text
copy files
move files
delete directories
archive files
manage datasets
```

While `pathlib` works with  **paths** , `shutil` works with  **file operations** .

In real systems, `pathlib` + `shutil` are often used  **together** .

Example imports:

```python
from pathlib import Path
import shutil
```

### 1. Copying Files

Basic file copy:

```python
import shutil

shutil.copy("source.txt", "destination.txt")
```

This copies the file  **content and permissions** .

Example with `pathlib`:

```python
from pathlib import Path
import shutil

src = Path("data/source.txt")
dst = Path("backup/source.txt")

shutil.copy(src, dst)
```

### 2. Copy File with Metadata

If we want to copy **file metadata** (timestamps etc.):

```python
shutil.copy2("source.txt", "destination.txt")
```

Difference:

| Function    | Behavior                |
| ----------- | ----------------------- |
| `copy()`  | copy content            |
| `copy2()` | copy content + metadata |

### 3. Copying Directories

To copy an entire folder:

```python
shutil.copytree("data", "backup_data")
```

Example directory:

```text
data/
   a.txt
   b.txt
   images/
       img1.jpg
```

After copy:

```text
backup_data/
   a.txt
   b.txt
   images/
       img1.jpg
```

Important option:

```python
shutil.copytree("data", "backup_data", dirs_exist_ok=True)
```

This avoids error if directory already exists.

### 4. Moving Files

Move file or directory:

```python
shutil.move("file.txt", "archive/file.txt")
```

Example:

```python
from pathlib import Path
import shutil

file = Path("data/report.txt")

shutil.move(file, "archive/report.txt")
```

Used heavily in  **automation scripts** .

### 5. Deleting Directories

To remove a directory and all its contents:

```python
shutil.rmtree("temp_folder")
```

Example:

```python
shutil.rmtree("old_logs")
```

This deletes:

```text
folder
all files
all subfolders
```

⚠ Be careful —  **this cannot be undone** .

### 6. Copy File Object

`copyfile()` copies file content only.

```python
shutil.copyfile("a.txt", "b.txt")
```

Difference:

| Function       | Behavior                |
| -------------- | ----------------------- |
| `copyfile()` | copy only data          |
| `copy()`     | copy data + permissions |
| `copy2()`    | copy data + metadata    |

### 7. Disk Usage

Check disk space:

```python
import shutil

usage = shutil.disk_usage("/")

print(usage)
```

Output:

```text
(total, used, free)
```

Example:

```python
total, used, free = shutil.disk_usage("/")

print("Total:", total)
print("Used:", used)
print("Free:", free)
```

### 8. Creating Archives

`shutil` can create compressed archives.

Example: zip archive.

```python
shutil.make_archive("backup", "zip", "data")
```

This creates:

```text
backup.zip
```

Archive formats supported:

```text
zip
tar
gztar
bztar
xztar
```

Example:

```python
shutil.make_archive("dataset_backup", "gztar", "dataset")
```

### 9. Extracting Archives

Example:

```python
shutil.unpack_archive("backup.zip", "restore_folder")
```

Result:

```text
restore_folder/
   extracted files
```

### 10. Ignore Certain Files During Copy

Example: skip `.log` files.

```python
shutil.copytree(
    "data",
    "backup",
    ignore=shutil.ignore_patterns("*.log")
)
```

This is useful in  **dataset backup pipelines** .

### Example directory:

```text
data/
   file1.txt
   file2.log
```

Result:

```text
backup/
   file1.txt
```

### 11. Combining `pathlib` + `shutil`

Example: backup all `.txt` files.

```python
from pathlib import Path
import shutil

source = Path("data")
backup = Path("backup")

backup.mkdir(exist_ok=True)

for file in source.rglob("*.txt"):
    shutil.copy(file, backup / file.name)
```

### 12. Real Project: File Organizer

Suppose we want to organize downloads.

Example messy folder:

```text
downloads/
   image1.jpg
   file.pdf
   script.py
   image2.png
```

Goal:

```text
downloads/
   images/
   documents/
   scripts/
```

### Implementation

```python
from pathlib import Path
import shutil

downloads = Path("downloads")

images = downloads / "images"
docs = downloads / "documents"
scripts = downloads / "scripts"

images.mkdir(exist_ok=True)
docs.mkdir(exist_ok=True)
scripts.mkdir(exist_ok=True)

for file in downloads.iterdir():

    if file.suffix in [".jpg", ".png"]:
        shutil.move(file, images / file.name)

    elif file.suffix == ".pdf":
        shutil.move(file, docs / file.name)

    elif file.suffix == ".py":
        shutil.move(file, scripts / file.name)
```

Result:

```text
downloads/
   images/
       image1.jpg
       image2.png
   documents/
       file.pdf
   scripts/
       script.py
```

### 13. Dataset Backup Example

Used in ML pipelines.

```python
from pathlib import Path
import shutil

dataset = Path("dataset")

backup = Path("dataset_backup")

shutil.copytree(dataset, backup, dirs_exist_ok=True)
```

### Key `shutil` Functions

| Function             | Purpose                 |
| -------------------- | ----------------------- |
| `copy()`           | copy file               |
| `copy2()`          | copy file with metadata |
| `copytree()`       | copy directory          |
| `move()`           | move file               |
| `rmtree()`         | delete directory        |
| `make_archive()`   | create archive          |
| `unpack_archive()` | extract archive         |
| `disk_usage()`     | disk info               |

### Mental Model

```text
pathlib → handle paths
shutil → perform file operations
```

Example pipeline:

```text
Find files (pathlib)
      ↓
Copy / move files (shutil)
      ↓
Process data
```

### Real Systems Using `shutil`

`shutil` is used in:

```text
dataset management
backup systems
automation scripts
file processing pipelines
ETL workflows
```
