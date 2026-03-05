## Python Iterators (Detailed Explanation)

Iterators are a  **core mechanism behind loops, generators, and many Python libraries** .
When you use a `for` loop in Python, you are  **actually using an iterator internally** .

To understand iterators clearly we need to understand  **four concepts step-by-step** :

1. Iterable
2. Iterator
3. `iter()` function
4. `next()` function

### 1. What is an Iterable?

An **iterable** is any object that can be  **looped over one element at a time** .

Common iterables:

```
list
tuple
string
dictionary
set
range
```

Example:

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

Output

```
10
20
30
```

Here `numbers` is an  **iterable** .

But `numbers` itself is  **not the iterator** .

### 2. What is an Iterator?

An **iterator** is an object that  **produces values one by one from an iterable** .

It remembers:

```
current position
next element
```

The iterator moves forward  **step by step** .

### 3. Converting Iterable → Iterator

To get an iterator from an iterable we use:

```python
iter()
```

Example:

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(it)
```

Now `it` is an  **iterator object** .

### 4. Getting Values Using `next()`

Iterators return elements using the function:

```
next()
```

Example:

```python
numbers = [10,20,30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

Output

```
10
20
30
```

The iterator  **moves forward each time** .

If we call `next()` again:

```
StopIteration
```

Python raises this error because  **there are no more values** .

### Visual Model

```
Iterable (list)
     ↓
iter()
     ↓
Iterator
     ↓
next() → value
next() → value
next() → value
```

### 5. How a `for` Loop Works Internally

A `for` loop actually works like this internally:

Example code:

```python
for num in numbers:
    print(num)
```

Internal process:

```
iterator = iter(numbers)

while True:
    value = next(iterator)
    print(value)
```

When `StopIteration` occurs, the loop stops.

### Example Demonstration

```python
numbers = [1,2,3]

iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        break
```

Output

```
1
2
3
```

This is exactly what a `for` loop does internally.

### 6. Iterator Protocol

Python defines a rule called the  **Iterator Protocol** .

For an object to be an iterator, it must implement two methods:

```
__iter__()
__next__()
```

### `__iter__()`

Returns the iterator object.

### `__next__()`

Returns the **next value** in the sequence.

If no value exists, it raises:

```
StopIteration
```

### 7. Creating a Custom Iterator (Class)

Example:

```python
class Counter:

    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration
```

Usage:

```python
c = Counter(5)

for num in c:
    print(num)
```

Output

```
1
2
3
4
5
```

### Internal Flow

```
Counter object
     ↓
__iter__()
     ↓
__next__()
     ↓
return value
```

### 8. Iterator State Tracking

An iterator remembers  **where it stopped last time** .

Example:

```python
numbers = [10,20,30]

it = iter(numbers)

print(next(it))
print(next(it))
```

Output

```
10
20
```

Now if we continue:

```python
print(next(it))
```

Output

```
30
```

The iterator remembers its position.

### 9. Iterator Exhaustion

Once an iterator is exhausted, it cannot restart.

Example:

```python
numbers = [1,2,3]

it = iter(numbers)

for n in it:
    print(n)

for n in it:
    print(n)
```

Second loop prints nothing because the iterator  **already reached the end** .

### 10. Iterator vs Iterable

| Feature            | Iterable | Iterator   |
| ------------------ | -------- | ---------- |
| Can loop over      | Yes      | Yes        |
| Stores data        | Yes      | Usually no |
| Has `__iter__()` | Yes      | Yes        |
| Has `__next__()` | No       | Yes        |

Example:

```
list → iterable
iterator → object that fetches values
```

### 11. Memory Advantage of Iterators

Iterators do  **not store all elements at once** .

They produce elements  **one by one** .

Example:

Large dataset:

```
10 million records
```

Using iterators allows processing  **without loading everything into memory** .

This is important for:

```
machine learning pipelines
big data processing
streaming systems
```

### 12. Built-in Iterators

Many Python objects already provide iterators.

Examples:

Dictionary iterator:

```python
data = {"a":1,"b":2}

it = iter(data)

print(next(it))
print(next(it))
```

Output

```
a
b
```

Range iterator:

```python
r = iter(range(3))

print(next(r))
print(next(r))
print(next(r))
```

Output

```
0
1
2
```

### 13. Real Example: File Iterator

Files are iterators.

Example:

```python
file = open("data.txt")

for line in file:
    print(line)
```

Python reads  **one line at a time** , not the whole file.

### Key Idea Summary

Iterator workflow:

```
Iterable
   ↓
iter()
   ↓
Iterator
   ↓
next()
   ↓
Next value
```

Iterator protocol:

```
__iter__()
__next__()
```

Used in:

```
for loops
generators
file reading
data pipelines
machine learning datasets
```

---

## Python Generators (Detailed Explanation)

Generators are a **special type of iterator** that allow you to  **generate values one at a time instead of storing them all in memory** .

They are extremely important in:

* **Machine learning pipelines**
* **Big data processing**
* **Streaming systems**
* **Large file processing**
* **Memory-efficient programs**

### Core Idea of Generators

Normal function:

```text
return → function ends
```

Generator function:

```text
yield → pause function
resume later from same point
```

So a generator  **produces values lazily (on demand)** .

### 1. Basic Generator Example

Generator function:

```python
def count(n):

    for i in range(n):
        yield i
```

Usage:

```python
g = count(5)

print(next(g))
print(next(g))
print(next(g))
```

Output

```
0
1
2
```

Here:

```
count() → generator function
g → generator object
```

### How It Works Internally

Execution flow:

```
count(5)
   |
   | yield 0
pause
   |
   | yield 1
pause
   |
   | yield 2
pause
```

The function  **remembers its previous state** .

### 2. Generator with `for` Loop

Generators work naturally with loops.

```python
def numbers():

    for i in range(3):
        yield i


for num in numbers():
    print(num)
```

Output

```
0
1
2
```

The loop automatically calls:

```
iter()
next()
```

### 3. Generator Execution Demonstration

Example:

```python
def demo():

    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3
```

Usage:

```python
g = demo()

print(next(g))
print(next(g))
print(next(g))
```

Output

```
Start
1
Middle
2
End
3
```

Execution pauses at each `yield`.

### Visual Flow

```
Generator Function
       |
       | yield value
       | pause
       | resume later
```

### 4. Generator vs Normal Function

Normal function:

```python
def square(nums):

    result = []

    for n in nums:
        result.append(n*n)

    return result
```

Generator version:

```python
def square(nums):

    for n in nums:
        yield n*n
```

Difference:

```
Normal function → returns entire list
Generator → produces values one by one
```

### Memory Example

List:

```python
nums = [i*i for i in range(1000000)]
```

This stores  **1 million numbers in memory** .

Generator:

```python
nums = (i*i for i in range(1000000))
```

This generates values  **only when needed** .

Memory comparison:

```
List → high memory
Generator → minimal memory
```

### 5. Generator Expression

Similar to list comprehension.

List comprehension:

```python
nums = [x*x for x in range(5)]
```

Generator expression:

```python
nums = (x*x for x in range(5))
```

Usage:

```python
for n in nums:
    print(n)
```

Output

```
0
1
4
9
16
```

### Structure

```
[ ] → list comprehension
( ) → generator expression
```

### 6. Infinite Generators

Generators can produce  **infinite sequences** .

Example:

```python
def infinite():

    num = 1

    while True:
        yield num
        num += 1
```

Usage:

```python
g = infinite()

print(next(g))
print(next(g))
print(next(g))
```

Output

```
1
2
3
```

This generator  **never ends** .

### 7. Real Use Case: Reading Large Files

Generators help process files  **line by line** .

Example:

```python
def read_file(filename):

    with open(filename) as file:

        for line in file:
            yield line
```

Usage:

```python
for line in read_file("data.txt"):
    print(line)
```

This prevents loading the  **entire file into memory** .

### 8. Generator Pipeline

Generators can be chained together.

Example:

```python
def numbers():

    for i in range(10):
        yield i


def squares(nums):

    for n in nums:
        yield n*n
```

Usage:

```python
result = squares(numbers())

for r in result:
    print(r)
```

Output

```
0
1
4
9
16
25
36
49
64
81
```

This is called a  **data pipeline** .

Used in:

```
machine learning
ETL pipelines
stream processing
```

### 9. Real ML Example: Batch Loader

Generators are widely used in ML training loops.

Example:

```python
def batch_loader(data, batch_size):

    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]
```

Usage:

```python
for batch in batch_loader(dataset, 32):
    train_model(batch)
```

This loads  **32 samples at a time instead of the entire dataset** .

### 10. Generator vs Iterator

| Feature          | Iterator  | Generator      |
| ---------------- | --------- | -------------- |
| Implementation   | Class     | Function       |
| Complexity       | More code | Very simple    |
| Memory           | Efficient | Very efficient |
| State management | Manual    | Automatic      |

Example iterator class:

```python
class Counter:

    def __init__(self,n):
        self.n=n
        self.i=0

    def __iter__(self):
        return self

    def __next__(self):

        if self.i<self.n:
            self.i+=1
            return self.i
        else:
            raise StopIteration
```

Generator version:

```python
def counter(n):

    for i in range(1,n+1):
        yield i
```

Generator is  **much simpler** .

### Generator Internals

Generators automatically implement:

```
__iter__()
__next__()
```

So they behave exactly like  **iterators** .

### Key Idea Summary

Generators:

```
produce values lazily
pause execution with yield
resume later
```

Structure:

```python
def generator():

    yield value
```

Usage:

```python
g = generator()

next(g)
```

### Real Systems Using Generators

Generators are heavily used in:

```
PyTorch DataLoader
TensorFlow pipelines
Pandas chunk processing
Web scraping
Log streaming
```

### Mental Model

```
Generator Function
       |
       | yield value
       | pause
       | resume
       |
       | yield next value
```

---



Iterable vs Iterator vs Generator (Deep Understanding)

These three terms are  **closely related but different** . Understanding them clearly is very important for  **Python interviews, ML pipelines, and large data processing** .

We will understand them step-by-step.

### 1. Iterable

An **iterable** is any object that can be  **looped over** .

An iterable **contains data** and can produce an iterator.

Examples of iterables:

```
list
tuple
string
dictionary
set
range
```

Example:

```python
numbers = [1,2,3,4]

for n in numbers:
    print(n)
```

Output

```
1
2
3
4
```

Here:

```
numbers → iterable
```

Important property:

An iterable must implement:

```
__iter__()
```

which returns an  **iterator** .

Example:

```python
numbers = [1,2,3]

print(numbers.__iter__())
```

or

```python
iter(numbers)
```

### Iterable Structure

```
Iterable
   |
   |-- contains data
   |
   |-- produces iterator
```

### 2. Iterator

An **iterator** is an object that  **produces elements one at a time** .

An iterator:

```
remembers current position
moves forward
returns next element
```

Iterators implement two methods:

```
__iter__()
__next__()
```

Example:

```python
numbers = [10,20,30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

Output

```
10
20
30
```

If we call `next()` again:

```
StopIteration
```

### Iterator Structure

```
Iterator
   |
   |-- __iter__()
   |
   |-- __next__()
```

Iterator behavior:

```
value1
value2
value3
StopIteration
```

### Example Flow

```
Iterable → list
      ↓
iter(list)
      ↓
Iterator
      ↓
next()
```

### 3. Generator

A **generator** is a  **simpler way to create iterators using `yield`** .

Generators automatically implement:

```
__iter__()
__next__()
```

Example generator:

```python
def count(n):

    for i in range(n):
        yield i
```

Usage:

```python
g = count(3)

print(next(g))
print(next(g))
print(next(g))
```

Output

```
0
1
2
```

Generators **pause execution at `yield`** and resume later.

### Generator Execution

```
yield value
pause function
resume later
```

Example:

```python
def demo():

    print("Start")
    yield 1

    print("Middle")
    yield 2
```

Usage:

```python
g = demo()

print(next(g))
print(next(g))
```

Output

```
Start
1
Middle
2
```

### Memory Behavior

Generators do  **lazy evaluation** .

Example list:

```python
nums = [x*x for x in range(1000000)]
```

This stores  **1 million values in memory** .

Generator:

```python
nums = (x*x for x in range(1000000))
```

This generates values  **one at a time** .

### Comparison Table

| Feature            | Iterable         | Iterator     | Generator               |
| ------------------ | ---------------- | ------------ | ----------------------- |
| Stores data        | Yes              | No           | No                      |
| Produces values    | No               | Yes          | Yes                     |
| Memory usage       | High             | Low          | Very low                |
| Implementation     | Built-in objects | Custom class | Function with `yield` |
| Has `__iter__()` | Yes              | Yes          | Yes                     |
| Has `__next__()` | No               | Yes          | Yes                     |

### Visual Model

```
Iterable
   |
   |-- produces
   ↓
Iterator
   |
   |-- next()
   ↓
values
```

Generator model:

```
Generator Function
       |
       |-- yield value
       |-- pause
       |-- resume
```

### Real World Example

Suppose we process  **10 million records** .

List approach:

```
load everything into memory
```

Generator approach:

```
load one record
process it
discard it
load next
```

This is why generators are used in:

```
machine learning
big data
streaming pipelines
```

Example ML batch loader:

```python
def batch_loader(data, size):

    for i in range(0, len(data), size):
        yield data[i:i+size]
```

Usage:

```python
for batch in batch_loader(dataset, 32):
    train(batch)
```

This loads  **32 samples at a time instead of entire dataset** .

### Internal Relationship

```
Iterable
   |
   |-- iter()
   ↓
Iterator
   |
   |-- next()
   ↓
value
```

Generator is simply:

```
Iterator created using yield
```

### One Important Interview Question

Why is a generator an iterator?

Because Python automatically provides:

```
__iter__()
__next__()
```

for generator functions.

### Key Understanding

```
Iterable → produces iterator
Iterator → produces values
Generator → easiest way to build iterator
```

### Final Mental Model

```
Iterable (list, tuple, etc.)
        |
        ↓
Iterator (iter())
        |
        ↓
next()
        |
        ↓
Value
```

Generator:

```
Iterator created using yield
```
