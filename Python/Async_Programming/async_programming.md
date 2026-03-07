## Python Async Programming (`async` / `await`)

Async programming is a  **concurrency model designed to handle many tasks efficiently without blocking execution** .

It is heavily used in:

* **FastAPI**
* **High-performance APIs**
* **Web scraping**
* **Real-time systems**
* **Network servers**
* **Microservices**

Async programming is best for  **I/O-bound tasks** , where programs spend a lot of time  **waiting for external resources** .

Examples:

```text
API requests
database queries
file operations
network calls
```

### 1. The Problem: Blocking Code

Consider this example:

```python
import time

def task1():
    print("Task 1 start")
    time.sleep(2)
    print("Task 1 end")

def task2():
    print("Task 2 start")
    time.sleep(2)
    print("Task 2 end")

task1()
task2()
```

Execution:

```
Task1 start
(wait 2s)
Task1 end
Task2 start
(wait 2s)
Task2 end
```

Total time:

```
4 seconds
```

The program  **blocks while waiting** .

### 2. Async Solution

Async allows tasks to  **run while waiting for I/O operations** .

Instead of blocking, the program  **switches to another task** .

Conceptual model:

```
Task1 waiting
      ↓
Switch to Task2
      ↓
Task2 waiting
      ↓
Return to Task1
```

### 3. Async Keywords

Async programming introduces two important keywords:

```text
async
await
```

| Keyword   | Purpose                              |
| --------- | ------------------------------------ |
| `async` | defines asynchronous function        |
| `await` | pauses execution until task finishes |

### 4. Basic Async Function

Example:

```python
import asyncio

async def hello():
    print("Hello")
```

Calling it normally:

```python
hello()
```

does  **not execute immediately** .

Instead it returns a  **coroutine object** .

Example:

```python
print(hello())
```

Output:

```
<coroutine object hello at ...>
```

To run async functions we use  **event loop** .

### 5. Running Async Code

Example:

```python
import asyncio

async def hello():
    print("Hello")

asyncio.run(hello())
```

Output:

```
Hello
```

### 6. Async Example with Waiting

Example:

```python
import asyncio

async def task1():
    print("Task1 start")
    await asyncio.sleep(2)
    print("Task1 end")

async def task2():
    print("Task2 start")
    await asyncio.sleep(2)
    print("Task2 end")

async def main():
    await task1()
    await task2()

asyncio.run(main())
```

This still runs sequentially.

Total time:

```
4 seconds
```

### 7. Running Tasks Concurrently

To run tasks together we use:

```python
asyncio.gather()
```

Example:

```python
import asyncio

async def task1():
    print("Task1 start")
    await asyncio.sleep(2)
    print("Task1 end")

async def task2():
    print("Task2 start")
    await asyncio.sleep(2)
    print("Task2 end")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

Execution:

```
Task1 start
Task2 start
(wait 2s)
Task1 end
Task2 end
```

Total time:

```
2 seconds
```

### 8. Event Loop

Async programming works using an  **event loop** .

The event loop:

```
1. schedules tasks
2. switches tasks while waiting
3. resumes tasks when ready
```

Architecture:

```
Event Loop
     |
     |---- Task1
     |---- Task2
     |---- Task3
```

Tasks run  **cooperatively** .

### 9. Coroutine

An  **async function is called a coroutine** .

Example:

```python
async def fetch_data():
    pass
```

Calling it returns a coroutine:

```python
fetch_data()
```

Execution requires:

```python
await
```

or

```python
asyncio.run()
```

### 10. Async Web Request Example

Example using `aiohttp`.

```python
import aiohttp
import asyncio

async def fetch(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():

    urls = [
        "https://example.com",
        "https://example.com",
        "https://example.com"
    ]

    tasks = [fetch(url) for url in urls]

    results = await asyncio.gather(*tasks)

    print(results)

asyncio.run(main())
```

This fetches  **multiple web pages simultaneously** .

### 11. Async vs Threading vs Multiprocessing

| Feature           | Async      | Threading  | Multiprocessing |
| ----------------- | ---------- | ---------- | --------------- |
| Best for          | I/O tasks  | I/O tasks  | CPU tasks       |
| Memory usage      | Very low   | Low        | Higher          |
| CPU parallelism   | No         | Limited    | Yes             |
| Context switching | Event loop | OS threads | OS processes    |

### When to Use Each

Async:

```
High concurrency APIs
web scraping
network servers
```

Threading:

```
file downloads
background I/O tasks
GUI applications
```

Multiprocessing:

```
machine learning preprocessing
video encoding
scientific computing
```

### 12. Real Example: FastAPI

FastAPI endpoints use async functions.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello"}
```

FastAPI uses async to  **handle thousands of requests concurrently** .

### Async Execution Model

```
Task Start
     |
     |-- running
     |
     |-- await I/O
     |
Switch to another task
     |
Resume task
```

### Key Concepts Summary

Async programming uses:

```
async
await
coroutines
event loop
```

Advantages:

```
high concurrency
efficient I/O handling
low memory usage
```

Common libraries using async:

```
FastAPI
aiohttp
asyncpg
websockets
```

### Important Mental Model

```
Threading → multiple workers
Multiprocessing → multiple CPUs
Async → single worker switching tasks efficiently
```

---

## Advanced Async Programming in Python

Now we go deeper into **advanced async concepts** used in real systems like:

```text
FastAPI
WebSocket servers
High-performance APIs
Real-time streaming systems
```

We will cover:

1. `asyncio.create_task()`
2. Async Generators
3. Async Context Managers
4. Async Queues
5. Building Async Pipelines

### 1. `asyncio.create_task()`

`create_task()` schedules a coroutine to  **run concurrently in the event loop** .

Earlier we used:

```python
await asyncio.gather(task1(), task2())
```

But sometimes we want to  **schedule tasks and run them independently** .

Example:

```python
import asyncio

async def worker(name):

    print(name, "started")

    await asyncio.sleep(2)

    print(name, "finished")


async def main():

    task1 = asyncio.create_task(worker("Task1"))
    task2 = asyncio.create_task(worker("Task2"))

    await task1
    await task2


asyncio.run(main())
```

Output

```
Task1 started
Task2 started
Task1 finished
Task2 finished
```

Execution model:

```
Event Loop
     |
     |---- Task1
     |---- Task2
```

Both run concurrently.

### `create_task()` vs `await`

`await`

```
waits immediately
```

`create_task()`

```
schedules task and continues execution
```

Example:

```python
async def main():

    task = asyncio.create_task(worker("Task1"))

    print("Main running")

    await task
```

Output

```
Main running
Task1 started
Task1 finished
```

### 2. Async Generators

Async generators combine:

```
async functions
yield
```

They produce  **asynchronous streams of data** .

Example:

```python
import asyncio

async def generate():

    for i in range(3):
        await asyncio.sleep(1)
        yield i
```

Usage:

```python
async def main():

    async for value in generate():
        print(value)

asyncio.run(main())
```

Output

```
0
1
2
```

Structure:

```
async generator
      |
      | yield value
      | await operation
```

Used in:

```
real-time streaming
sensor data
API streams
```

### 3. Async Context Managers

Async context managers work with:

```
async with
```

They implement:

```
__aenter__()
__aexit__()
```

Example:

```python
import asyncio

class AsyncManager:

    async def __aenter__(self):
        print("Entering context")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Exiting context")


async def main():

    async with AsyncManager():
        print("Inside block")

asyncio.run(main())
```

Output

```
Entering context
Inside block
Exiting context
```

Used in libraries like:

```
aiohttp
async database clients
websocket servers
```

Example:

```python
async with aiohttp.ClientSession() as session:
```

### 4. Async Queue

Async queues allow  **communication between async tasks** .

Example:

```python
import asyncio

async def producer(queue):

    for i in range(5):

        print("Producing", i)

        await queue.put(i)

        await asyncio.sleep(1)


async def consumer(queue):

    while True:

        item = await queue.get()

        print("Consumed", item)

        queue.task_done()


async def main():

    queue = asyncio.Queue()

    asyncio.create_task(producer(queue))
    asyncio.create_task(consumer(queue))

    await asyncio.sleep(6)

asyncio.run(main())
```

Output:

```
Producing 0
Consumed 0
Producing 1
Consumed 1
...
```

Structure:

```
Producer → Queue → Consumer
```

Used in:

```
stream processing
message pipelines
task scheduling
```

### 5. Async Pipeline Example

Example: data processing pipeline.

Step1: produce numbers
Step2: square numbers
Step3: print result

Example:

```python
import asyncio

async def producer(queue):

    for i in range(5):

        await queue.put(i)

    await queue.put(None)


async def worker(queue):

    while True:

        item = await queue.get()

        if item is None:
            break

        print("Square:", item*item)


async def main():

    queue = asyncio.Queue()

    p = asyncio.create_task(producer(queue))
    w = asyncio.create_task(worker(queue))

    await p
    await w


asyncio.run(main())
```

Pipeline model:

```
Producer
    |
Queue
    |
Worker
```

This pattern is used in:

```
data pipelines
real-time analytics
ML preprocessing
```

### Async Architecture

```
Event Loop
     |
     |---- Coroutine 1
     |---- Coroutine 2
     |---- Coroutine 3
```

Tasks yield control using:

```
await
```

### Real Systems Using Async

Async is used heavily in:

```
FastAPI
Discord bots
web scraping systems
real-time trading systems
WebSocket servers
```

Example FastAPI endpoint:

```python
@app.get("/users")
async def get_users():
    return await database.fetch_users()
```

Thousands of requests can run concurrently.

### Key Async Tools

```
async
await
asyncio.run()
create_task()
gather()
async for
async with
asyncio.Queue
```

### Async vs Threading vs Multiprocessing

| Feature         | Async                | Threading | Multiprocessing |
| --------------- | -------------------- | --------- | --------------- |
| CPU parallelism | No                   | Limited   | Yes             |
| Memory          | Very low             | Low       | High            |
| Best for        | High concurrency I/O | I/O tasks | CPU tasks       |

### Mental Model

```
Multiprocessing → many CPUs
Threading → many workers
Async → single worker switching tasks
```

### Important Real-World Skill

Modern backend systems often combine:

```
async programming
thread pools
process pools
```

Example architecture:

```
FastAPI (async)
      |
Thread pool → blocking I/O
      |
Process pool → CPU tasks
```

xxxxxxxxxxx
