student = [
    {"id": 1, "name": "Alice", "age": 30, "major": "Computer Science"},
    {"id": 2, "name": "Bob", "age": 25, "major": "Pysics"},
    {"id": 3, "name": "Charlie", "age": 35, "major": "Mathematics"}
]

courses = [
    {"courseID": "C101", "CourseName": "Databases", "Professor": "Dr.Smith"},
    {"courseID": "C102", "CourseName": "Quantum Pysics", "Professor": "Dr.Doe"},
    {"courseID": "C103", "CourseName": "Calculus", "Professor": "Dr.White"}
]


def selection(table, column, value):
    """Select rows where column equals value"""
    return [row for row in table if row[column] == value]


def projection(table, columns):
    """Select specific columns from the table"""
    return [{col: row[col] for col in columns} for row in table]


def join(table1, table2, join_column):
    """Perform inner join on the join_column"""
    join_data = []
    for row1 in table1:
        for row2 in table2:
            if row1[join_column] == row2[join_column]:
                "Append unpacked key value pair"
                join_data.append(**row1, **row2)
    return join_data


def main():
    # Map table names to data arrays
    tables = {
        'student': student,
        'courses': courses
    }

    while True:
        print("\nRelax-like Command Line App")
        print("1. Selection")
        print("2. Projection")
        print("3. Join")
        print("4. exit")
        choice = input("Choose an operation: ")

        available_tables = ', '.join(tables.keys())

        if choice == '1':
            """Select"""
            print(f"Available tables: {available_tables}")
            table_name = input("Enter table for selection ")
            if table_name not in tables:
                print("Failed to find table")
                return

            table = tables[table_name]
            print("Available columns:", ', '.join(table[0].keys()))
            col = input("Enter column for selection: ")

            unique_values = set(row[col] for row in table)
            print("Available values in column '{}': {}".format(col, ', '.join(map(str, unique_values))))
            val = input("Enter value for selection: ")


            result = selection(table, col, val)
            print("Result:", result)

        elif choice == '2':
            """Projection"""
            print(f"Available tables: {available_tables}")
            table = input("Enter table for selection ")
            if table not in tables:
                print("Failed to find table")
                return

            cols = input("Enter columns for projection (comma-separated): ").split(',')
            cols = [col.strip() for col in cols]
            result = projection(table, cols)
            print("Result:", result)

        elif choice == '3':
            """Join"""
            join_col = input("Enter the column to join on: ")
            result = join(student, courses, join_col)
            print("Result", result)

        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
