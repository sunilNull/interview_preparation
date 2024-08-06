Certainly! Here are detailed answers to each of the questions:

### Python Basics

1. **What are Python’s key features?**
   - Python is an interpreted, high-level, general-purpose programming language with dynamic typing and binding. Key features include:
     - **Readability:** Clean, readable syntax.
     - **Interpreted Language:** No need for compilation, executed line-by-line.
     - **Dynamically Typed:** No need to declare variable types.
     - **Extensive Libraries:** Rich standard library and many third-party packages.
     - **Community Support:** Large, active community and extensive documentation.
     - **Cross-Platform:** Runs on various operating systems.

2. **How is Python interpreted?**
   - Python code is executed by the Python interpreter, which performs the following steps:
     - **Parsing:** Converts source code into a parse tree.
     - **Compilation:** Converts the parse tree into bytecode.
     - **Execution:** Bytecode is executed by the Python Virtual Machine (PVM).

3. **What is PEP 8 and why is it important?**
   - PEP 8 is the Python Enhancement Proposal that provides guidelines and best practices on how to write Python code. It is important because:
     - **Consistency:** Ensures a consistent coding style.
     - **Readability:** Makes code easier to read and understand.
     - **Collaboration:** Facilitates collaboration among developers.

4. **How does memory management work in Python?**
   - Python uses automatic memory management with the following mechanisms:
     - **Reference Counting:** Tracks the number of references to an object.
     - **Garbage Collection:** Reclaims memory by collecting objects with zero references.
     - **Dynamic Typing:** Allocates memory dynamically for variables.

5. **Explain the use of decorators.**
   - Decorators are functions that modify the behavior of another function or method. They are used to:
     - **Add Functionality:** Enhance or modify functions without changing their code.
     - **Code Reusability:** Reuse common patterns like logging, authentication, etc.
     - **Readability:** Keep code clean and readable.

6. **What are *args and **kwargs?**
   - `*args` allows a function to accept any number of positional arguments.
   - `**kwargs` allows a function to accept any number of keyword arguments.
   - They are used to write flexible and reusable functions.

7. **What are list comprehensions?**
   - List comprehensions provide a concise way to create lists. Syntax:
     ```python
     [expression for item in iterable if condition]
     ```
   - Example:
     ```python
     squares = [x**2 for x in range(10) if x % 2 == 0]
     ```

8. **What is the difference between a list and a tuple?**
   - **List:** Mutable, can be changed (add, remove, modify elements).
   - **Tuple:** Immutable, cannot be changed once created. Used for fixed collections.

9. **How does Python handle type conversion?**
   - **Explicit Conversion:** Using functions like `int()`, `float()`, `str()`, `list()`, etc.
   - **Implicit Conversion:** Performed by the interpreter in certain expressions.

10. **What is the difference between Python 2 and Python 3?**
    - **Print Function:** `print` is a function in Python 3 (`print()`).
    - **Integer Division:** `5 / 2` returns `2.5` in Python 3.
    - **Unicode Strings:** Default string type is Unicode in Python 3.
    - **Syntax Improvements:** Better syntax consistency and removal of old constructs.

### Advanced Python

11. **Explain the GIL (Global Interpreter Lock).**
    - The GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes simultaneously. It:
      - **Simplifies Memory Management:** Ensures that only one thread interacts with Python objects at a time.
      - **Bottleneck:** Can be a performance bottleneck in CPU-bound multi-threaded programs.

12. **What are metaclasses in Python?**
    - Metaclasses are classes of classes that define how a class behaves. They:
      - **Customize Class Creation:** Allow customization of class creation and behavior.
      - **Syntax:** Defined by inheriting from `type` and overriding `__new__` and `__init__` methods.

13. **How do you create and use static methods and class methods?**
    - **Static Method:** Defined using `@staticmethod`. Does not take `self` or `cls`.
      ```python
      class MyClass:
          @staticmethod
          def static_method():
              print("This is a static method")
      ```
    - **Class Method:** Defined using `@classmethod`. Takes `cls` as the first parameter.
      ```python
      class MyClass:
          @classmethod
          def class_method(cls):
              print("This is a class method")
      ```

14. **What is the purpose of the `__init__.py` file?**
    - The `__init__.py` file:
      - **Package Initialization:** Marks a directory as a Python package.
      - **Initialization Code:** Can execute package initialization code.
      - **Public Interface:** Defines the public interface using `__all__`.

15. **Explain the difference between deep copy and shallow copy.**
    - **Shallow Copy:** Creates a new object, but inserts references to the objects found in the original.
      ```python
      import copy
      original = [1, [2, 3]]
      shallow_copy = copy.copy(original)
      ```
    - **Deep Copy:** Creates a new object and recursively copies all objects found in the original.
      ```python
      deep_copy = copy.deepcopy(original)
      ```

16. **How do you handle exceptions in Python?**
    - Exceptions are handled using `try-except` blocks.
      ```python
      try:
          risky_code()
      except Exception as e:
          handle_exception(e)
      else:
          execute_if_no_exception()
      finally:
          execute_always()
      ```

17. **What are context managers?**
    - Context managers allow for the setup and cleanup of resources using the `with` statement. They:
      - **Implement `__enter__` and `__exit__` Methods:** Manage resource allocation and deallocation.
      - **Example:**
        ```python
        with open('file.txt', 'r') as file:
            content = file.read()
        ```

18. **How do you use lambda functions?**
    - Lambda functions are small anonymous functions defined using the `lambda` keyword. Syntax:
      ```python
      lambda arguments: expression
      ```
    - Example:
      ```python
      add = lambda x, y: x + y
      result = add(2, 3)
      ```

19. **What is the difference between map, filter, and reduce?**
    - **map:** Applies a function to all items in an iterable.
      ```python
      result = map(lambda x: x * 2, [1, 2, 3])
      ```
    - **filter:** Creates a list of elements for which a function returns true.
      ```python
      result = filter(lambda x: x % 2 == 0, [1, 2, 3])
      ```
    - **reduce:** Applies a function of two arguments cumulatively to the items of an iterable, reducing it to a single value.
      ```python
      from functools import reduce
      result = reduce(lambda x, y: x + y, [1, 2, 3])
      ```

20. **Explain the concept of iterators and generators.**
    - **Iterators:** Objects that implement the `__iter__` and `__next__` methods.
      ```python
      class MyIterator:
          def __iter__(self):
              return self
          def __next__(self):
              # return next item
      ```
    - **Generators:** Functions that use the `yield` statement to produce a sequence of values.
      ```python
      def my_generator():
          yield 1
          yield 2
          yield 3
      ```

### Object-Oriented Programming (OOP)

21. **What is OOP and how is it implemented in Python?**
    - OOP (Object-Oriented Programming) is a programming paradigm based on the concept of objects. Python implements OOP with:
      - **Classes and Objects:** Classes are blueprints for objects.
      - **Encapsulation, Inheritance, Polymorphism, and Abstraction:** Core OOP principles.
      - **Syntax:**
        ```python
        class MyClass:
            def __init__(self, value):
                self.value = value
            def method(self):
                return self.value
        ```

22. **Explain inheritance in Python.**
    - Inheritance allows a class to inherit attributes and methods from another class.
      ```python
      class BaseClass:
          def base_method(self):
              pass
      class DerivedClass(BaseClass):
          def derived_method(self):
              pass
      ```

23. **What is polymorphism?**
    - Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables methods to be used interchangeably.
      ```python
      class Shape:
          def draw(self):
              pass
      class Circle(Shape):
          def draw(self):
              print("Drawing Circle")
      class Square(Shape):
          def draw(self):
              print("Drawing Square")
      def draw_shape(shape):
          shape.draw()
      ```

24. **What is encapsulation and how does Python achieve it?**
    - Encapsulation restricts direct access to

 an object's data and methods. Python achieves encapsulation using:
      - **Private Attributes:** Prefixing attributes with an underscore `_`.
      - **Example:**
        ```python
        class MyClass:
            def __init__(self):
                self._private_attribute = "private"
        ```

25. **How do you implement abstraction in Python?**
    - Abstraction is implemented using abstract base classes (ABCs) and the `abc` module.
      ```python
      from abc import ABC, abstractmethod
      class AbstractClass(ABC):
          @abstractmethod
          def abstract_method(self):
              pass
      class ConcreteClass(AbstractClass):
          def abstract_method(self):
              print("Implemented abstract method")
      ```

26. **What is method overriding?**
    - Method overriding occurs when a subclass provides a specific implementation of a method already defined in its superclass.
      ```python
      class BaseClass:
          def method(self):
              print("Base method")
      class DerivedClass(BaseClass):
          def method(self):
              print("Overridden method")
      ```

27. **What is method overloading?**
    - Method overloading is not directly supported in Python, but can be achieved using default arguments or variable-length arguments.
      ```python
      class MyClass:
          def method(self, a, b=None):
              if b is None:
                  print("Single argument")
              else:
                  print("Two arguments")
      ```

28. **How do you define a class in Python?**
    - A class is defined using the `class` keyword.
      ```python
      class MyClass:
          def __init__(self, value):
              self.value = value
          def method(self):
              return self.value
      ```

29. **Explain multiple inheritance.**
    - Multiple inheritance allows a class to inherit from more than one base class.
      ```python
      class Base1:
          def method1(self):
              pass
      class Base2:
          def method2(self):
              pass
      class Derived(Base1, Base2):
          pass
      ```

30. **What is the MRO (Method Resolution Order)?**
    - The MRO determines the order in which base classes are searched when looking for a method. Python uses the C3 linearization algorithm.
      ```python
      class A: pass
      class B(A): pass
      class C(A): pass
      class D(B, C): pass
      print(D.__mro__)
      ```

### Libraries and Frameworks

31. **What is Django and why is it used?**
    - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is used for:
      - **Scalability:** Handles large applications.
      - **Security:** Built-in security features.
      - **Batteries Included:** Provides tools and libraries for common web development tasks.

32. **Explain the MVC pattern in Django.**
    - Django follows the Model-View-Template (MVT) pattern, similar to MVC.
      - **Model:** Defines the data structure.
      - **View:** Handles business logic and interacts with the model.
      - **Template:** Renders the data to the user.

33. **What are Django models?**
    - Django models define the structure of the database. They are Python classes that map to database tables.
      ```python
      from django.db import models
      class MyModel(models.Model):
          name = models.CharField(max_length=100)
          age = models.IntegerField()
      ```

34. **How does Django handle database migrations?**
    - Django uses migrations to propagate changes made to models into the database schema.
      - **makemigrations:** Creates migration files based on model changes.
      - **migrate:** Applies the migration files to the database.

35. **What is Flask and how does it compare to Django?**
    - Flask is a lightweight WSGI web application framework. It is:
      - **Flexible:** Allows more control over components.
      - **Microframework:** Minimalistic, without built-in tools.
      - **Compared to Django:** Flask is more suitable for smaller applications or APIs, while Django is better for larger, more complex applications.

36. **Explain the use of SQLAlchemy.**
    - SQLAlchemy is an SQL toolkit and Object-Relational Mapping (ORM) library. It provides:
      - **Database Abstraction:** Interacts with databases using Python objects.
      - **Flexibility:** Works with various databases.
      - **Example:**
        ```python
        from sqlalchemy import create_engine, Column, Integer, String, Sequence
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.orm import sessionmaker

        engine = create_engine('sqlite:///:memory:')
        Base = declarative_base()

        class User(Base):
            __tablename__ = 'users'
            id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
            name = Column(String(50))

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        ```

37. **What is Celery and how is it used?**
    - Celery is an asynchronous task queue/job queue based on distributed message passing. It is used to:
      - **Offload Tasks:** Execute long-running tasks asynchronously.
      - **Example:**
        ```python
        from celery import Celery
        app = Celery('tasks', broker='pyamqp://guest@localhost//')
        @app.task
        def add(x, y):
            return x + y
        ```

38. **Describe the purpose of pytest.**
    - `pytest` is a testing framework that makes it easy to write simple and scalable test cases for Python code. It provides:
      - **Fixtures:** For setup and teardown code.
      - **Plugins:** For extended functionality.
      - **Example:**
        ```python
        def test_addition():
            assert add(2, 3) == 5
        ```

39. **How do you manage dependencies in a Python project?**
    - Dependencies are managed using tools like `pip` and `virtualenv`.
      - **Requirements File:** Lists all dependencies.
        ```python
        pip freeze > requirements.txt
        pip install -r requirements.txt
        ```

40. **What is the purpose of a virtual environment?**
    - A virtual environment isolates Python dependencies for a project, preventing conflicts with other projects. It ensures that:
      - **Dependencies:** Each project has its own set of dependencies.
      - **Isolation:** No interference between projects.

### Data Handling and APIs

41. **How do you work with JSON in Python?**
    - JSON data can be handled using the `json` module.
      ```python
      import json
      data = {'key': 'value'}
      json_str = json.dumps(data)
      data = json.loads(json_str)
      ```

42. **What is RESTful API and how do you implement it in Python?**
    - RESTful API is an architectural style for designing networked applications. It uses standard HTTP methods. Implementation example with Flask:
      ```python
      from flask import Flask, jsonify, request
      app = Flask(__name__)
      @app.route('/api/resource', methods=['GET'])
      def get_resource():
          return jsonify({'key': 'value'})
      @app.route('/api/resource', methods=['POST'])
      def create_resource():
          data = request.json
          return jsonify(data), 201
      ```

43. **Explain the use of requests library.**
    - The `requests` library is used to make HTTP requests in Python.
      ```python
      import requests
      response = requests.get('https://api.example.com/data')
      data = response.json()
      ```

44. **How do you handle authentication in a web application?**
    - Authentication can be handled using various methods, such as:
      - **Session-Based:** Using cookies and server-side sessions.
      - **Token-Based:** Using JWT (JSON Web Tokens).
      - **OAuth:** For third-party authentication.

45. **What are WebSockets and how do you use them in Python?**
    - WebSockets provide full-duplex communication channels over a single TCP connection. Example using `websockets` library:
      ```python
      import asyncio
      import websockets

      async def echo(websocket, path):
          async for message in websocket:
              await websocket.send(message)

      start_server = websockets.serve(echo, 'localhost', 8765)

      asyncio.get_event_loop().run_until_complete(start_server)
      asyncio.get_event_loop().run_forever()
      ```

46. **How do you use Pandas for data manipulation?**
    - Pandas provides data structures like DataFrame and Series for data manipulation.
      ```python
      import pandas as pd
      df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
      df['col3'] = df['col1'] + df['col2']
      ```

47. **What is the role of NumPy in scientific computing?**
    - NumPy provides support for arrays, matrices, and high-level mathematical functions. It is widely used for:
      - **Numerical Computations:** Efficient array operations.
      - **Example:**
        ```python
        import numpy as np
        arr = np.array([1, 2, 3])
        result = np.mean(arr)
        ```

48. **How do you interact with a database in Python?**
    - Databases can be interacted with using libraries like `sqlite3` for SQLite, `psycopg2` for PostgreSQL, and `mysql-connector` for MySQL.
      ```python
     

 import sqlite3
      conn = sqlite3.connect('example.db')
      cursor = conn.cursor()
      cursor.execute('CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, value TEXT)')
      conn.commit()
      conn.close()
      ```

49. **What is the use of the `with` statement in file handling?**
    - The `with` statement ensures proper acquisition and release of resources. It is commonly used for file handling.
      ```python
      with open('file.txt', 'r') as file:
          content = file.read()
      ```

50. **How do you handle CSV files in Python?**
    - CSV files can be handled using the `csv` module or Pandas.
      ```python
      import csv
      with open('file.csv', 'r') as file:
          reader = csv.reader(file)
          for row in reader:
              print(row)
      ```

### Best Practices

51. **What is PEP 20?**
    - PEP 20 is "The Zen of Python," which provides aphorisms guiding the design of Python. It can be accessed by:
      ```python
      import this
      ```

52. **How do you optimize Python code for performance?**
    - Optimizing Python code involves:
      - **Profiling:** Using tools like `cProfile`.
      - **Efficient Data Structures:** Choosing the right data structures.
      - **Avoiding Unnecessary Computations:** Minimizing redundant calculations.
      - **Using Built-in Functions:** Leveraging Python's optimized built-in functions.

53. **What is test-driven development (TDD)?**
    - TDD is a software development approach where tests are written before writing the actual code. It involves:
      - **Writing Tests:** Define the expected behavior.
      - **Implementing Code:** Write the minimum code to pass the tests.
      - **Refactoring:** Improve the code while ensuring tests still pass.

54. **How do you document Python code?**
    - Python code can be documented using:
      - **Docstrings:** Describing the purpose and usage of functions, classes, and modules.
        ```python
        def my_function():
            """This is a docstring."""
            pass
        ```
      - **Comments:** Adding inline explanations and clarifications.

55. **What is Continuous Integration (CI)?**
    - CI is a practice where developers frequently integrate their code into a shared repository, followed by automated builds and tests. It ensures:
      - **Early Detection:** Early detection of integration issues.
      - **Quality Assurance:** Automated testing ensures code quality.

56. **Explain the Singleton pattern.**
    - The Singleton pattern ensures a class has only one instance and provides a global point of access to it.
      ```python
      class Singleton:
          _instance = None
          def __new__(cls, *args, **kwargs):
              if not cls._instance:
                  cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
              return cls._instance
      ```

57. **What is the Factory pattern?**
    - The Factory pattern provides a way to create objects without specifying the exact class of the object that will be created.
      ```python
      class ShapeFactory:
          def create_shape(self, shape_type):
              if shape_type == 'circle':
                  return Circle()
              elif shape_type == 'square':
                  return Square()
      ```

58. **Explain Dependency Injection.**
    - Dependency Injection is a design pattern where dependencies are injected into a class, rather than the class creating them itself. It promotes loose coupling and easier testing.

59. **What is the Observer pattern?**
    - The Observer pattern defines a one-to-many dependency between objects, where one object (subject) notifies many other objects (observers) of any state changes.
      ```python
      class Subject:
          def __init__(self):
              self._observers = []
          def attach(self, observer):
              self._observers.append(observer)
          def notify(self, message):
              for observer in self._observers:
                  observer.update(message)
      ```

60. **What are design patterns and why are they important?**
    - Design patterns are reusable solutions to common software design problems. They provide:
      - **Best Practices:** Proven solutions to recurring problems.
      - **Code Readability:** Standardized approaches make code more understandable.
      - **Efficiency:** Save time by reusing existing solutions.

### Miscellaneous

61. **How do you handle large files in Python?**
    - Large files can be handled efficiently by:
      - **Reading in Chunks:** Process the file in smaller chunks.
        ```python
        with open('large_file.txt', 'r') as file:
            while chunk := file.read(1024):
                process(chunk)
        ```
      - **Using Generators:** Yield lines or chunks of the file.

62. **What are Python’s built-in data structures?**
    - Python's built-in data structures include:
      - **List:** Ordered, mutable sequence of elements.
      - **Tuple:** Ordered, immutable sequence of elements.
      - **Set:** Unordered collection of unique elements.
      - **Dictionary:** Unordered collection of key-value pairs.

63. **Explain the use of `itertools` module.**
    - The `itertools` module provides functions for creating iterators for efficient looping.
      - **Examples:** `chain()`, `cycle()`, `repeat()`, `combinations()`.
      ```python
      import itertools
      for item in itertools.chain([1, 2], [3, 4]):
          print(item)
      ```

64. **What is the `functools` module?**
    - The `functools` module provides higher-order functions for working with functions and callable objects.
      - **Examples:** `lru_cache()`, `partial()`, `reduce()`.
      ```python
      from functools import lru_cache
      @lru_cache(maxsize=128)
      def expensive_function(param):
          pass
      ```

65. **How do you implement logging in Python?**
    - Logging is implemented using the `logging` module.
      ```python
      import logging
      logging.basicConfig(level=logging.INFO)
      logging.info("This is an info message")
      ```

66. **What is the use of `argparse` module?**
    - The `argparse` module is used for parsing command-line arguments.
      ```python
      import argparse
      parser = argparse.ArgumentParser(description="A simple argument parser")
      parser.add_argument('name', type=str, help="Name of the user")
      args = parser.parse_args()
      print(f"Hello, {args.name}")
      ```

67. **How do you handle time and date in Python?**
    - Time and date can be handled using the `datetime` module.
      ```python
      from datetime import datetime
      now = datetime.now()
      formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
      ```

68. **What is the difference between synchronous and asynchronous code?**
    - **Synchronous:** Code executes sequentially, one task at a time.
    - **Asynchronous:** Code allows multiple tasks to be executed concurrently, improving performance in I/O-bound operations.

69. **Explain the use of `asyncio` module.**
    - The `asyncio` module is used for writing asynchronous code using coroutines and event loops.
      ```python
      import asyncio
      async def main():
          print("Hello")
          await asyncio.sleep(1)
          print("World")
      asyncio.run(main())
      ```

70. **How do you test exceptions in Python?**
    - Exceptions can be tested using `pytest` or `unittest` modules.
      ```python
      import pytest
      def test_zero_division():
          with pytest.raises(ZeroDivisionError):
              1 / 0
      ```

### Python Internals

71. **What is the difference between `__str__` and `__repr__`?**
    - **`__str__`:** Returns a human-readable string representation of an object.
    - **`__repr__`:** Returns an unambiguous string representation of an object, ideally one that could be used to recreate the object.

72. **What are Python’s built-in types?**
    - Built-in types include `int`, `float`, `str`, `list`, `tuple`, `set`, `dict`, `bool`, `bytes`, etc.

73. **How does Python’s garbage collector work?**
    - Python’s garbage collector uses reference counting and generational garbage collection to manage memory. It automatically deallocates objects that are no longer referenced.

74. **What are Python’s special methods?**
    - Special methods (also known as magic methods) are predefined methods with double underscores, such as `__init__`, `__str__`, `__repr__`, `__add__`, etc. They allow custom behavior for built-in operations.

75. **Explain the use of `__slots__`.**
    - `__slots__` is used to explicitly declare data members and prevent the creation of `__dict__` and `__weakref__` attributes. It can save memory and improve performance.
      ```python
      class MyClass:
          __slots__ = ['attribute1', 'attribute2']
      ```

76. **What is the purpose of the `@property` decorator?**
    - The `@property` decorator is used to define properties in a class, allowing methods to be accessed like attributes.
      ```python
      class MyClass:
          def __init__(self, value):
              self._value = value
          @property
          def value(self):
              return

 self._value
          @value.setter
          def value(self, new_value):
              self._value = new_value
      ```

77. **How do you handle circular imports in Python?**
    - Circular imports can be handled by:
      - **Refactoring:** Moving imports inside functions or methods.
      - **Reorganizing Code:** Breaking modules into smaller, more manageable pieces.
      - **Using `importlib`:** Dynamically importing modules.

78. **What is the Global Interpreter Lock (GIL)?**
    - The GIL is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecode simultaneously. It ensures thread safety but can be a bottleneck for CPU-bound programs.

79. **How does Python’s memory management work?**
    - Python uses a private heap for memory management, which is managed by the interpreter. Memory allocation and deallocation are handled by the built-in garbage collector.

80. **What is a context manager?**
    - A context manager is an object that defines methods `__enter__` and `__exit__` to set up and tear down resources. It is commonly used with the `with` statement.
      ```python
      class MyContext:
          def __enter__(self):
              print("Entering context")
          def __exit__(self, exc_type, exc_value, traceback):
              print("Exiting context")
      with MyContext():
          print("Inside context")
      ```

81. **What is the purpose of `__name__ == "__main__"`?**
    - It allows code to be run when the module is executed as a script, but not when it is imported as a module.
      ```python
      if __name__ == "__main__":
          main()
      ```

82. **Explain the use of decorators in Python.**
    - Decorators are functions that modify the behavior of other functions or methods. They are often used for logging, access control, memoization, etc.
      ```python
      def my_decorator(func):
          def wrapper():
              print("Before function call")
              func()
              print("After function call")
          return wrapper
      @my_decorator
      def my_function():
          print("Inside function")
      ```

83. **How do you create a package in Python?**
    - A package is created by organizing modules into directories and including an `__init__.py` file.
      ```text
      mypackage/
          __init__.py
          module1.py
          module2.py
      ```

84. **What is the purpose of `__init__.py`?**
    - The `__init__.py` file indicates that the directory should be treated as a package. It can also be used to initialize package-level variables and import submodules.

85. **How do you handle exceptions in Python?**
    - Exceptions are handled using `try`, `except`, `else`, and `finally` blocks.
      ```python
      try:
          result = 1 / 0
      except ZeroDivisionError as e:
          print(f"Error: {e}")
      else:
          print("No exceptions")
      finally:
          print("Always executed")
      ```

86. **What are Python’s built-in functions?**
    - Built-in functions include `len()`, `type()`, `range()`, `print()`, `input()`, `sum()`, `min()`, `max()`, `map()`, `filter()`, `zip()`, etc.

87. **How do you generate random numbers in Python?**
    - Random numbers can be generated using the `random` module.
      ```python
      import random
      random_number = random.randint(1, 10)
      ```

88. **Explain the use of `yield` in Python.**
    - The `yield` keyword is used to create generators, which are iterators that return values one at a time, suspending and resuming their state between calls.
      ```python
      def my_generator():
          yield 1
          yield 2
          yield 3
      ```

89. **What is the purpose of the `global` keyword?**
    - The `global` keyword is used to declare that a variable inside a function is global (defined outside the function).
      ```python
      global_var = 0
      def modify_global():
          global global_var
          global_var += 1
      ```

90. **How do you work with binary data in Python?**
    - Binary data can be handled using the `struct` module and reading/writing binary files.
      ```python
      import struct
      data = struct.pack('i', 42)
      with open('binary_file', 'wb') as file:
          file.write(data)
      ```

### Code Examples

91. **How do you implement a linked list in Python?**
    - A linked list can be implemented using classes.
      ```python
      class Node:
          def __init__(self, data):
              self.data = data
              self.next = None
      class LinkedList:
          def __init__(self):
              self.head = None
          def append(self, data):
              new_node = Node(data)
              if not self.head:
                  self.head = new_node
              else:
                  current = self.head
                  while current.next:
                      current = current.next
                  current.next = new_node
          def display(self):
              current = self.head
              while current:
                  print(current.data, end=' ')
                  current = current.next
      ```

92. **How do you implement a stack in Python?**
    - A stack can be implemented using a list.
      ```python
      class Stack:
          def __init__(self):
              self.stack = []
          def push(self, data):
              self.stack.append(data)
          def pop(self):
              if not self.is_empty():
                  return self.stack.pop()
          def is_empty(self):
              return len(self.stack) == 0
      ```

93. **How do you implement a queue in Python?**
    - A queue can be implemented using `collections.deque`.
      ```python
      from collections import deque
      class Queue:
          def __init__(self):
              self.queue = deque()
          def enqueue(self, data):
              self.queue.append(data)
          def dequeue(self):
              if not self.is_empty():
                  return self.queue.popleft()
          def is_empty(self):
              return len(self.queue) == 0
      ```

94. **How do you implement a binary tree in Python?**
    - A binary tree can be implemented using classes.
      ```python
      class TreeNode:
          def __init__(self, data):
              self.data = data
              self.left = None
              self.right = None
      class BinaryTree:
          def __init__(self):
              self.root = None
          def insert(self, data):
              if not self.root:
                  self.root = TreeNode(data)
              else:
                  self._insert(data, self.root)
          def _insert(self, data, node):
              if data < node.data:
                  if node.left:
                      self._insert(data, node.left)
                  else:
                      node.left = TreeNode(data)
              else:
                  if node.right:
                      self._insert(data, node.right)
                  else:
                      node.right = TreeNode(data)
      ```

95. **How do you reverse a string in Python?**
    - A string can be reversed using slicing.
      ```python
      reversed_string = "hello"[::-1]
      ```

96. **How do you find the maximum value in a list in Python?**
    - The maximum value in a list can be found using the `max()` function.
      ```python
      max_value = max([1, 2, 3, 4, 5])
      ```

97. **How do you calculate the factorial of a number in Python?**
    - The factorial of a number can be calculated using recursion or a loop.
      ```python
      def factorial(n):
          if n == 0:
              return 1
          else:
              return n * factorial(n - 1)
      ```

98. **How do you check if a string is a palindrome in Python?**
    - A string can be checked for being a palindrome by comparing it to its reverse.
      ```python
      def is_palindrome(s):
          return s == s[::-1]
      ```

99. **How do you remove duplicates from a list in Python?**
    - Duplicates can be removed from a list using a set.
      ```python
      unique_list = list(set([1, 2, 2, 3, 4, 4, 5]))
      ```

100. **How do you sort a list in Python?**
    - A list can be sorted using the `sorted()` function or the `sort()` method.
      ```python
      sorted_list = sorted([3, 1, 4, 1, 5, 9])
      ```
