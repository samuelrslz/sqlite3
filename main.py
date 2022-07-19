import sqlite3

# Connect to the database
connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()

# Create table (if it does not already exist)
cursor.execute("DROP TABLE IF EXISTS people") # --- In case that I need to delete that table.
cursor.execute("DROP TABLE IF EXISTS countries")

# Create one table for people and one for countries
cursor.execute("CREATE TABLE IF NOT EXISTS people (fname TEXT, lname TEXT, gender TEXT, age REAL, type_of_relation TEXT, country TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS countries (country_name TEXT, demonym TEXT, population REAL)")

# Insert some data into countries
cursor.execute("INSERT INTO countries VALUES \
                ('USA', 'American', '329.5'), \
                ('Mexico', 'Mexican', '128.9'), \
                ('El Salvador', 'Salvadoran', '6.5'), \
                ('Guatemala', 'Guatemalan', '16.9')")

def get_name(cursor):
    # function used later when deleting someone from the table
    cursor.execute("SELECT fname FROM people")
    results = cursor.fetchall()
    if len(results) == 0:
        print("No names in database")
        return None
    for i in range(len(results)):
        print(f"{i+1} - {results[i][0]}")
    choice = 0
    while choice < 1 or choice > len(results):
        choice = int(input("Name ID: "))
    return results[choice-1][0]


choice = None
while choice != "6":
    print("1) Display People")
    print("2) Add People")
    print("3) Update a Person's Type of Relationship")
    print("4) Delete a Person")
    print("5) Add Country")
    print("6) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Display Persons
        cursor.execute("SELECT fname, lname, gender, age, type_of_relation, country, demonym, population \
                        FROM people \
                        INNER JOIN countries ON people.country = countries.country_name \
                        ORDER BY lname DESC")   # Performs a join so you can see the country of the person too
        print("{:>10}  {:>10}  {:>10}  {:>10}  {:>17}  {:>13}  {:>14}  {:>14}".format("First Name", "Last Name", "Gender", "Age", "Relationship", "Country", "Demonym", "Population"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}  {:>10}  {:>10}  {:>17}  {:>13}  {:>14}  {:>14}".format(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))
    elif choice == "2":
        # Add People
        try:
            fname = input("First Name: ")
            lname = input("Last Name: ")
            gender = input("Gender: ")
            age = input("Age: ")
            type_of_relation = input("Type of Relationship: ")
            country = input("Country: ")
            values = (fname, lname, gender, age, type_of_relation, country)
            cursor.execute("INSERT INTO people VALUES (?,?,?,?,?,?)", values)
            connection.commit()
        except ValueError:
            print("Invalid pay!")
    elif choice == "3":
        # Update type of relationship
        try:
            fname = input("First Name: ")
            type_of_relation = input("Type of Relationship: ")
            values = (type_of_relation, fname) # Make sure order is correct
            cursor.execute("UPDATE people SET type_of_relation = ? WHERE fname = ?", values)
            connection.commit()
            if cursor.rowcount == 0:
                print("Invalid name!")
        except ValueError:
            print("Invalid pay!")
    elif choice == "4":
        # Delete person
        name = get_name(cursor)
        if name == None:
            continue
        values = (name, )
        cursor.execute("DELETE FROM people WHERE fname = ?", values)
        connection.commit()
    elif choice == "5":
        # Adds a new country to the country table
        country = input("Country Name: ")
        demonym = input("Demonym: ")
        population = input("Population (in Millions): ")
        values = (country, demonym, population)
        cursor.execute("INSERT INTO countries VALUES (?,?,?)", values)
    print()

# Close the database connection before exiting
connection.close()


