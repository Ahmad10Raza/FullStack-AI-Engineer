## Python Decorators (Complete Guide)

Decorators are one of the  **most powerful and widely used features in Python** . They are heavily used in:

* **Flask / FastAPI**
* **Django**
* **Machine Learning libraries**
* **Logging systems**
* **Authentication systems**

Before understanding decorators, we must first understand  **functions as objects** .

### 1. Functions Are First-Class Objects in Python

In Python, functions can:

* Be assigned to variables
* Be passed as arguments
* Be returned from other functions

Example:

```python
def greet():
    print("Hello")

say_hello = greet

say_hello()
```

Output

```
Hello
```

Here the function `greet` is assigned to another variable.

### 2. Functions Inside Functions

Python allows defining a function  **inside another function** .

Example:

```python
def outer():

    def inner():
        print("Inner function")

    inner()

outer()
```

Output

```
Inner function
```

This concept is important for decorators.

### 3. Functions Returning Functions

A function can  **return another function** .

Example:

```python
def outer():

    def inner():
        print("Hello from inner")

    return inner


func = outer()

func()
```

Output

```
Hello from inner
```

Here `outer()` returns `inner`.

This mechanism is the  **foundation of decorators** .

### 4. What is a Decorator?

A  **decorator is a function that modifies or extends another function without changing its code** .

Simple idea

```
Original Function
       ↓
Decorator
       ↓
Enhanced Function
```

Syntax:

```python
@decorator_name
def function():
```

### 5. Example: Simple Decorator

Decorator function:

```python
def my_decorator(func):

    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")

    return wrapper
```

Function to decorate:

```python
def say_hello():
    print("Hello")
```

Applying decorator manually:

```python
say_hello = my_decorator(say_hello)

say_hello()
```

Output

```
Before function runs
Hello
After function runs
```

The decorator  **adds extra behavior** .

### 6. Decorator Syntax (`@`)

Instead of manually wrapping functions, Python provides a cleaner syntax.

Example:

```python
def my_decorator(func):

    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")

    return wrapper


@my_decorator
def greet():
    print("Hello")


greet()
```

Output

```
Before function runs
Hello
After function runs
```

Python internally converts this:

```
@my_decorator
def greet():
```

to

```
greet = my_decorator(greet)
```

### 7. Decorator With Arguments

Functions often have parameters, so decorators must handle them.

Example:

```python
def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Before execution")
        func(*args, **kwargs)
        print("After execution")

    return wrapper


@my_decorator
def add(a, b):
    print(a + b)


add(5, 3)
```

Output

```
Before execution
8
After execution
```

`*args` and `**kwargs` allow decorators to work with  **any function** .

### 8. Practical Example: Logging Decorator

Example logging function calls.

```python
def logger(func):

    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} started")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result

    return wrapper


@logger
def multiply(a, b):
    return a * b


print(multiply(4, 5))
```

Output

```
Function multiply started
Function multiply finished
20
```

This pattern is used in  **production systems** .

### 9. Multiple Decorators

You can stack decorators.

Example:

```python
def decor1(func):

    def wrapper():
        print("Decorator 1")
        func()

    return wrapper


def decor2(func):

    def wrapper():
        print("Decorator 2")
        func()

    return wrapper


@decor1
@decor2
def greet():
    print("Hello")


greet()
```

Execution order:

```
decor1(decor2(greet))
```

Output

```
Decorator 1
Decorator 2
Hello
```

### 10. Decorators for Authentication Example

Example used in web frameworks.

```python
def require_login(func):

    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            print("Access denied")

    return wrapper


@require_login
def dashboard(user):
    print("Welcome to dashboard")


dashboard("admin")
dashboard("guest")
```

Output

```
Welcome to dashboard
Access denied
```

### 11. Class Decorators

Decorators can also modify classes.

Example:

```python
def add_method(cls):

    def greet(self):
        print("Hello from decorator")

    cls.greet = greet
    return cls


@add_method
class Person:
    pass


p = Person()
p.greet()
```

Output

```
Hello from decorator
```

### 12. Built-in Python Decorators

Python already uses decorators in many places.

Examples

`@staticmethod`

```
class Example:

    @staticmethod
    def hello():
        print("Hello")
```

`@classmethod`

```
class Example:

    @classmethod
    def show(cls):
        print("Class method")
```

`@property`

```
class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

Usage:

```
p = Person(25)
print(p.age)
```

### Visual Flow of Decorator

```
Function Call
      ↓
Decorator Wrapper
      ↓
Original Function
```

### Key Points

Decorators:

* Modify functions without changing original code
* Use **higher-order functions**
* Are widely used in **web frameworks and ML libraries**

Core structure:

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        # extra logic
        return func(*args, **kwargs)

    return wrapper
```

Usage:

```python
@decorator
def function():
```

---

## Advanced Python Decorators

Now we go deeper into decorators that are **commonly used in production systems** like  **FastAPI, Flask, Django, ML pipelines, logging systems, and caching systems** .

We will cover:

1. Decorators with Parameters
2. `functools.wraps`
3. Stateful Decorators
4. Class-Based Decorators
5. Real-world decorators (Caching, Timing, Retry)

### 1. Decorators with Parameters

Sometimes we want a decorator that  **accepts arguments** .

Example idea:

```text
@repeat(3)
def greet():
```

This means the decorator itself must  **receive parameters** .

Structure:

```text
Decorator Function
      ↓
Decorator Wrapper
      ↓
Actual Function
```

Example:

```python
def repeat(n):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello")


greet()
```

Output

```
Hello
Hello
Hello
```

Execution flow

```
greet = repeat(3)(greet)
```

So the decorator is  **called first with parameter 3** .

### 2. `functools.wraps`

When we use decorators, the  **original function metadata is lost** .

Example problem:

```python
def decorator(func):

    def wrapper():
        func()

    return wrapper


@decorator
def greet():
    print("Hello")


print(greet.__name__)
```

Output

```
wrapper
```

The original function name  **is replaced by wrapper** .

Solution: `functools.wraps`.

Example:

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper():
        func()

    return wrapper


@decorator
def greet():
    print("Hello")


print(greet.__name__)
```

Output

```
greet
```

Now the original function information is preserved.

### 3. Stateful Decorators

A  **stateful decorator remembers information across multiple calls** .

Example: counting how many times a function runs.

```python
def call_counter(func):

    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print("Function called", count, "times")
        return func(*args, **kwargs)

    return wrapper


@call_counter
def greet():
    print("Hello")


greet()
greet()
greet()
```

Output

```
Function called 1 times
Hello
Function called 2 times
Hello
Function called 3 times
Hello
```

The decorator  **stores state using closure variables** .

### 4. Class-Based Decorators

Decorators can also be implemented using  **classes** .

This uses the special method:

```python
__call__()
```

Example:

```python
class Logger:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Function started")
        result = self.func(*args, **kwargs)
        print("Function finished")
        return result


@Logger
def add(a, b):
    return a + b


print(add(3, 4))
```

Output

```
Function started
Function finished
7
```

Python converts this internally to:

```
add = Logger(add)
```

### 5. Timing Decorator (Performance Monitoring)

Used in  **ML training and data pipelines** .

```python
import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution time:", end - start)

        return result

    return wrapper


@timer
def slow_function():
    time.sleep(2)
    print("Task finished")


slow_function()
```

Output

```
Task finished
Execution time: 2.00
```

### 6. Caching Decorator

Used to  **avoid recomputation** .

Example: Fibonacci calculation.

```python
def cache(func):

    memory = {}

    def wrapper(n):

        if n in memory:
            return memory[n]

        result = func(n)
        memory[n] = result
        return result

    return wrapper


@cache
def fib(n):

    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)


print(fib(10))
```

Caching drastically  **improves performance** .

### 7. Retry Decorator (Production Use)

Used in APIs and network systems.

Example: retry if a function fails.

```python
import time

def retry(attempts):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for i in range(attempts):

                try:
                    return func(*args, **kwargs)

                except Exception:
                    print("Retrying...")
                    time.sleep(1)

        return wrapper

    return decorator


@retry(3)
def unstable():

    raise ValueError("Error")


unstable()
```

### 8. Real Framework Example

Example similar to  **Flask routing** .

```python
def route(path):

    def decorator(func):
        print("Registering route:", path)
        return func

    return decorator


@route("/home")
def home():
    print("Home page")
```

Output

```
Registering route: /home
```

Frameworks like **Flask and FastAPI** heavily use decorators.

Example:

```
@app.get("/users")
def get_users():
```

### Mental Model of Decorators

```
Function Call
     ↓
Decorator Wrapper
     ↓
Original Function
```

Decorators allow us to  **add behavior without modifying existing code** .

### Key Advanced Concepts

Decorators can:

* Accept arguments
* Maintain internal state
* Be implemented with classes
* Modify metadata using `functools.wraps`
* Improve performance using caching
* Implement logging, authentication, retry logic

### Decorators in Real Systems

Decorators are used heavily in:

* **FastAPI / Flask routing**
* **Authentication systems**
* **Caching**
* **Monitoring**
* **ML experiment tracking**
* **Database transactions**

Example:

```
@login_required
@cache
@timer
def expensive_operation():
```

Each decorator  **adds one layer of functionality** .

If you want, I can also explain **one of the most confusing but powerful topics in Python** next:

**Closures in Python**

Closures are the  **hidden mechanism that makes decorators work internally** , and understanding them makes decorators  **100× easier to master** .

---

## Closures in Python

Closures are the  **core mechanism that makes decorators work** .
To understand closures, we need to understand  **three concepts together** :

1. Nested Functions
2. Function Returning Functions
3. Remembering variables from outer scope

A **closure** happens when a  **nested function remembers variables from its enclosing function even after the outer function has finished executing** .

Simple idea:

```text
Outer Function
      ↓
Creates Variable
      ↓
Inner Function Uses It
      ↓
Outer Function Ends
      ↓
Inner Function STILL remembers the variable
```

### 1. Basic Nested Function

```python
def outer():

    message = "Hello"

    def inner():
        print(message)

    inner()

outer()
```

Output

```
Hello
```

Here `inner()` can access the variable `message` from `outer()`.

This is called  **lexical scoping** .

### 2. Function Returning Function

Now let's return the inner function.

```python
def outer():

    message = "Hello"

    def inner():
        print(message)

    return inner


func = outer()

func()
```

Output

```
Hello
```

Important thing:

Even though `outer()` has finished executing, the inner function  **still remembers `message`** .

This is a  **closure** .

### Visual Representation

```
outer() runs
   |
   |-- message = "Hello"
   |
   |-- returns inner()

outer() finished

inner() still remembers message
```

The inner function  **closes over the outer variable** .

Hence the name  **closure** .

### 3. Closure Example with Parameters

```python
def multiplier(x):

    def multiply(y):
        return x * y

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))
```

Output

```
10
15
```

Explanation

```
double remembers x = 2
triple remembers x = 3
```

Structure

```
multiplier(2)
      ↓
 returns multiply(y)
      ↓
multiply remembers x = 2
```

### 4. Inspecting Closure Variables

Python stores closure variables inside:

```python
function.__closure__
```

Example:

```python
def outer():

    x = 10

    def inner():
        print(x)

    return inner


func = outer()

print(func.__closure__)
```

Output shows  **stored reference to x** .

### 5. Practical Example (Power Function)

```python
def power(n):

    def calculate(x):
        return x ** n

    return calculate


square = power(2)
cube = power(3)

print(square(5))
print(cube(5))
```

Output

```
25
125
```

Each returned function  **remembers its own `n` value** .

### 6. Closure with Mutable State

Closures can also  **store changing values** .

Example:

```python
def counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()

print(c())
print(c())
print(c())
```

Output

```
1
2
3
```

Important keyword:

```python
nonlocal
```

`nonlocal` allows modifying a variable from the  **enclosing scope** .

### 7. Closures Behind Decorators

Decorators work because of closures.

Example decorator:

```python
def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper
```

Here:

```
wrapper remembers func
```

Even after `decorator()` finishes, `wrapper()` still  **has access to `func`** .

This is  **closure behavior** .

### Decorator Execution Flow

```
Original Function
        ↓
Passed to Decorator
        ↓
Decorator returns wrapper
        ↓
Wrapper remembers original function
```

Without closures,  **decorators would not work** .

### 8. Real Example: Configurable Logger

```python
def logger(prefix):

    def decorator(func):

        def wrapper(*args, **kwargs):
            print(prefix, "Function called")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logger("DEBUG")
def add(a, b):
    return a + b


print(add(3,4))
```

Output

```
DEBUG Function called
7
```

Here closure stores:

```
prefix
func
```

### Closure vs Class

Closures are sometimes used instead of classes.

Closure version:

```python
def counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

Class version:

```python
class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
```

Both behave similarly.

Closures are often  **lighter than classes** .

### Key Characteristics of Closures

A closure requires:

1. A nested function
2. The inner function referencing outer variables
3. The outer function returning the inner function

Structure

```python
def outer():

    variable = value

    def inner():
        use(variable)

    return inner
```

### Why Closures Matter

Closures are heavily used in:

* Decorators
* Functional programming
* Callback systems
* Data hiding
* State persistence without classes

Libraries using closures internally include:

* Flask
* FastAPI
* TensorFlow
* PyTorch
* Pandas

### Mental Model

```
Function + Remembered Variables
           ↓
        Closure
```

The function  **carries its environment with it** .

### If you want, the next step (very powerful for Python mastery) is:

**Python Context Managers and the `with` statement**

This includes:

```
__enter__()
__exit__()
contextlib
custom resource management
```

This concept is used everywhere in Python like:

```
with open(file)
with torch.no_grad()
with database_transaction()
```

---

## Python Context Managers and the `with` Statement

A **Context Manager** is a Python construct that  **manages resources automatically** , such as files, database connections, locks, or network connections.

It ensures that:

* **Setup code runs before a block**
* **Cleanup code runs after the block**

even if an  **error occurs** .

The context manager is typically used with the  **`with` statement** .

Basic idea:

```
Setup Resource
      ↓
Run Code Block
      ↓
Cleanup Resource
```

### 1. Basic Example: File Handling

Without context manager:

```python
file = open("data.txt", "r")

data = file.read()

file.close()
```

Problem:

If an error happens before `file.close()`, the file  **remains open** .

Using `with`:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

Python automatically does:

```
open file
run block
close file
```

### Execution Flow of `with`

```
Enter Context
      ↓
Execute Code
      ↓
Exit Context (cleanup)
```

### 2. How Context Managers Work Internally

A context manager is implemented using two special methods:

```
__enter__()
__exit__()
```

Structure:

```python
class ContextManager:

    def __enter__(self):
        # setup
        return resource

    def __exit__(self, exc_type, exc_value, traceback):
        # cleanup
```

### 3. Example: Custom Context Manager

```python
class FileManager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening file")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file")
        self.file.close()
```

Usage:

```python
with FileManager("data.txt", "w") as f:
    f.write("Hello")
```

Output

```
Opening file
Closing file
```

Execution internally becomes:

```
manager = FileManager("data.txt","w")
f = manager.__enter__()

run block

manager.__exit__()
```

### 4. Exception Handling in Context Managers

`__exit__` receives information about errors.

Parameters:

```
exc_type
exc_value
traceback
```

Example:

```python
class Demo:

    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")
```

Usage:

```python
with Demo():
    print("Inside block")
```

Output

```
Start
Inside block
End
```

Even if an error occurs, `__exit__` still runs.

### 5. Suppressing Exceptions

If `__exit__` returns `True`, the exception is  **suppressed** .

Example:

```python
class Safe:

    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exception handled")
        return True
```

Usage:

```python
with Safe():
    x = 1 / 0
```

Output

```
Start
Exception handled
```

The program  **does not crash** .

### 6. Context Managers Using `contextlib`

Python provides a simpler way using  **`contextlib`** .

Decorator:

```
@contextmanager
```

Example:

```python
from contextlib import contextmanager

@contextmanager
def my_context():

    print("Entering")

    yield

    print("Exiting")
```

Usage:

```python
with my_context():
    print("Inside block")
```

Output

```
Entering
Inside block
Exiting
```

Here:

```
before yield → __enter__
after yield → __exit__
```

### 7. Real Example: Timing Context Manager

Used in ML pipelines.

```python
import time
from contextlib import contextmanager

@contextmanager
def timer():

    start = time.time()

    yield

    end = time.time()

    print("Execution time:", end - start)
```

Usage:

```python
with timer():
    time.sleep(2)
```

Output

```
Execution time: 2.00
```

### 8. Real Libraries Using Context Managers

Many Python libraries rely heavily on context managers.

Examples:

File handling

```
with open("file.txt")
```

Thread locks

```
with lock:
```

PyTorch

```
with torch.no_grad():
```

Database transactions

```
with transaction():
```

TensorFlow

```
with tf.GradientTape():
```

### 9. Multiple Context Managers

You can use multiple context managers in one statement.

```python
with open("file1.txt") as f1, open("file2.txt") as f2:
    data1 = f1.read()
    data2 = f2.read()
```

Python manages both resources automatically.

### Visual Representation

```
with ContextManager():
       |
       |-- __enter__()
       |
       |-- run block
       |
       |-- __exit__()
```

### Key Points

Context managers handle  **resource management automatically** .

Implemented using:

```
__enter__()
__exit__()
```

or

```
contextlib.contextmanager
```

Benefits:

* Automatic cleanup
* Exception safety
* Cleaner code

Common use cases:

* File handling
* Database connections
* Locks
* ML model inference
* Resource monitoring
