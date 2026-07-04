import sqlite3

def secure_database_query(user_input_id):
    print("Simulating Secure Database Transaction against SQLi...")
    
    # Create an in-memory database for testing
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INT, username TEXT, role TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'maryam_admin', 'Administrator')")
    
    # SECURE WAY: Using Parameterized Queries (Industry Standard Hardening)
    secure_query = "SELECT * FROM users WHERE id = ?"
    
    cursor.execute(secure_query, (user_input_id,))
    result = cursor.fetchone()
    
    if result:
        print(f"PASSED: Securely fetched user: {result[1]} without exposing database layers.")
    else:
        print("No user found with secure validation.")
        
    conn.close()

if __name__ == "__main__":
    secure_database_query(1)
