## Python `argparse` Module (Build CLI Tools)

`argparse` is used to build **command-line interfaces (CLI)** for Python programs.

Instead of hardcoding values in the script, users can  **pass parameters when running the program** .

Example command:

```bash
python train.py --epochs 10 --batch-size 32
```

This is widely used in:

```text
machine learning training scripts
data engineering pipelines
DevOps tools
automation scripts
system utilities
```

Many tools like **pip, git, docker CLI wrappers, ML training scripts** use this pattern.

### 1. Basic Example

Without `argparse`:

```python
name = input("Enter name: ")
print("Hello", name)
```

With `argparse`:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name")

args = parser.parse_args()

print("Hello", args.name)
```

Run:

```bash
python script.py --name Ahmad
```

Output:

```
Hello Ahmad
```

### How It Works

```text
User CLI input
     ↓
argparse parser
     ↓
Arguments object
     ↓
Program logic
```

### 2. Positional Arguments

Positional arguments are  **required arguments** .

Example:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

print("Hello", args.name)
```

Run:

```bash
python script.py Ahmad
```

Output:

```
Hello Ahmad
```

Here `name` is required.

### 3. Optional Arguments

Optional arguments start with `--`.

Example:

```python
parser.add_argument("--age")
```

Run:

```bash
python script.py --age 22
```

Output:

```
22
```

### 4. Default Values

Example:

```python
parser.add_argument("--epochs", default=5)
```

Run:

```bash
python train.py
```

Output:

```
epochs = 5
```

If user specifies:

```bash
python train.py --epochs 20
```

Output:

```
epochs = 20
```

### 5. Type Conversion

Arguments are strings by default.

We can specify types.

Example:

```python
parser.add_argument("--epochs", type=int)
```

Example:

```python
parser.add_argument("--learning-rate", type=float)
```

### Example Script

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--epochs", type=int)
parser.add_argument("--lr", type=float)

args = parser.parse_args()

print(args.epochs)
print(args.lr)
```

Run:

```bash
python train.py --epochs 10 --lr 0.001
```

Output:

```
10
0.001
```

### 6. Boolean Flags

Sometimes arguments act as  **switches** .

Example:

```python
parser.add_argument("--verbose", action="store_true")
```

Run:

```bash
python script.py --verbose
```

Output:

```
True
```

Without flag:

```
False
```

Used for:

```text
debug mode
verbose output
dry-run mode
```

### 7. Help Messages

`argparse` automatically generates help.

Example:

```python
parser = argparse.ArgumentParser(description="Training script")

parser.add_argument("--epochs", type=int, help="Number of training epochs")
```

Run:

```bash
python train.py --help
```

Output:

```
usage: train.py [-h] [--epochs EPOCHS]

Training script

optional arguments:
  -h, --help            show help message
  --epochs EPOCHS       Number of training epochs
```

### 8. Required Arguments

Example:

```python
parser.add_argument("--dataset", required=True)
```

Run without dataset:

```bash
python train.py
```

Output:

```
error: the following arguments are required: --dataset
```

### 9. Choices (Restrict Input)

Example:

```python
parser.add_argument("--model", choices=["cnn", "resnet", "transformer"])
```

Run:

```bash
python train.py --model cnn
```

Invalid:

```bash
python train.py --model abc
```

Error occurs.

### 10. Multiple Values

Example:

```python
parser.add_argument("--layers", nargs="+", type=int)
```

Run:

```bash
python script.py --layers 64 128 256
```

Output:

```
[64,128,256]
```

### 11. Subcommands (Advanced CLI)

Used in tools like `git`.

Example:

```text
git commit
git push
git pull
```

Example in argparse:

```python
import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")

train = subparsers.add_parser("train")
train.add_argument("--epochs", type=int)

test = subparsers.add_parser("test")

args = parser.parse_args()

print(args.command)
```

Run:

```bash
python script.py train --epochs 10
```

Output:

```
train
```

### 12. Real ML Training CLI Example

Example:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--dataset", required=True)
parser.add_argument("--epochs", type=int, default=10)
parser.add_argument("--batch-size", type=int, default=32)
parser.add_argument("--lr", type=float, default=0.001)

args = parser.parse_args()

print("Dataset:", args.dataset)
print("Epochs:", args.epochs)
print("Batch size:", args.batch_size)
print("Learning rate:", args.lr)
```

Run:

```bash
python train.py --dataset data.csv --epochs 20
```

### 13. CLI Architecture

```text
Command Line
     |
argparse parser
     |
Argument object
     |
Program logic
```

### 14. Modules Commonly Used With `argparse`

CLI tools often combine:

```text
argparse → command line inputs
logging → application logs
pathlib → file handling
json/yaml → configuration files
```

Example architecture:

```text
CLI tool
   |
Arguments
   |
Processing pipeline
   |
Logging
```

### Real Systems Using argparse

`argparse` is used in:

```text
ML training pipelines
data engineering tools
automation scripts
DevOps utilities
ETL pipelines
```

Example:

```bash
python preprocess.py --input data.csv --output clean.csv
```

### Key `argparse` Concepts

```text
ArgumentParser
add_argument()
parse_args()
flags
positional arguments
subcommands
```

These are enough to build  **professional CLI applications** .

### Next Step (Project)

Now that you understand `argparse`, the best way to master it is by building a  **real CLI tool** .

We can build something very practical:

1️⃣ **File Organizer CLI**

Example usage:

```bash
python organizer.py --source downloads --mode images
```

2️⃣ **Dataset Processor CLI**

```bash
python dataset_tool.py --dataset data --resize 256
```

3️⃣ **Log Analyzer CLI**

```bash
python log_tool.py --logfile app.log --errors
```

These projects combine:

```text
argparse
pathlib
shutil
logging
```

* [ ] exactly like  **real production automation tools** .
