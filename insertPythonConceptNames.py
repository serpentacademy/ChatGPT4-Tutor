import sqlite3

# Core concepts related to Python's primary data types
core_concepts = [
    "int",
    "float",
    "complex",
    "str",
    "list",
    "tuple",
    "set",
    "dict",
    "bool",
    "bytes",
    "bytearray",
    "memoryview",
    "range",
    "frozenset"
]

# Connect to the SQLite database (this will create a new file 'concepts.db')
conn = sqlite3.connect('python_concepts.sqlite')
cursor = conn.cursor()



# Insert the core concepts into the Concepts table
for concept in core_concepts:
    try:
        cursor.execute("INSERT INTO Concepts (name) VALUES (?)", (concept,))
    except sqlite3.IntegrityError:
        # This will handle the case where a concept is already in the table due to the UNIQUE constraint
        print(f"'{concept}' is already in the database.")

# Commit the changes
conn.commit()

# Close the database connection
conn.close()

print("Concepts have been inserted into the SQLite database!")
