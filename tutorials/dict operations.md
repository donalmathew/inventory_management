Python dictionaries are versatile data structures that allow you to store and manipulate data in key-value pairs. Here’s an overview of the operations you can perform on dictionaries, as well as some commonly used methods.

## Operations on Dictionaries

### 1. **Creating a Dictionary**
You can create a dictionary using curly braces `{}` or the `dict()` function.

```python
# Using curly braces
my_dict = {"name": "Alice", "age": 25}

# Using dict() function
my_dict = dict([("name", "Alice"), ("age", 25)])
```

### 2. **Accessing Values**
You can access values by their keys using square brackets or the `get()` method.

```python
name = my_dict["name"]  # Accessing with brackets
age = my_dict.get("age")  # Accessing with get()
```

### 3. **Adding or Modifying Items**
You can add a new key-value pair or modify an existing one by assigning a value to a key.

```python
my_dict["favorite_color"] = "blue"  # Adding a new item
my_dict["age"] = 26  # Modifying an existing item
```

### 4. **Removing Items**
You can remove items using the `del` statement, `pop()`, or `popitem()` methods.

```python
del my_dict["favorite_color"]  # Remove an item by key
age = my_dict.pop("age")  # Remove and return the value of the specified key
key, value = my_dict.popitem()  # Remove and return the last inserted key-value pair
```

### 5. **Clearing All Items**
To remove all items from a dictionary, use the `clear()` method.

```python
my_dict.clear()  # Removes all items from the dictionary
```

### 6. **Checking for Key Existence**
You can check if a key exists in a dictionary using the `in` keyword.

```python
if "name" in my_dict:
    print("Name exists in the dictionary.")
```

### 7. **Iterating Through a Dictionary**
You can iterate over keys, values, or key-value pairs using loops.

```python
# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

### 8. **Getting Keys and Values**
You can retrieve all keys or values using the `keys()` and `values()` methods.

```python
keys = my_dict.keys()   # Returns a view of all keys
values = my_dict.values()  # Returns a view of all values
```

### 9. **Copying a Dictionary**
To create a shallow copy of a dictionary, use the `copy()` method.

```python
new_dict = my_dict.copy()  # Creates a copy of the original dictionary
```

### 10. **Updating a Dictionary**
You can update a dictionary with another dictionary's key-value pairs using the `update()` method.

```python
my_dict.update({"age": 30, "city": "New York"})  # Updates existing keys or adds new ones
```

### Summary of Common Dictionary Methods

| Method       | Description                                           |
|--------------|-------------------------------------------------------|
| `clear()`    | Removes all elements from the dictionary              |
| `copy()`     | Returns a shallow copy of the dictionary              |
| `get(key)`   | Returns the value for specified key                   |
| `items()`    | Returns a view of the dictionary's key-value pairs    |
| `keys()`     | Returns a view of all keys in the dictionary          |
| `pop(key)`   | Removes and returns the value for specified key       |
| `popitem()`  | Removes and returns the last inserted key-value pair  |
| `update()`   | Updates the dictionary with specified key-value pairs |
| `values()`   | Returns a view of all values in the dictionary        |

Dictionaries are powerful tools for data management in Python, allowing for efficient storage, retrieval, and manipulation of data through their flexible structure.

Citations:
[1] https://www.programiz.com/python-programming/dictionary
[2] https://www.w3schools.com/python/python_ref_dictionary.asp
[3] https://favtutor.com/blogs/python-dictionary
[4] https://docs.python.org/pt-br/3.13/tutorial/datastructures.html