## Memory Optimization in Python

Memory optimization means  **reducing the amount of RAM your program uses while maintaining performance** .

This becomes very important in:

```text
machine learning pipelines
large datasets
data processing systems
high-performance applications
```

Large Python programs can consume **GBs of memory** if not optimized.

We will cover the most important techniques:

1. Understanding Python Memory Model
2. Using Generators Instead of Lists
3. Using `__slots__`
4. Efficient Data Structures
5. Memory Profiling
6. Object Reuse and Interning
7. Chunk Processing
8. Lazy Evaluation

### 1. Python Memory Model (Basic Idea)

Every variable in Python is an  **object stored in memory** .

Example:

```python
x = 10
```

Python internally creates:

```
Object (10)
   |
Reference → x
```

Multiple variables can point to the same object.

Example:

```python
a = 10
b = a
```

Structure:

```
Object 10
 |     |
 a     b
```

Python uses **reference counting and garbage collection** to manage memory.

### 2. Lists vs Generators

Lists store  **all elements in memory** .

Example:

```python
nums = [i*i for i in range(10000000)]
```

This creates  **10 million numbers in RAM** .

Generator version:

```python
nums = (i*i for i in range(10000000))
```

This generates numbers  **only when needed** .

Memory comparison:

```
List → high memory
Generator → minimal memory
```

Example usage:

```python
for n in nums:
    print(n)
```

### 3. Using `__slots__`

Normal Python objects store attributes in a  **dictionary** .

Example:

```python
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
```

Internally each object stores:

```
object
 |
 |-- __dict__
```

This consumes extra memory.

Using `__slots__` removes `__dict__`.

Example:

```python
class User:

    __slots__ = ("name","age")

    def __init__(self,name,age):
        self.name=name
        self.age=age
```

Benefits:

```
less memory usage
faster attribute access
```

Useful when creating  **millions of objects** .

### 4. Using Efficient Data Structures

Choosing the correct data structure saves memory.

Example:

List:

```python
numbers = [1,2,3,4]
```

Tuple:

```python
numbers = (1,2,3,4)
```

Tuple advantages:

```
immutable
smaller memory footprint
```

For large constant datasets, prefer  **tuples** .

### 5. Using `array` Instead of List

Lists store  **full Python objects** , which consumes more memory.

Example:

```python
numbers = [1,2,3,4]
```

Using array:

```python
import array

numbers = array.array('i',[1,2,3,4])
```

Memory comparison:

```
list → stores objects
array → stores raw values
```

Useful for  **numeric datasets** .

### 6. Memory Profiling

To optimize memory, we must  **measure memory usage** .

Useful library:

```python
memory_profiler
```

Install:

```
pip install memory-profiler
```

Example:

```python
from memory_profiler import profile

@profile
def create_list():
    a = [i for i in range(1000000)]
    return a

create_list()
```

This shows  **memory usage per line** .

Another tool:

```python
sys.getsizeof()
```

Example:

```python
import sys

a = [1,2,3,4]

print(sys.getsizeof(a))
```

### 7. Chunk Processing

Instead of loading entire data, process it  **in chunks** .

Bad approach:

```python
data = file.read()
```

Better approach:

```python
with open("data.txt") as f:
    for line in f:
        process(line)
```

This loads  **one line at a time** .

Chunk example:

```python
def read_chunks(file,size):

    while True:

        chunk = file.read(size)

        if not chunk:
            break

        yield chunk
```

### 8. Lazy Evaluation

Lazy evaluation means  **compute values only when needed** .

Example:

```python
map()
filter()
zip()
```

Example:

```python
nums = map(lambda x: x*x, range(1000000))
```

This  **does not compute immediately** .

Values are generated  **only when iterated** .

### 9. Using `del` to Free Memory

Sometimes large objects stay in memory longer than needed.

Example:

```python
data = load_big_dataset()

process(data)

del data
```

This allows Python to  **free memory sooner** .

### 10. Avoiding Unnecessary Copies

Bad:

```python
b = a.copy()
```

Better:

```
use reference if modification not needed
```

Example:

```python
b = a
```

### 11. Using `itertools`

`itertools` provides memory-efficient operations.

Example:

```python
import itertools

nums = itertools.count(1)
```

This produces  **infinite sequence without storing values** .

Another example:

```python
import itertools

result = itertools.islice(range(1000000),10)
```

Only first  **10 values are generated** .

### 12. NumPy Instead of Lists

NumPy arrays are far more memory-efficient.

Example:

```python
import numpy as np

a = np.array([1,2,3,4])
```

Comparison:

```
Python list → object storage
NumPy array → contiguous memory
```

Used heavily in  **machine learning and scientific computing** .

### 13. Garbage Collection

Python automatically removes unused objects.

Example:

```python
import gc

gc.collect()
```

Garbage collector handles  **cyclic references** .

### Python Memory Architecture

```
Python Program
      |
      |-- Stack (function calls)
      |
      |-- Heap (objects stored here)
```

Objects live in  **heap memory** .

### Key Memory Optimization Techniques

```
Use generators
Use __slots__
Use efficient data structures
Process data in chunks
Avoid unnecessary copies
Use NumPy for numeric data
Profile memory usage
```

### Real Example: Data Processing

Bad approach:

```
Load entire dataset
Process
Store result
```

Better approach:

```
Stream dataset
Process batch
Release memory
```

This approach is used in:

```
ML pipelines
ETL systems
data streaming
```

### Key Insight

Most memory issues come from:

```
loading too much data
creating unnecessary objects
storing large lists
```

Optimized Python programs use:

```
generators
lazy evaluation
stream processing
```

---

## Python Performance Optimization

Performance optimization means  **making Python programs run faster and more efficiently** .

It becomes very important when working with:

```text
large datasets
machine learning pipelines
data engineering systems
high-performance APIs
scientific computing
```

Python is  **not the fastest language** , but with the right techniques it can become  **extremely efficient** .

We will cover the most important techniques:

1. Profiling Code (Find Bottlenecks)
2. Algorithm Optimization
3. Using Built-in Functions
4. Vectorization with NumPy
5. Using Numba
6. Using Cython
7. Reducing Function Calls
8. Avoiding Global Variables
9. Using PyPy
10. Parallel Processing

### 1. Profiling Code

Before optimizing, we must  **identify the slow parts of the program** .

This process is called  **profiling** .

Python provides:

```text
cProfile
```

Example:

```python
import cProfile

def slow_function():
    total = 0
    for i in range(10000000):
        total += i
    return total

cProfile.run("slow_function()")
```

This shows:

```text
number of function calls
time spent in each function
```

This helps locate the  **performance bottleneck** .

Another profiling tool:

```python
import time
```

Example:

```python
import time

start = time.time()

for i in range(1000000):
    pass

end = time.time()

print("Time:", end - start)
```

### 2. Algorithm Optimization

The **biggest performance improvement** usually comes from choosing a better algorithm.

Example:

Slow approach:

```python
nums = list(range(10000))

for i in nums:
    if i in nums:
        pass
```

Time complexity:

```text
O(n²)
```

Better approach using set:

```python
nums = set(range(10000))

for i in nums:
    if i in nums:
        pass
```

Time complexity:

```text
O(n)
```

Using correct data structures improves performance drastically.

### 3. Using Built-in Functions

Python built-ins are  **implemented in C** , making them much faster.

Example:

Slow loop:

```python
total = 0

for i in range(1000000):
    total += i
```

Faster version:

```python
total = sum(range(1000000))
```

Other fast built-ins:

```text
sum()
min()
max()
sorted()
any()
all()
map()
filter()
```

### 4. Vectorization with NumPy

Loops in Python are slow.

NumPy allows  **vectorized operations** , which are extremely fast.

Example:

Normal Python loop:

```python
a = [1,2,3,4]

result = []

for i in a:
    result.append(i*2)
```

NumPy version:

```python
import numpy as np

a = np.array([1,2,3,4])

result = a * 2
```

This is much faster because NumPy operations run in  **compiled C code** .

Used heavily in:

```text
machine learning
scientific computing
data science
```

### 5. Using Numba (JIT Compilation)

Numba can convert Python code into  **machine code at runtime** .

Example:

```python
from numba import jit

@jit
def compute():

    total = 0

    for i in range(10000000):
        total += i

    return total

compute()
```

Numba compiles the function using  **LLVM** , making it much faster.

Best for:

```text
numerical computations
loops
scientific calculations
```

### 6. Using Cython

Cython converts Python code into  **C code** .

Example:

```python
def add(int a, int b):
    return a + b
```

This can run  **much faster than pure Python** .

Used in large libraries like:

```text
pandas
scikit-learn
```

### 7. Reducing Function Calls

Function calls add overhead.

Example:

Slow:

```python
def square(x):
    return x*x

for i in range(1000000):
    square(i)
```

Faster:

```python
for i in range(1000000):
    i*i
```

Reducing unnecessary function calls improves performance.

### 8. Avoid Global Variables

Accessing global variables is slower.

Example:

Slow:

```python
x = 10

def func():
    return x
```

Better:

```python
def func(x):
    return x
```

Local variables are accessed faster.

### 9. Using PyPy

PyPy is an  **alternative Python interpreter** .

It uses  **Just-In-Time compilation (JIT)** .

Example benefits:

```text
2x to 10x speed improvement
```

Works well for:

```text
pure Python loops
algorithm-heavy code
```

But some libraries may not be fully compatible.

### 10. Parallel Processing

We can speed up programs using:

```text
multiprocessing
multithreading
async programming
```

Example using multiprocessing:

```python
from multiprocessing import Pool

def square(x):
    return x*x

with Pool(4) as p:
    result = p.map(square, range(10))

print(result)
```

This uses  **multiple CPU cores** .

### Performance Optimization Strategy

Professional developers follow this order:

```text
1. Profile the code
2. Improve algorithm
3. Use built-in functions
4. Use vectorization
5. Use parallel processing
6. Use JIT/C extensions
```

### Example: Optimizing Data Processing

Slow version:

```python
data = []

for i in range(1000000):
    data.append(i*i)
```

Better version:

```python
data = [i*i for i in range(1000000)]
```

Even faster with NumPy:

```python
import numpy as np

data = np.arange(1000000)**2
```

### Real Systems Use These Techniques

These optimization methods are used in:

```text
machine learning frameworks
financial trading systems
scientific simulations
large-scale data pipelines
```

Libraries like:

```text
NumPy
Pandas
TensorFlow
PyTorch
```

use **C extensions, vectorization, and parallel processing** internally.

### Key Performance Optimization Techniques

```text
Profile before optimizing
Choose better algorithms
Use built-in functions
Use vectorization (NumPy)
Use JIT compilation (Numba)
Use multiprocessing
Avoid unnecessary object creation
```

---

## Python Design Patterns

Design patterns are  **reusable solutions to common software design problems** .
They help developers write  **clean, scalable, and maintainable code** .

Large frameworks like **Django, TensorFlow, FastAPI, and Pandas** use design patterns internally.

Design patterns are usually divided into  **three categories** .

### 1. Creational Patterns

Used for  **object creation mechanisms** .

Examples:

```text
Singleton
Factory
Builder
Prototype
```

### 2. Structural Patterns

Used to  **organize relationships between classes and objects** .

Examples:

```text
Adapter
Decorator
Facade
Proxy
```

### 3. Behavioral Patterns

Used to define  **communication between objects** .

Examples:

```text
Observer
Strategy
Command
Iterator
```

We will start with the  **most important patterns used in Python** .

## 1. Singleton Pattern

Singleton ensures **only one instance of a class exists** in the entire program.

Used when we need a  **single shared resource** .

Examples:

```text
database connection
configuration manager
logging system
```

### Example

```python
class Singleton:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance
```

Usage:

```python
a = Singleton()
b = Singleton()

print(a is b)
```

Output:

```
True
```

Both variables refer to  **the same object** .

### Structure

```
Singleton Class
      |
      |-- single instance shared
```

## 2. Factory Pattern

Factory pattern is used to  **create objects without specifying the exact class** .

It provides a  **centralized object creation method** .

Example problem:

```text
Create different types of vehicles
Car
Bike
Truck
```

### Example

```python
class Car:
    def drive(self):
        print("Car driving")

class Bike:
    def drive(self):
        print("Bike driving")


class VehicleFactory:

    def create_vehicle(self, vehicle_type):

        if vehicle_type == "car":
            return Car()

        if vehicle_type == "bike":
            return Bike()
```

Usage:

```python
factory = VehicleFactory()

vehicle = factory.create_vehicle("car")

vehicle.drive()
```

Output:

```
Car driving
```

### Structure

```
Factory
   |
   |-- create object
   |
Car   Bike
```

Factory pattern is used heavily in:

```text
machine learning model loaders
database connectors
plugin systems
```

## 3. Decorator Pattern

Decorator pattern allows  **adding functionality to objects dynamically** .

You already saw decorators in Python.

Example:

```python
def log(func):

    def wrapper():

        print("Function started")

        func()

        print("Function ended")

    return wrapper


@log
def task():
    print("Running task")

task()
```

Output:

```
Function started
Running task
Function ended
```

The decorator  **wraps the original function** .

Structure:

```
Decorator
   |
Original Function
```

This pattern is used in:

```text
Flask routes
FastAPI endpoints
authentication systems
logging systems
```

## 4. Observer Pattern

Observer pattern allows  **objects to subscribe to events** .

When something changes, all observers are notified.

Example:

```text
Stock price changes
notify traders
```

### Example

```python
class Subject:

    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
```

Observer class:

```python
class Observer:

    def update(self, message):
        print("Received:", message)
```

Usage:

```python
subject = Subject()

obs1 = Observer()
obs2 = Observer()

subject.subscribe(obs1)
subject.subscribe(obs2)

subject.notify("Stock price updated")
```

Output:

```
Received: Stock price updated
Received: Stock price updated
```

Structure:

```
Subject
   |
Observers
```

Used in:

```text
event systems
GUI frameworks
message brokers
```

## 5. Strategy Pattern

Strategy pattern allows  **switching algorithms dynamically** .

Example problem:

```text
Different payment methods
Credit card
PayPal
UPI
```

### Example

```python
class CreditCard:

    def pay(self, amount):
        print("Paid", amount, "using credit card")


class UPI:

    def pay(self, amount):
        print("Paid", amount, "using UPI")
```

Context class:

```python
class Payment:

    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)
```

Usage:

```python
payment = Payment(CreditCard())

payment.pay(100)
```

Output:

```
Paid 100 using credit card
```

Strategy can change dynamically.

### Structure

```
Context
   |
Strategy Interface
   |
Multiple Strategies
```

Used in:

```text
machine learning algorithms
sorting strategies
payment systems
```

## 6. Adapter Pattern

Adapter converts  **one interface into another** .

Example problem:

```text
Old system → different API
New system → different API
```

Adapter bridges them.

Example:

```python
class OldSystem:

    def old_method(self):
        return "Old system data"
```

Adapter:

```python
class Adapter:

    def __init__(self, obj):
        self.obj = obj

    def new_method(self):
        return self.obj.old_method()
```

Usage:

```python
old = OldSystem()

adapter = Adapter(old)

print(adapter.new_method())
```

Output:

```
Old system data
```

Used in:

```text
legacy system integration
API wrappers
library compatibility
```

## Most Important Patterns in Python

In real Python projects these patterns are used the most:

```text
Singleton
Factory
Decorator
Observer
Strategy
```

These appear frequently in  **large frameworks** .

Example:

FastAPI:

```
Decorator pattern
Dependency injection
Factory pattern
```

Django:

```
Singleton
Observer
Factory
```

## Key Benefits of Design Patterns

Design patterns provide:

```text
reusable solutions
better architecture
cleaner code
easier maintenance
```

They help build  **large scalable systems** .
