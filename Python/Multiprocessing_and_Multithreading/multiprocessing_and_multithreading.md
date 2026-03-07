## Python Multiprocessing (Complete Explanation)

Multiprocessing is used when we want a program to  **run multiple processes simultaneously using multiple CPU cores** .

This is extremely useful for:

* **CPU-intensive tasks**
* **Machine learning preprocessing**
* **Data processing pipelines**
* **Large mathematical computations**

### Why Multiprocessing is Needed

Normally Python programs run  **sequentially** .

Example:

```python
def task():
    for i in range(5):
        print(i)

task()
task()
```

Execution:

```
Task1 → finish
Task2 → start
```

Only  **one task runs at a time** .

### Problem: CPU-Intensive Work

Example:

```text
image processing
matrix multiplication
machine learning preprocessing
video encoding
```

These tasks can take a lot of time.

Modern computers have  **multiple CPU cores** , but normal Python programs often use  **only one core** .

Multiprocessing allows us to  **use all CPU cores** .

### Processes vs Threads

| Feature   | Process          | Thread          |
| --------- | ---------------- | --------------- |
| Memory    | Separate memory  | Shared memory   |
| Speed     | Slower creation  | Faster creation |
| CPU usage | True parallelism | Limited by GIL  |
| Isolation | Strong           | Weak            |

Python threads are limited by something called the  **GIL (Global Interpreter Lock)** .

Because of the GIL:

```text
threads cannot run CPU-heavy code in true parallel
```

Multiprocessing avoids this limitation.

### Basic Multiprocessing Example

Python provides the module:

```python
multiprocessing
```

Example:

```python
from multiprocessing import Process

def task():
    print("Task running")

p = Process(target=task)

p.start()
p.join()
```

Output:

```
Task running
```

### How It Works

```
Main Process
     |
     |--- create new process
     |
     |--- run function in parallel
```

Execution flow:

```
Process created
Process started
Process finished
```

### Important Methods

| Method          | Purpose                    |
| --------------- | -------------------------- |
| `start()`     | start process              |
| `join()`      | wait for process to finish |
| `terminate()` | stop process               |

### Example: Multiple Processes

```python
from multiprocessing import Process

def worker(n):
    print("Worker", n)

processes = []

for i in range(3):
    p = Process(target=worker, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()
```

Output (order may vary):

```
Worker 0
Worker 1
Worker 2
```

Processes run  **independently** .

### Process ID Example

Each process has a  **unique PID** .

```python
import os
from multiprocessing import Process

def task():
    print("Process ID:", os.getpid())

p = Process(target=task)

p.start()
p.join()
```

Example output:

```
Process ID: 12345
```

### CPU Core Utilization

Suppose your CPU has:

```
8 cores
```

Multiprocessing allows:

```
8 tasks running simultaneously
```

### Example: CPU Intensive Task

Without multiprocessing:

```python
import time

def square_numbers():
    for i in range(100000000):
        i*i

start = time.time()

square_numbers()
square_numbers()

print("Time:", time.time() - start)
```

With multiprocessing:

```python
import time
from multiprocessing import Process

def square_numbers():
    for i in range(100000000):
        i*i

start = time.time()

p1 = Process(target=square_numbers)
p2 = Process(target=square_numbers)

p1.start()
p2.start()

p1.join()
p2.join()

print("Time:", time.time() - start)
```

This runs  **faster because both tasks run on different cores** .

### Multiprocessing Pool

Creating many processes manually can be difficult.

Python provides  **Process Pools** .

Example:

```python
from multiprocessing import Pool

def square(n):
    return n*n

with Pool(4) as p:
    result = p.map(square, [1,2,3,4,5])

print(result)
```

Output:

```
[1,4,9,16,25]
```

Here:

```
Pool(4) → uses 4 worker processes
```

### Pool Workflow

```
Main Program
      |
      |-- Pool of workers
      |
      |-- distribute tasks
      |
      |-- collect results
```

### Sharing Data Between Processes

Processes have  **separate memory** , so sharing data requires special objects.

Example:

```python
from multiprocessing import Value

counter = Value('i', 0)
```

Or using:

```
Queue
Pipe
Manager
```

### Example: Using Queue

```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello")

q = Queue()

p = Process(target=worker, args=(q,))
p.start()

print(q.get())

p.join()
```

Output:

```
Hello
```

Queue allows  **communication between processes** .

### Key Multiprocessing Components

| Component   | Purpose                 |
| ----------- | ----------------------- |
| `Process` | create process          |
| `Pool`    | manage worker processes |
| `Queue`   | communication           |
| `Pipe`    | two-way communication   |
| `Manager` | shared objects          |

### Multiprocessing Architecture

```
Main Process
     |
     |--- Worker Process 1
     |--- Worker Process 2
     |--- Worker Process 3
```

Each worker has  **its own memory space** .

### Multiprocessing vs Multithreading

| Feature    | Multithreading | Multiprocessing |
| ---------- | -------------- | --------------- |
| GIL impact | Yes            | No              |
| Memory     | Shared         | Separate        |
| Best for   | I/O tasks      | CPU tasks       |
| Speed      | Limited        | True parallel   |

Example:

```
Web requests → threading
Image processing → multiprocessing
```

### Real Use Cases

Multiprocessing is used in:

```
ML data preprocessing
ETL pipelines
image processing
video encoding
scientific simulations
```

Example ML pipeline:

```
Load images
Resize images
Normalize data
Train model
```

Each step can run  **in parallel processes** .

### Key Idea Summary

Multiprocessing allows:

```
multiple CPU cores
true parallel execution
faster CPU-heavy tasks
```

Core tools:

```
Process
Pool
Queue
Pipe
Manager
```

---

## Python Multiprocessing — Advanced Concepts

Now we go deeper into multiprocessing. These topics are **very important for real-world systems** and  **data processing pipelines** .

We will cover:

1. Process Pools (in depth)
2. Shared Memory (`Value`, `Array`)
3. Process Communication (`Queue`, `Pipe`)
4. Process Synchronization (`Lock`, `Semaphore`)
5. Multiprocessing vs Threading vs Async (when to use each)

### 1. Process Pool (Worker Pool)

Creating processes manually can be inefficient if we have  **many tasks** .

Instead of creating new processes repeatedly, Python provides a  **Pool of worker processes** .

Structure:

```
Main Process
      |
      |---- Worker 1
      |---- Worker 2
      |---- Worker 3
      |---- Worker 4
```

Tasks are distributed among these workers.

### Basic Pool Example

```python
from multiprocessing import Pool

def square(x):
    return x * x

with Pool(4) as p:
    result = p.map(square, [1,2,3,4,5])

print(result)
```

Output

```
[1, 4, 9, 16, 25]
```

Here:

```
Pool(4) → 4 worker processes
```

Tasks are distributed automatically.

### `map()` vs `apply()`

`map()` → processes multiple inputs

```python
p.map(func, iterable)
```

Example:

```python
p.map(square, [1,2,3,4])
```

`apply()` → executes a single function

```python
p.apply(square, (5,))
```

### `apply_async()` (Asynchronous Execution)

```python
from multiprocessing import Pool

def square(n):
    return n*n

pool = Pool(2)

result = pool.apply_async(square, (5,))

print(result.get())
```

Output

```
25
```

Here the task runs  **asynchronously** .

### Pool Methods

| Method            | Purpose                |
| ----------------- | ---------------------- |
| `map()`         | parallel map operation |
| `apply()`       | run one function       |
| `apply_async()` | async execution        |
| `close()`       | stop accepting tasks   |
| `join()`        | wait for completion    |

### 2. Shared Memory

Processes normally have  **separate memory spaces** .

This means:

```
Process A cannot directly access Process B variables
```

Python provides special objects for  **shared memory** .

### Shared `Value`

Example:

```python
from multiprocessing import Process, Value

def increment(counter):
    counter.value += 1

counter = Value('i', 0)

p1 = Process(target=increment, args=(counter,))
p2 = Process(target=increment, args=(counter,))

p1.start()
p2.start()

p1.join()
p2.join()

print(counter.value)
```

Output

```
2
```

Here:

```
Value('i', 0)
```

means:

```
i → integer
0 → initial value
```

### Shared `Array`

Example:

```python
from multiprocessing import Process, Array

def modify(arr):
    arr[0] = 100

arr = Array('i', [1,2,3])

p = Process(target=modify, args=(arr,))
p.start()
p.join()

print(arr[:])
```

Output

```
[100, 2, 3]
```

### Shared Memory Structure

```
Shared Memory
      |
      |--- Value
      |--- Array
```

### 3. Process Communication

Processes communicate using:

```
Queue
Pipe
```

### Queue Example

```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello from process")

q = Queue()

p = Process(target=worker, args=(q,))
p.start()

print(q.get())

p.join()
```

Output

```
Hello from process
```

Queue is  **thread-safe and process-safe** .

### Pipe Example

Pipe provides  **two-way communication** .

```python
from multiprocessing import Process, Pipe

def worker(conn):
    conn.send("Message from worker")
    conn.close()

parent_conn, child_conn = Pipe()

p = Process(target=worker, args=(child_conn,))
p.start()

print(parent_conn.recv())

p.join()
```

Output

```
Message from worker
```

### Queue vs Pipe

| Feature       | Queue         | Pipe                 |
| ------------- | ------------- | -------------------- |
| Communication | Multi-process | Two processes        |
| Structure     | FIFO          | Two endpoints        |
| Use case      | Task sharing  | Direct communication |

### 4. Process Synchronization

When multiple processes access  **shared resources** , conflicts may occur.

Example problem:

```
Two processes updating same variable
```

Solution: **Locks**

### Lock Example

```python
from multiprocessing import Process, Lock

def task(lock):
    lock.acquire()
    print("Process running")
    lock.release()

lock = Lock()

p1 = Process(target=task, args=(lock,))
p2 = Process(target=task, args=(lock,))

p1.start()
p2.start()

p1.join()
p2.join()
```

Lock ensures  **only one process executes critical code at a time** .

### Semaphore

Semaphore allows  **limited number of processes simultaneously** .

Example:

```
Database connections limit = 5
```

### Semaphore Example

```python
from multiprocessing import Semaphore

sem = Semaphore(2)
```

This allows  **2 processes simultaneously** .

### 5. Multiprocessing vs Threading vs Async

Understanding this is  **very important in system design** .

| Feature         | Multiprocessing  | Multithreading | Async            |
| --------------- | ---------------- | -------------- | ---------------- |
| CPU parallelism | Yes              | Limited        | No               |
| Memory          | Separate         | Shared         | Shared           |
| Best for        | CPU tasks        | I/O tasks      | High concurrency |
| Example         | ML preprocessing | Web requests   | FastAPI servers  |

### When to Use Each

CPU heavy tasks:

```
image processing
video encoding
ML feature engineering
```

→ Use **multiprocessing**

I/O heavy tasks:

```
API requests
database queries
web scraping
```

→ Use **multithreading**

Massive concurrent systems:

```
high performance APIs
chat servers
real-time streaming
```

→ Use **async programming**

### Real ML Example

Training pipeline:

```
Load images
Resize images
Normalize
Create batches
Train model
```

Multiprocessing can parallelize:

```
image preprocessing
feature extraction
data loading
```

### Key Multiprocessing Tools

```
Process
Pool
Queue
Pipe
Value
Array
Lock
Semaphore
```

### Multiprocessing Architecture

```
Main Process
     |
     |--- Worker Process 1
     |--- Worker Process 2
     |--- Worker Process 3
     |--- Worker Process 4
```

All workers run  **in parallel on multiple CPU cores** .

### Key Takeaway

Multiprocessing is best when:

```
tasks are CPU intensive
parallel computation needed
large datasets processed
```


---



## Python Multithreading (Detailed Explanation)

Multithreading allows a program to  **run multiple threads inside a single process** .

Each thread executes  **independently** , but all threads  **share the same memory space** .

Multithreading is mainly useful for **I/O-bound tasks** such as:

```
API requests
file reading/writing
database queries
web scraping
network operations
```

### 1. Process vs Thread

First understand the difference.

Process:

```
Independent program execution
Separate memory
```

Thread:

```
Lightweight execution unit inside a process
Shared memory
```

Structure:

```
Process
   |
   |--- Thread 1
   |--- Thread 2
   |--- Thread 3
```

Threads run concurrently inside the same process.

### 2. Why Multithreading is Useful

Consider a program that downloads files.

Sequential execution:

```
Download file1 → wait
Download file2 → wait
Download file3 → wait
```

Multithreading:

```
Download file1
Download file2
Download file3
```

All downloads happen  **simultaneously** .

### 3. Python Threading Module

Python provides:

```python
threading
```

Basic thread example:

```python
import threading

def task():
    print("Thread running")

t = threading.Thread(target=task)

t.start()
t.join()
```

Output:

```
Thread running
```

### Thread Methods

| Method         | Purpose                   |
| -------------- | ------------------------- |
| `start()`    | start thread              |
| `join()`     | wait for thread to finish |
| `is_alive()` | check if running          |

### 4. Running Multiple Threads

Example:

```python
import threading

def worker(n):
    print("Worker", n)

threads = []

for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

Output (order may vary):

```
Worker 0
Worker 1
Worker 2
```

Threads run  **concurrently** .

### 5. Thread Identification

Each thread has an ID.

Example:

```python
import threading

def task():
    print(threading.current_thread().name)

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
```

Output:

```
Thread-1
Thread-2
```

### 6. Multithreading for I/O Tasks

Example: Simulated network request.

Sequential version:

```python
import time

def download():
    print("Downloading...")
    time.sleep(2)

start = time.time()

download()
download()

print("Time:", time.time() - start)
```

Execution:

```
4 seconds
```

Threaded version:

```python
import threading
import time

def download():
    print("Downloading...")
    time.sleep(2)

start = time.time()

t1 = threading.Thread(target=download)
t2 = threading.Thread(target=download)

t1.start()
t2.start()

t1.join()
t2.join()

print("Time:", time.time() - start)
```

Execution:

```
2 seconds
```

Because tasks run  **simultaneously** .

### 7. Shared Memory in Threads

Threads share memory.

Example:

```python
counter = 0

def increment():
    global counter
    counter += 1
```

All threads can access the  **same variable** .

But this can cause problems called  **race conditions** .

### 8. Race Condition Problem

Example:

Two threads updating same variable.

```
Thread1 reads counter
Thread2 reads counter
Thread1 increments
Thread2 increments
```

Final value becomes incorrect.

### 9. Thread Synchronization (Lock)

To prevent race conditions we use  **Lock** .

Example:

```python
import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter

    lock.acquire()
    counter += 1
    lock.release()
```

This ensures  **only one thread modifies the variable at a time** .

Cleaner syntax:

```python
with lock:
    counter += 1
```

### 10. Thread Pool (ThreadPoolExecutor)

Creating many threads manually is inefficient.

Python provides  **thread pools** .

Example:

```python
from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x*x

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, [1,2,3,4])

print(list(results))
```

Output:

```
[1,4,9,16]
```

Thread pools manage threads automatically.

### 11. The Global Interpreter Lock (GIL)

One important concept in Python threading is  **GIL** .

GIL = **Global Interpreter Lock**

Meaning:

```
Only one thread can execute Python bytecode at a time
```

Even if multiple threads exist.

This means:

```
CPU-heavy tasks → threads won't run truly in parallel
```

Example CPU task:

```
large mathematical calculations
machine learning computations
image processing
```

Threads  **won't speed these up** .

### GIL Impact

| Task Type | Threading Benefit |
| --------- | ----------------- |
| I/O tasks | High              |
| CPU tasks | Low               |

For CPU-heavy tasks we use:

```
multiprocessing
```

### 12. Multithreading Architecture

```
Process
   |
   |--- Thread 1
   |--- Thread 2
   |--- Thread 3
```

All threads share:

```
memory
variables
resources
```

### 13. Real World Uses

Multithreading is used in:

```
web servers
file downloads
web scraping
API calls
database queries
GUI applications
```

Example web scraper:

```
Thread1 → scrape page1
Thread2 → scrape page2
Thread3 → scrape page3
```

### 14. Threading vs Multiprocessing

| Feature    | Multithreading | Multiprocessing |
| ---------- | -------------- | --------------- |
| Memory     | Shared         | Separate        |
| GIL impact | Yes            | No              |
| Best for   | I/O tasks      | CPU tasks       |
| Overhead   | Low            | Higher          |

### Simple Rule

```
I/O tasks → Multithreading
CPU tasks → Multiprocessing
```

### 15. Thread Lifecycle

```
Thread Created
      |
      ↓
Thread Started
      |
      ↓
Running
      |
      ↓
Finished
```

### Key Multithreading Tools

```
Thread
Lock
RLock
Semaphore
ThreadPoolExecutor
```

### Key Takeaway

Multithreading allows:

```
concurrent execution
faster I/O operations
better resource utilization
```

But because of  **GIL** , it is  **not ideal for CPU-heavy tasks** .

### Next Important Topic (Very Important for System Design)

The next concept that combines everything you learned is:

## Python Async Programming (`async`, `await`, Event Loop)

This is used in:

```
FastAPI
high performance APIs
web scraping systems
real-time systems
```

It is one of the  **most powerful concurrency models in Python**.
