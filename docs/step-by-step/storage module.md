# Design Document: Storage Module for Plagiarism Detection Project

**Author**: Rajat Roy  
**Date**: 18th oct 24  
**Purpose**: Provide clear instructions to implement the storage module for managing assignment data using Python and SQLite.

---

## 1. **Overview**
The storage module will handle the storage and retrieval of assignment submissions in the plagiarism detection project. This includes creating a database for storing metadata related to the uploaded files, as well as functions to insert and retrieve records.

**Tools & Frameworks**:
- **Python (sqlite3)**: To manage SQLite databases.
- **SQLite**: A lightweight, serverless database used for local storage.

---

## 2. **Functional Requirements**

### 2.1 Database Setup
We will use SQLite to store assignment information in a local database called `assignments.db`.

- **Database Name**: `assignments.db`
- **Table**: `assignments`
  - **Columns**:
    - `id`: INTEGER (Primary Key)
    - `roll_no`: TEXT (Student Roll Number)
    - `class`: TEXT (Class Name)
    - `filename`: TEXT (Name of the uploaded assignment file)
    - `filepath`: TEXT (Full path to the file location)

### 2.2 Functionality

#### 2.2.1 Store Assignment Function
A function to insert assignment details into the database.

- **Function Name**: `store_assignment`
- **Parameters**:
  - `roll_no`: Roll number of the student (string)
  - `class_name`: Class to which the student belongs (string)
  - `filename`: Name of the assignment file (string)
  - `filepath`: Full path to where the file is stored (string)
  
- **Behavior**:
  - Opens a connection to the `assignments.db` database.
  - Inserts the provided data into the `assignments` table.
  - Closes the connection.

#### 2.2.2 Retrieve Assignments Function
A function to retrieve assignment details based on class and roll number.

- **Function Name**: `get_assignments`
- **Parameters**:
  - `class_name`: Class to search for (string)
  - `roll_no`: Roll number to search for (string)
  
- **Behavior**:
  - Opens a connection to the `assignments.db` database.
  - Queries the `assignments` table for records matching the given class and roll number.
  - Returns all matching assignments.
  - Closes the connection.

---

## 3. **Code Implementation**

### 3.1 **Database and Table Creation**
The database and the `assignments` table should be created when the system initializes.

```python
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('assignments.db')
cursor = conn.cursor()

# Create a table for storing assignments
cursor.execute('''
CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY,
    roll_no TEXT NOT NULL,
    class TEXT NOT NULL,
    filename TEXT NOT NULL,
    filepath TEXT NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
```

### 3.2 **Store Assignment Function**

```python
def store_assignment(roll_no, class_name, filename, filepath):
    conn = sqlite3.connect('assignments.db')
    cursor = conn.cursor()
    
    # Insert assignment details into the table
    cursor.execute('''
    INSERT INTO assignments (roll_no, class, filename, filepath) 
    VALUES (?, ?, ?, ?)
    ''', (roll_no, class_name, filename, filepath))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
```

### 3.3 **Retrieve Assignments Function**

```python
def get_assignments(class_name, roll_no):
    conn = sqlite3.connect('assignments.db')
    cursor = conn.cursor()
    
    # Fetch assignments based on class and roll number
    cursor.execute('''
    SELECT * FROM assignments WHERE class = ? AND roll_no = ?
    ''', (class_name, roll_no))
    
    assignments = cursor.fetchall()
    
    conn.close()
    return assignments
```

---

## 4. **Example Usage**

### 4.1 **Storing an Assignment**
The following example shows how to store assignment details in the database.

```python
store_assignment('12345', '10A', 'assignment1.pdf', '/path/to/assignment1.pdf')
```

### 4.2 **Retrieving Assignments**
Retrieve assignments for a specific student using class and roll number.

```python
assignments = get_assignments('10A', '12345')
for assignment in assignments:
    print(assignment)
```

---

## 5. **Design Considerations**

- **Error Handling**: Future implementations should include error handling for database operations, ensuring the system can handle unexpected failures (e.g., database connection issues).
- **File Paths**: Ensure the file path management is consistent and follows best practices for handling file I/O.
- **Testing**: Verify the correct functionality of each method with unit tests to ensure data integrity during insertions and retrievals.

---

## 6. **Next Steps**
1. Implement these functions in the relevant module of the plagiarism detection system.
2. Write unit tests to validate database operations.
3. Once implemented, integrate this module with the other components (retrieval, pre-processing, and plagiarism detection).

---

## 7. **Conclusion**
By following this document, you'll be able to set up and manage the assignment storage for the project. If you have any questions during the implementation, feel free to reach out.

