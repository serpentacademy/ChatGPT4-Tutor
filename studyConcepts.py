import sqlite3
import pyperclip

# Connect to the SQLite database (assuming it's named 'concepts.db')
conn = sqlite3.connect('python_concepts.sqlite')
cursor = conn.cursor()

# Fetch all the concept names from the Concepts table
cursor.execute("SELECT name, simplified_description FROM Concepts")
concepts = cursor.fetchall()

# Interactively print each concept name
for concept in concepts:
    #print(concept[0])  # concept is a tuple, where the first item is the concept_name
    str_tutor = f"""
    CONTEXT: a)Define {concept[0]} in simple terms 33 words. 
    b)Give me the {concept[0]} core concept in 66 words 
    c)Give me a real use case example of {concept[0]} in Python with code 
    d) Ask me a question to continue the Python {concept[1]} Conversation, 
    using the Socratic Maieutics Dialogue

    """
    pyperclip.copy(str_tutor)

    print(str_tutor)
    user_input = input("Enter 1 to continue to the next concept: ")

    # Wait for user to enter '1' before proceeding
    while user_input != '1':
        user_input = input("Enter 1 to continue to the next concept: ")

# Close the database connection
conn.close()