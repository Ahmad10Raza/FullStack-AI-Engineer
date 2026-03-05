### 1. Python Classes (Introduction)

Object-Oriented Programming (OOP) in Python is a programming paradigm where we structure programs using **objects and classes** instead of only functions and variables.

Before understanding advanced OOP concepts like  **inheritance, polymorphism, and encapsulation** , we must understand  **what a class is** .

#### What is a Class?

A **class** is a **blueprint or template** used to create objects.

It defines:

* **Attributes (variables)** → properties of the object
* **Methods (functions)** → behaviors of the object

Think of it like this:

Class → Blueprint of a house
Object → Actual house built from that blueprint

Example in real life:

Class: **Car**
Attributes: color, brand, speed
Methods: start(), stop(), accelerate()

#### Syntax of a Python Class

```python
class ClassName:
    # attributes
    # methods
```

Example:

```python
class Car:
    brand = "Toyota"
    color = "Red"

    def start(self):
        print("Car started")
```

Here:

* `Car` → Class
* `brand`, `color` → Class attributes
* `start()` → Method (function inside class)

#### Creating an Object from a Class

An **object** is an instance of a class.

```python
class Car:
    brand = "Toyota"
    color = "Red"

    def start(self):
        print("Car started")

# creating object
my_car = Car()

print(my_car.brand)
print(my_car.color)

my_car.start()
```

Output

```
Toyota
Red
Car started
```

Explanation:

* `my_car = Car()` creates an **object**
* `my_car.brand` accesses attribute
* `my_car.start()` calls method

#### Another Simple Example

```python
class Student:
    name = "Ahmad"
    age = 22

student1 = Student()

print(student1.name)
print(student1.age)
```

Output

```
Ahmad
22
```

Here:

* `Student` is the **class**
* `student1` is the **object**
* `name` and `age` are **attributes**

#### Key Points

Class → blueprint
Object → instance of a class
Attributes → variables inside class
Methods → functions inside class

Example structure:

```
Class
 ├── Attributes
 └── Methods
```

#### Real World Analogy

Class → **Student**

Attributes

* name
* age
* roll_number

Methods

* study()
* attend_class()
* give_exam()

Objects

```
student1
student2
student3
```

Each object has **its own data** but follows the  **same class structure** .

---

### 2. Python OOP (Object-Oriented Programming)

Object-Oriented Programming (OOP) is a programming paradigm where programs are designed using **objects and classes** instead of only functions and procedures.

In Python, OOP helps to:

* Organize large programs
* Reuse code
* Make code easier to maintain
* Model real-world entities

Python is a  **multi-paradigm language** , but OOP is widely used in large applications such as  **web frameworks, machine learning systems, automation tools, and APIs** .

You will often see OOP used in libraries like  **TensorFlow, PyTorch, and Flask** , which is relevant to your AI/ML projects.

### Core Concepts of OOP

There are  **4 main pillars of OOP** .

1. **Encapsulation**
2. **Inheritance**
3. **Polymorphism**
4. **Abstraction** (Python supports it but it's often discussed separately)

We will study some of these later in detail.

### Basic Structure of OOP

In OOP we use:

* **Class** → blueprint
* **Object** → instance of class
* **Attributes** → variables
* **Methods** → functions inside class

Example:

```python
class Student:

    def study(self):
        print("Student is studying")

student1 = Student()
student1.study()
```

Output

```
Student is studying
```

Here:

`Student` → Class
`student1` → Object
`study()` → Method

### Example 1: Real World Example

Let's model a  **Bank Account** .

```python
class BankAccount:

    def deposit(self):
        print("Money Deposited")

    def withdraw(self):
        print("Money Withdrawn")

account1 = BankAccount()

account1.deposit()
account1.withdraw()
```

Output

```
Money Deposited
Money Withdrawn
```

Here the  **BankAccount object performs operations like a real account** .

### Example 2: Multiple Objects

```python
class Dog:

    def bark(self):
        print("Dog is barking")

dog1 = Dog()
dog2 = Dog()

dog1.bark()
dog2.bark()
```

Output

```
Dog is barking
Dog is barking
```

Both `dog1` and `dog2` are  **different objects but from the same class** .

### Why OOP is Important

Without OOP, large programs become difficult to manage.

Example without OOP:

```
deposit_money()
withdraw_money()
check_balance()
transfer_money()
```

These functions become messy when the system grows.

With OOP:

```
BankAccount
   ├── deposit()
   ├── withdraw()
   └── check_balance()
```

Everything is  **grouped logically** .

### Real Example from ML / AI

When you use a model in  **scikit-learn** , it is actually OOP.

Example:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X, y)
model.predict(X_test)
```

Here:

`LinearRegression` → Class
`model` → Object
`fit()` and `predict()` → Methods

So when you use ML libraries, you are  **already using OOP** .

### Key Points

OOP organizes programs using  **classes and objects** .

Important components:

Class → blueprint
Object → instance
Attribute → data
Method → behavior

OOP principles:

Encapsulation
Inheritance
Polymorphism
Abstraction

---

### 3. Python Classes / Objects

In Python OOP, the **two most fundamental elements** are:

**Class** → Blueprint / Template
**Object** → Instance created from the class

A class defines the  **structure and behavior** , while objects are the  **actual entities that use that structure** .

### Relationship Between Class and Object

Think of it like this:

Class → **Car Blueprint**

Objects created from it:

```
Car Class
   |
   |---- car1
   |---- car2
   |---- car3
```

All objects share the same structure but can contain  **different data** .

### Creating a Class

Basic syntax:

```python
class ClassName:
    pass
```

Example:

```python
class Student:
    pass
```

Here `Student` is a class but currently  **empty** .

### Creating an Object

An object is created by calling the class like a function.

```python
class Student:
    pass

student1 = Student()
```

`student1` is now an **object (instance)** of the class `Student`.

### Example: Class with Attributes

```python
class Student:
    name = "Ahmad"
    age = 22

student1 = Student()

print(student1.name)
print(student1.age)
```

Output

```
Ahmad
22
```

Explanation

`name` and `age` → attributes of the class
`student1` → object accessing those attributes

### Multiple Objects Example

```python
class Car:
    brand = "Toyota"
    color = "Red"

car1 = Car()
car2 = Car()

print(car1.brand)
print(car2.color)
```

Output

```
Toyota
Red
```

Both objects share the  **same class attributes** .

### Modifying Object Attributes

Objects can have  **their own values** .

```python
class Student:
    name = "Unknown"

student1 = Student()
student2 = Student()

student1.name = "Ahmad"
student2.name = "Ali"

print(student1.name)
print(student2.name)
```

Output

```
Ahmad
Ali
```

Now each object stores  **different data** .

### Class with Methods

Classes can also contain  **functions called methods** .

```python
class Person:

    def greet(self):
        print("Hello")

person1 = Person()
person1.greet()
```

Output

```
Hello
```

Explanation

`greet()` → method of the class
`person1.greet()` → object calling the method

### Accessing Attributes and Methods

Objects access class components using  **dot notation** .

```
object.attribute
object.method()
```

Example:

```python
student1.name
student1.study()
```

### Internal Representation

When Python creates an object:

```
Student Class
   |
   |---- student1 → memory location
   |---- student2 → memory location
```

Each object has its  **own memory storage** .

### Real Example

```python
class Laptop:

    brand = "Dell"

    def start(self):
        print("Laptop Starting")

lap1 = Laptop()
lap2 = Laptop()

lap1.start()
```

Output

```
Laptop Starting
```

Here:

Class → `Laptop`
Objects → `lap1`, `lap2`
Attribute → `brand`
Method → `start()`

### Key Points

Class → Blueprint
Object → Instance of class
Attributes → Data inside class
Methods → Functions inside class

Object interaction:

```
object.attribute
object.method()
```

---

### 4. Python `__init__` Method

The `__init__` method is a **special method (constructor)** in Python that is automatically executed  **when an object of a class is created** .

It is mainly used to  **initialize object attributes** .

So whenever you create an object like:

```python
obj = ClassName()
```

Python automatically calls:

```python
ClassName.__init__()
```

### Why `__init__` is Needed

Without `__init__`, every object would have the  **same default values** .

Example without `__init__`:

```python
class Student:
    name = "Unknown"
    age = 0

s1 = Student()
s2 = Student()

print(s1.name)
print(s2.name)
```

Output

```
Unknown
Unknown
```

Both objects have the  **same value** .

Using `__init__`, we can assign  **different values to each object** .

### Syntax of `__init__`

```python
class ClassName:

    def __init__(self, parameters):
        self.variable = parameters
```

`__init__` always runs  **first when the object is created** .

### Example 1: Basic `__init__`

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Ahmad", 22)
student2 = Student("Ali", 21)

print(student1.name)
print(student2.age)
```

Output

```
Ahmad
21
```

Explanation

When this runs:

```python
student1 = Student("Ahmad", 22)
```

Python internally does:

```
__init__(student1, "Ahmad", 22)
```

And assigns:

```
student1.name = "Ahmad"
student1.age = 22
```

### Visual Representation

```
Student Class
    |
    |--- student1
    |       name = Ahmad
    |       age = 22
    |
    |--- student2
            name = Ali
            age = 21
```

Each object stores  **its own data** .

### Example 2: Class with Method and `__init__`

```python
class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display(self):
        print(self.brand, self.color)

car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

car1.display()
car2.display()
```

Output

```
Toyota Red
BMW Black
```

Explanation

`__init__` initializes the attributes and `display()` prints them.

### Example 3: Default Values in `__init__`

You can also give  **default values** .

```python
class Employee:

    def __init__(self, name, salary=50000):
        self.name = name
        self.salary = salary

emp1 = Employee("Ahmad")
emp2 = Employee("Ali", 80000)

print(emp1.salary)
print(emp2.salary)
```

Output

```
50000
80000
```

### Important Notes

1. `__init__` is **not the object itself**
   It only  **initializes attributes** .
2. It is  **automatically executed** .
3. The first parameter must always be  **`self`** .

### Internal Flow

When you write:

```python
student1 = Student("Ahmad", 22)
```

Python internally performs:

```
1. Create empty object
2. Call __init__()
3. Assign values to attributes
```

### Key Points

`__init__` is called a  **constructor** .

Purpose:

* Initialize object attributes
* Assign values during object creation

Structure

```python
class Example:

    def __init__(self):
        pass
```

Example creation

```python
obj = Example()
```

---

### 5. Python `self` Parameter

In Python OOP,  **`self` refers to the current object of the class** .

It is used to  **access variables and methods of the same object inside the class** .

When a method is called using an object, Python  **automatically passes the object as the first argument** , which we conventionally name `self`.

### Why `self` is Needed

`self` allows each object to  **access and store its own data** .

Without `self`, Python would not know  **which object's data is being accessed** .

### Basic Syntax

```python
class ClassName:

    def method(self):
        pass
```

Here:

`self` → represents the **current object**

### Example 1: Using `self` to Access Attributes

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

s1 = Student("Ahmad")
s2 = Student("Ali")

s1.display()
s2.display()
```

Output

```
Ahmad
Ali
```

Explanation

When this runs:

```python
s1.display()
```

Python internally does:

```
Student.display(s1)
```

So `self` becomes `s1`.

When:

```
s2.display()
```

Python internally does:

```
Student.display(s2)
```

So `self` becomes `s2`.

### Visual Representation

```
Student Class
      |
      |---- s1
      |       name = Ahmad
      |
      |---- s2
              name = Ali
```

Inside the method:

```
self.name
```

Python understands:

```
s1.name
s2.name
```

depending on which object calls the method.

### Example 2: Multiple Attributes Using `self`

```python
class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print(self.brand, self.color)

car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

car1.show()
car2.show()
```

Output

```
Toyota Red
BMW Black
```

Here `self.brand` and `self.color` store  **data specific to each object** .

### Example 3: Using `self` to Call Another Method

`self` can also call  **another method of the same class** .

```python
class Person:

    def greet(self):
        print("Hello")

    def message(self):
        self.greet()
        print("Welcome")

p = Person()
p.message()
```

Output

```
Hello
Welcome
```

Here:

```
self.greet()
```

means the object calls its own method.

### Important Rules

1. `self` must be the  **first parameter in every instance method** .

Example

```python
def method(self):
```

2. `self` is  **not a keyword** .
   It is just a  **convention** , but almost every Python developer uses it.

Technically this works:

```python
class Test:

    def show(obj):
        print("Hello")
```

But it is  **not recommended** .

### Internal Working

When we call:

```python
car1.show()
```

Python internally converts it to:

```
Car.show(car1)
```

So the object automatically becomes `self`.

### Common Beginner Mistake

Incorrect:

```python
class Student:

    def show():
        print("Hello")
```

Error occurs because  **`self` is missing** .

Correct:

```python
class Student:

    def show(self):
        print("Hello")
```

### Key Idea

`self` = **current object**

It allows:

* Accessing object attributes
* Calling class methods
* Storing object-specific data

Example structure

```
class Example:
    def method(self):
        print(self)
```

Object call

```
obj.method()
```

---

### 6. Python Class Properties

In Python,  **class properties are variables that store data inside a class** .
They define the  **state or characteristics of an object** .

Properties are also called  **attributes** .

There are two main types of properties in Python OOP:

1. **Class Properties (Class Variables)**
2. **Instance Properties (Instance Variables)**

Understanding the difference between these two is very important.

### 1. Class Properties (Class Variables)

Class properties are  **shared by all objects of the class** .

They are defined  **directly inside the class but outside any method** .

#### Example

```python
class Car:
    wheels = 4

car1 = Car()
car2 = Car()

print(car1.wheels)
print(car2.wheels)
```

Output

```
4
4
```

Explanation

`wheels` is a  **class property** .
Every object created from `Car` will share the same value.

Internal representation

```
Car Class
   |
   |---- wheels = 4
   |
   |---- car1
   |---- car2
```

Both objects access the  **same property** .

### Modifying a Class Property

```python
class Car:
    wheels = 4

car1 = Car()
car2 = Car()

Car.wheels = 6

print(car1.wheels)
print(car2.wheels)
```

Output

```
6
6
```

Changing the class property affects  **all objects** .

### 2. Instance Properties (Instance Variables)

Instance properties belong to  **individual objects** .

They are usually defined using  **`self` inside the `__init__` method** .

#### Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ahmad", 22)
s2 = Student("Ali", 21)

print(s1.name)
print(s2.name)
```

Output

```
Ahmad
Ali
```

Internal structure

```
Student Class
    |
    |---- s1
    |       name = Ahmad
    |       age = 22
    |
    |---- s2
            name = Ali
            age = 21
```

Each object stores  **its own values** .

### Example: Both Class and Instance Properties

```python
class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Ahmad", 70000)
e2 = Employee("Ali", 80000)

print(e1.company)
print(e1.name)
```

Output

```
Google
Ahmad
```

Explanation

`company` → class property
`name`, `salary` → instance properties

### Accessing Properties

Properties can be accessed using  **dot notation** .

```
object.property
```

Example

```python
print(e1.salary)
print(e2.company)
```

### Modifying Instance Properties

```python
class Person:

    def __init__(self, name):
        self.name = name

p1 = Person("Ahmad")
p2 = Person("Ali")

p1.name = "Rahul"

print(p1.name)
print(p2.name)
```

Output

```
Rahul
Ali
```

Only `p1` changed because instance properties are  **object-specific** .

### Key Difference

| Feature | Class Property  | Instance Property        |
| ------- | --------------- | ------------------------ |
| Defined | Inside class    | Inside `__init__`      |
| Shared  | Yes             | No                       |
| Access  | Class or object | Object only              |
| Memory  | One copy        | Separate copy per object |

Example structure

```
Class
   |
   |--- Class Property
   |
   |--- Object1 → Instance Properties
   |--- Object2 → Instance Properties
```

### Key Points

Class property

* Shared across objects
* Defined outside methods

Instance property

* Unique for each object
* Defined using `self`

Example pattern

```python
class Example:

    class_property = value

    def __init__(self, data):
        self.instance_property = data
```

---

### 7. Python Class Methods

In Python, **methods are functions defined inside a class** that describe the  **behavior of objects** .

Methods allow objects to  **perform actions** .

Example actions:

* A **Car** can `start()` and `stop()`
* A **Student** can `study()`
* A **BankAccount** can `deposit()` and `withdraw()`

In Python, there are  **three types of methods** :

1. **Instance Methods**
2. **Class Methods**
3. **Static Methods**

We will understand each one clearly.

### 1. Instance Methods

Instance methods are the  **most common type of methods** .
They work with  **object data (instance variables)** .

They always take  **`self` as the first parameter** .

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student name:", self.name)

s1 = Student("Ahmad")
s1.display()
```

Output

```
Student name: Ahmad
```

Explanation

`display()` is an **instance method** because it works with `self.name`.

Internal execution:

```
s1.display()
```

Python converts it to:

```
Student.display(s1)
```

So `self` becomes the object `s1`.

### Example 2

```python
class Calculator:

    def add(self, a, b):
        return a + b

calc = Calculator()

print(calc.add(5, 3))
```

Output

```
8
```

Here `add()` is an  **instance method** .

### 2. Class Methods

Class methods operate on the  **class itself rather than individual objects** .

They use the  **`@classmethod` decorator** .

Instead of `self`, they use **`cls`** as the first parameter.

`cls` refers to the  **class itself** .

Example:

```python
class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

Employee.change_company("Microsoft")

print(Employee.company)
```

Output

```
Microsoft
```

Explanation

`change_company()` modifies the  **class variable** .

All objects will see the change.

Example:

```python
class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, name):
        cls.company = name

emp1 = Employee()
emp2 = Employee()

Employee.change_company("Amazon")

print(emp1.company)
print(emp2.company)
```

Output

```
Amazon
Amazon
```

Both objects reflect the updated class property.

### 3. Static Methods

Static methods  **do not depend on class or object data** .

They behave like  **normal functions inside a class** .

They use the decorator:

```
@staticmethod
```

Example:

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 7))
```

Output

```
12
```

Explanation

`add()` does not use `self` or `cls`.

It is just a  **utility function inside the class** .

### Another Example

```python
class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(Temperature.celsius_to_fahrenheit(30))
```

Output

```
86
```

### Visual Difference

```
Instance Method
   |
   |--- Uses self
   |--- Works with object data

Class Method
   |
   |--- Uses cls
   |--- Works with class data

Static Method
   |
   |--- No self or cls
   |--- Independent utility function
```

### Comparison Table

| Type            | First Parameter | Works With        |
| --------------- | --------------- | ----------------- |
| Instance Method | `self`        | Object data       |
| Class Method    | `cls`         | Class data        |
| Static Method   | None            | Independent logic |

### Example Combining All Three

```python
class Example:

    class_var = 10

    def instance_method(self):
        print("Instance Method")

    @classmethod
    def class_method(cls):
        print("Class Method")

    @staticmethod
    def static_method():
        print("Static Method")

obj = Example()

obj.instance_method()
Example.class_method()
Example.static_method()
```

Output

```
Instance Method
Class Method
Static Method
```

### Key Points

Methods define  **behavior of objects** .

Three types:

Instance Method
Uses `self`

Class Method
Uses `@classmethod` and `cls`

Static Method
Uses `@staticmethod`

General structure:

```python
class Example:

    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass
```

---

### 8. Python Inheritance

**Inheritance** is one of the most important concepts in Object-Oriented Programming.

Inheritance allows a  **class to acquire the properties and methods of another class** .

In simple terms:

A  **child class can reuse the code of a parent class** .

This helps in:

* Code reusability
* Reducing duplication
* Better program organization

### Basic Idea

```text
Parent Class (Base Class)
        ↓
Child Class (Derived Class)
```

The  **child class automatically gets all attributes and methods of the parent class** .

### Syntax of Inheritance

```python
class ParentClass:
    # parent properties and methods


class ChildClass(ParentClass):
    # child properties and methods
```

The  **child class is written inside parentheses** .

### Example 1: Basic Inheritance

```python
class Animal:

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    pass


dog = Dog()
dog.speak()
```

Output

```
Animal makes a sound
```

Explanation

`Dog` inherits from `Animal`, so it automatically gets the `speak()` method.

Structure

```
Animal
   |
   └── Dog
```

### Example 2: Child Class with Its Own Method

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()
```

Output

```
Animal is eating
Dog is barking
```

Explanation

`Dog` can use:

* Parent method → `eat()`
* Child method → `bark()`

### Example 3: Using `__init__` with Inheritance

```python
class Person:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Student(Person):
    pass


s = Student("Ahmad")
s.show()
```

Output

```
Name: Ahmad
```

The `Student` class  **inherits the constructor from the parent class** .

### Example 4: Method Overriding

A child class can  **modify a method from the parent class** .

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        print("Dog barks")


dog = Dog()
dog.speak()
```

Output

```
Dog barks
```

The child class  **overrides the parent method** .

### Using `super()` in Inheritance

`super()` allows the child class to  **access methods of the parent class** .

Example

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


s = Student("Ahmad", 22)

print(s.name)
print(s.age)
```

Output

```
Ahmad
22
```

Explanation

`super().__init__(name)` calls the  **parent constructor** .

### Types of Inheritance in Python

Python supports multiple inheritance types.

1. **Single Inheritance**

```
Parent
   |
 Child
```

Example

```python
class A:
    pass

class B(A):
    pass
```

2. **Multiple Inheritance**

A child class inherits from  **multiple parent classes** .

```
Parent1   Parent2
     \     /
      Child
```

Example

```python
class A:
    def show(self):
        print("Class A")


class B:
    def display(self):
        print("Class B")


class C(A, B):
    pass


obj = C()
obj.show()
obj.display()
```

3. **Multilevel Inheritance**

```
Grandparent
      |
   Parent
      |
    Child
```

Example

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

### Real Example

```python
class Vehicle:

    def start(self):
        print("Vehicle starting")


class Car(Vehicle):

    def drive(self):
        print("Car driving")


car = Car()

car.start()
car.drive()
```

Output

```
Vehicle starting
Car driving
```

Here `Car` inherits features from `Vehicle`.

### Key Points

Inheritance allows  **one class to reuse another class's code** .

Terminology

Parent Class → Base class
Child Class → Derived class

Syntax

```python
class Child(Parent):
```

Benefits

* Code reuse
* Extensibility
* Cleaner architecture

---

### 9. Python Polymorphism

**Polymorphism** means  **"many forms"** .

In Object-Oriented Programming, polymorphism allows  **the same method name or operation to behave differently depending on the object** .

Simple idea:

```
Same Method Name
        ↓
Different Behavior
```

Polymorphism improves  **flexibility and extensibility of code** .

In Python, polymorphism mainly appears in:

1. **Method Overriding**
2. **Operator Overloading**
3. **Method Polymorphism**

### Example 1: Simple Polymorphism

Different objects responding to the same method.

```python
class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

Output

```
Dog barks
Cat meows
```

Explanation

Both classes use the  **same method name `sound()`** , but behavior is different.

### Example 2: Polymorphism with Loop

Python allows calling the same method on different objects.

```python
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


class Cow:
    def sound(self):
        print("Cow moos")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
```

Output

```
Dog barks
Cat meows
Cow moos
```

The loop does  **not care about object type** .

It only calls `sound()`.

### Example 3: Method Overriding (Inheritance Polymorphism)

When a child class  **redefines a parent method** , it is called  **method overriding** .

```python
class Animal:

    def speak(self):
        print("Animal makes sound")


class Dog(Animal):

    def speak(self):
        print("Dog barks")


class Cat(Animal):

    def speak(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
```

Output

```
Dog barks
Cat meows
```

Each child class  **overrides the parent method** .

### Example 4: Operator Overloading

Python operators also behave  **differently for different data types** .

Example of `+` operator.

```python
print(5 + 3)
print("Hello " + "World")
print([1,2] + [3,4])
```

Output

```
8
Hello World
[1,2,3,4]
```

Here `+` performs:

```
Numbers → Addition
Strings → Concatenation
Lists → Merge
```

Same operator, different behavior →  **Polymorphism** .

### Example 5: Function Polymorphism

Some Python functions automatically support polymorphism.

Example: `len()`

```python
print(len("Python"))
print(len([1,2,3,4]))
print(len({"a":1, "b":2}))
```

Output

```
6
4
2
```

The same function works for  **different data types** .

### Real World Example

```python
class Shape:

    def area(self):
        pass


class Rectangle(Shape):

    def area(self):
        print("Rectangle Area")


class Circle(Shape):

    def area(self):
        print("Circle Area")


shapes = [Rectangle(), Circle()]

for shape in shapes:
    shape.area()
```

Output

```
Rectangle Area
Circle Area
```

Same method `area()` works for  **different shapes** .

### Visual Representation

```
Animal
   |
   |--- Dog → speak() → Bark
   |
   |--- Cat → speak() → Meow
```

Same method name, different behavior.

### Key Points

Polymorphism means  **same interface, different behavior** .

Common forms in Python:

Method overriding
Operator overloading
Function polymorphism

Benefits

* Flexible code
* Cleaner design
* Easier extension

General structure

```python
object.method()
```

The method behavior depends on  **object type** .

---

### 10. Python Encapsulation

**Encapsulation** is the concept of  **wrapping data (variables) and methods (functions) together inside a class and restricting direct access to some of the data** .

The goal of encapsulation is to:

* **Protect object data**
* Prevent accidental modification
* Control how data is accessed or modified

Simple idea:

```text
Data + Methods
     ↓
  Encapsulation
```

The class **hides internal details** and only exposes necessary functionality.

### Example Without Encapsulation

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance


account = BankAccount(5000)

account.balance = -1000
print(account.balance)
```

Output

```
-1000
```

Problem:
Anyone can directly change `balance` to an invalid value.

Encapsulation solves this problem.

### Encapsulation in Python

Python provides  **three access levels** .

1. **Public**
2. **Protected**
3. **Private**

### 1. Public Variables

Public variables can be accessed  **from anywhere** .

Example

```python
class Student:

    def __init__(self, name):
        self.name = name


s = Student("Ahmad")

print(s.name)
```

Output

```
Ahmad
```

`name` is  **public** .

Structure

```text
class Student
     |
     |-- name (public)
```

### 2. Protected Variables

Protected variables are indicated using a  **single underscore `_`** .

Convention:
They  **should not be accessed directly outside the class** , but Python does not strictly prevent it.

Example

```python
class Student:

    def __init__(self, name):
        self._name = name


s = Student("Ahmad")

print(s._name)
```

Output

```
Ahmad
```

Here `_name` is  **protected** .

It means:

```text
Internal use recommended
```

### 3. Private Variables

Private variables are created using  **double underscore `__`** .

They cannot be accessed directly from outside the class.

Example

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance


account = BankAccount(5000)

print(account.__balance)
```

This will cause an error.

```
AttributeError
```

Because `__balance` is  **private** .

### Accessing Private Variables Using Methods

To access private data, we use  **getter methods** .

Example

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print(account.get_balance())
```

Output

```
5000
```

Now the balance is  **safely accessed through a method** .

### Modifying Private Data Safely

We can also use  **setter methods** .

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(2000)

print(account.get_balance())
```

Output

```
7000
```

Now the balance can only change  **through controlled methods** .

### Python Name Mangling (Internal Mechanism)

Python internally renames private variables.

Example

```python
class Test:

    def __init__(self):
        self.__value = 10
```

Internally it becomes

```text
_Test__value
```

So technically it can still be accessed like this:

```python
print(obj._Test__value)
```

But this is  **not recommended** .

### Visual Representation

```
Class
   |
   |--- Public → accessible everywhere
   |
   |--- Protected → internal use
   |
   |--- Private → restricted access
```

### Comparison

| Access Type | Symbol         | Access                  |
| ----------- | -------------- | ----------------------- |
| Public      | `variable`   | Anywhere                |
| Protected   | `_variable`  | Within class / subclass |
| Private     | `__variable` | Only inside class       |

### Key Points

Encapsulation hides  **internal object data** .

Access levels:

Public
Protected
Private

Private data is accessed using:

* Getter methods
* Setter methods

Encapsulation helps in:

* Data security
* Controlled modification
* Cleaner architecture

---

### 11. Python Inner Classes

An **Inner Class** is a class defined  **inside another class** .

It is used when one class is **logically related to another class** and should not exist independently.

Simple idea:

```
Outer Class
     |
     |---- Inner Class
```

The inner class is usually used to represent a  **component or part of the outer class** .

### Basic Syntax

```python
class OuterClass:

    class InnerClass:
        pass
```

The  **InnerClass exists inside OuterClass** .

### Example 1: Basic Inner Class

```python
class Outer:

    class Inner:

        def show(self):
            print("This is inner class method")


inner_obj = Outer.Inner()

inner_obj.show()
```

Output

```
This is inner class method
```

Explanation

To create an object of an inner class, we use:

```python
Outer.Inner()
```

### Example 2: Real World Example (Student and Laptop)

Suppose a  **Student has a Laptop** .

The laptop logically belongs to the student, so we can define it as an inner class.

```python
class Student:

    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()

    def show(self):
        print("Student:", self.name)

    class Laptop:

        def __init__(self):
            self.brand = "Dell"
            self.ram = 16

        def show(self):
            print("Laptop:", self.brand, self.ram)


s = Student("Ahmad")

s.show()
s.laptop.show()
```

Output

```
Student: Ahmad
Laptop: Dell 16
```

Structure

```
Student
   |
   |--- Laptop
```

Here:

`Student` → Outer class
`Laptop` → Inner class

Each student automatically  **has a laptop object** .

### Example 3: Multiple Students with Inner Objects

```python
class Student:

    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()

    class Laptop:

        def __init__(self):
            self.brand = "HP"


s1 = Student("Ahmad")
s2 = Student("Ali")

print(s1.laptop.brand)
print(s2.laptop.brand)
```

Output

```
HP
HP
```

Each student object contains its  **own inner laptop object** .

### Accessing Inner Class

There are  **two ways** .

#### Method 1: Through Outer Class

```python
obj = Outer.Inner()
```

Example

```python
inner_obj = Outer.Inner()
```

#### Method 2: Through Outer Object

```python
outer_obj.inner_obj
```

Example

```python
student.laptop.show()
```

### When to Use Inner Classes

Inner classes are useful when:

1. One class **depends completely on another class**
2. The inner class **should not exist independently**
3. The inner class represents a **part of another object**

Example relationships

```
Car
   └── Engine

University
   └── Department

Computer
   └── Processor
```

### Example: Car and Engine

```python
class Car:

    def __init__(self):
        self.engine = self.Engine()

    class Engine:

        def start(self):
            print("Engine started")


car = Car()

car.engine.start()
```

Output

```
Engine started
```

### Key Points

Inner class =  **class inside another class** .

Structure

```
Outer Class
     |
     └── Inner Class
```

Benefits

* Better organization
* Logical grouping
* Encapsulation of related components

Example structure

```python
class Outer:

    class Inner:
        pass
```

You have now completed the  **core OOP concepts in Python** :

1. Classes
2. OOP Basics
3. Classes / Objects
4. `__init__`
5. `self`
6. Class Properties
7. Class Methods
8. Inheritance
9. Polymorphism
10. Encapsulation
11. Inner Classes

---

### 12. Abstraction in Python

**Abstraction** means  **hiding internal implementation details and showing only the necessary functionality to the user** .

The user knows  **what a function does** , but not  **how it does it internally** .

Simple idea:

```text
User → Uses Function
          ↓
      Internal Logic Hidden
```

Real-life example:

```text
ATM Machine
```

You only press:

* Withdraw
* Deposit
* Check Balance

But you  **don’t see the internal banking system logic** .

That is  **abstraction** .

### How Abstraction is Implemented in Python

Python implements abstraction using:

* **Abstract Classes**
* **Abstract Methods**

This is done using the module:

```python
abc (Abstract Base Class)
```

### Importing Abstract Class Tools

```python
from abc import ABC, abstractmethod
```

`ABC` → Abstract Base Class
`abstractmethod` → method that must be implemented in child classes.

### Example 1: Abstract Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

Here:

`Shape` is an  **abstract class** .

`area()` is an  **abstract method** .

This means  **any child class must implement `area()`** .

### Example 2: Implementing Abstract Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def area(self):
        print("Rectangle area calculated")


class Circle(Shape):

    def area(self):
        print("Circle area calculated")


r = Rectangle()
c = Circle()

r.area()
c.area()
```

Output

```
Rectangle area calculated
Circle area calculated
```

Explanation

Both child classes  **must implement `area()`** , otherwise Python will raise an error.

### Important Rule

You  **cannot create an object of an abstract class** .

Example:

```python
shape = Shape()
```

This will raise an error.

Because abstract classes are meant to  **define structure only** .

### Real Example

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class CreditCard(Payment):

    def pay(self):
        print("Paid using credit card")


class UPI(Payment):

    def pay(self):
        print("Paid using UPI")


payment1 = CreditCard()
payment2 = UPI()

payment1.pay()
payment2.pay()
```

Output

```
Paid using credit card
Paid using UPI
```

The user only calls `pay()` but  **doesn't care about internal implementation** .

### Visual Representation

```
Abstract Class → Payment
         |
   -------------------
   |                 |
CreditCard         UPI
```

Each child class provides  **its own implementation** .

### Key Points

Abstraction hides  **implementation details** .

Implemented using:

```python
abc module
ABC
@abstractmethod
```

Abstract class defines  **rules for child classes** .

---

### 13. Magic Methods / Dunder Methods in Python

Magic methods are  **special methods in Python that start and end with double underscores `__`** .

They are also called **Dunder Methods** (Double Under).

Example:

```
__init__
__str__
__repr__
__len__
__add__
__getitem__
```

These methods allow  **custom objects to behave like built-in Python objects** .

For example:

* printing an object
* using operators (`+`, `-`, `*`)
* using `len()`
* indexing (`obj[0]`)

All of these internally use  **magic methods** .

### Why Magic Methods Are Important

They allow developers to  **customize how objects behave in Python** .

Example idea:

```
print(object)
```

Python internally calls

```
object.__str__()
```

### Example 1: `__init__`

You already learned this one.

It is called when an  **object is created** .

```python
class Student:

    def __init__(self, name):
        self.name = name

s = Student("Ahmad")
```

Internally Python does

```
Student.__init__(s, "Ahmad")
```

### Example 2: `__str__` (String Representation)

`__str__` defines  **what should be printed when we print an object** .

Without `__str__`:

```python
class Student:
    pass

s = Student()

print(s)
```

Output

```
<__main__.Student object at 0x7f4a>
```

This is  **not useful** .

Using `__str__`:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"


s = Student("Ahmad")

print(s)
```

Output

```
Student name is Ahmad
```

Now printing the object gives  **meaningful information** .

### Example 3: `__len__`

`__len__` allows your object to work with  **`len()`** .

```python
class Playlist:

    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


p = Playlist(["song1", "song2", "song3"])

print(len(p))
```

Output

```
3
```

Python internally calls:

```
p.__len__()
```

### Example 4: `__add__` (Operator Overloading)

This allows objects to use the  **`+` operator** .

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
```

Output

```
30
```

Internally Python converts

```
n1 + n2
```

to

```
n1.__add__(n2)
```

### Example 5: `__getitem__`

Allows objects to support  **indexing** .

```python
class Data:

    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]


d = Data([10,20,30,40])

print(d[2])
```

Output

```
30
```

Internally Python runs

```
d.__getitem__(2)
```

### Common Magic Methods

| Method          | Purpose                      |
| --------------- | ---------------------------- |
| `__init__`    | Object constructor           |
| `__str__`     | Object string representation |
| `__repr__`    | Developer representation     |
| `__len__`     | Length of object             |
| `__add__`     | `+`operator                |
| `__sub__`     | `-`operator                |
| `__getitem__` | Index access                 |
| `__eq__`      | Equality comparison          |

### Visual Example

```
Object Operation
        ↓
Python calls Magic Method
```

Examples

```
print(obj) → obj.__str__()

len(obj) → obj.__len__()

obj1 + obj2 → obj1.__add__(obj2)

obj[0] → obj.__getitem__(0)
```

### Real Libraries Using Magic Methods

Libraries like:

* NumPy
* Pandas
* PyTorch
* TensorFlow

heavily use magic methods to make objects behave like  **native Python structures** .

Example:

```
tensor1 + tensor2
```

works because of  **operator overloading (`__add__`)** .

### Key Points

Magic methods allow  **custom objects to behave like built-in types** .

They control:

* printing
* operators
* indexing
* length
* comparisons

Structure:

```python
def __method__(self):
```

---

### 14. Method Resolution Order (MRO)

**Method Resolution Order (MRO)** defines  **the order in which Python searches for methods and attributes in a class hierarchy** .

It becomes important when **multiple inheritance** is used.

Simple idea:

```text
If a method is called,
Python follows a specific order
to find where that method exists.
```

This search order is called  **MRO** .

### Why MRO is Needed

In single inheritance, method lookup is simple.

Example:

```text
Child → Parent
```

But in  **multiple inheritance** , a class may inherit from multiple parents.

Example:

```text
      A
     / \
    B   C
     \ /
      D
```

If class `D` calls a method, Python must decide:

```text
Should it use B's method or C's method?
```

This decision is made using  **MRO** .

### Example 1: Simple Inheritance MRO

```python
class A:

    def show(self):
        print("Class A")


class B(A):
    pass


obj = B()
obj.show()
```

Output

```
Class A
```

Search order:

```
B → A
```

Python first looks in  **B** , then in  **A** .

### Checking MRO

Python provides a built-in method:

```python
ClassName.mro()
```

Example

```python
print(B.mro())
```

Output

```
[B, A, object]
```

Explanation

Python will search methods in this order:

```
B → A → object
```

### Example 2: Multiple Inheritance

```python
class A:
    def show(self):
        print("Class A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


obj = D()
obj.show()
```

Output

```
Class A
```

But how does Python decide the order?

Check MRO:

```python
print(D.mro())
```

Output

```
[D, B, C, A, object]
```

Search order becomes

```
D → B → C → A → object
```

So Python checks:

1. Class `D`
2. Class `B`
3. Class `C`
4. Class `A`

### Example 3: Method Conflict

```python
class A:
    def show(self):
        print("Class A")


class B:
    def show(self):
        print("Class B")


class C(A, B):
    pass


obj = C()
obj.show()
```

Output

```
Class A
```

Check MRO:

```python
print(C.mro())
```

Output

```
[C, A, B, object]
```

Python searches in this order:

```
C → A → B → object
```

Since `A` has `show()`, Python uses that.

### Example 4: Changing Parent Order

```python
class A:
    def show(self):
        print("Class A")


class B:
    def show(self):
        print("Class B")


class C(B, A):
    pass


obj = C()
obj.show()
```

Output

```
Class B
```

MRO becomes

```
[C, B, A, object]
```

Now Python finds the method in  **B first** .

### Visual Representation

Example:

```
class D(B, C)
```

MRO:

```
D
↓
B
↓
C
↓
A
↓
object
```

Python searches  **top to bottom** .

### C3 Linearization (Concept)

Python uses an algorithm called **C3 Linearization** to calculate MRO.

Rules:

1. **Child class is checked first**
2. **Parents are checked left to right**
3. **A parent is never checked before its child**

Example

```
class D(B, C)
```

Python ensures:

```
B comes before C
```

because it appears first in the class definition.

### Example with `super()`

`super()` follows  **MRO order** .

Example:

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(B):
    def show(self):
        print("C")
        super().show()


obj = C()
obj.show()
```

Output

```
C
B
A
```

Execution follows MRO:

```
C → B → A
```

### Checking MRO Easily

```python
print(ClassName.mro())
```

or

```python
print(ClassName.__mro__)
```

Example

```python
print(C.__mro__)
```

### Key Points

MRO determines  **method search order** .

Python checks methods in this order:

```
Child → Parent → Parent's Parent → object
```

Important when using:

* Multiple inheritance
* `super()`

Useful command:

```python
ClassName.mro()
```
