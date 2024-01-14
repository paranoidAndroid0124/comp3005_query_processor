import json


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
    file_name = 'data.json'

    with open(file_name, 'r') as file:
        data = json.load(file)

    # Dynamically create the table dictionary
    tables = {key: value for key, value in data.items()}

    while True:
        print("\nRelax-like Command Line App")
        print("1. Selection")
        print("2. Projection")
        print("3. Join")
        print("4. exit")
        choice = input("Choose an operation: ")

        if choice == '1':
            """Select"""

            # display available tables
            available_tables = list(tables.keys())
            print("\nAvailable tables:")
            for index, table_name in enumerate(available_tables, start=1):
                print(f"{index}. {table_name}")

            # parse user table selection
            table_index = input("Enter the number of the table for selection: ")
            table_index = int(table_index) - 1
            select_table = available_tables[table_index]
            table = tables[select_table]

            # display available columns
            available_col = list(table[0].keys())
            print("\nAvailable columns:")
            for index, column_name in enumerate(available_col, start=1):
                print(f"{index}. {column_name}")

            # parse user column selection
            column_index = input("Enter the number of the column for selection: ")
            column_index = int(column_index) - 1
            col = available_col[column_index]

            # display available values
            unique_values = set(row[col] for row in table)
            available_values = list(unique_values)
            print("\nAvailable values:")
            for index, value_name in enumerate(available_values, start=1):
                print(f"{index}. {value_name}")
            
            # parse value selection
            value_index = input("Enter value for selection: ")
            value_index = int(value_index)-1
            val = available_values[value_index]

            result = selection(table, col, val)
            print("Result:", result)

        elif choice == '2':
            """Projection"""
            # display available tables
            available_tables = list(tables.keys())
            print("\nAvailable tables:")
            for index, table_name in enumerate(available_tables, start=1):
                print(f"{index}. {table_name}")

            # parse user table selection
            table_index = input("Enter the number of the table for selection: ")
            table_index = int(table_index) - 1
            select_table = available_tables[table_index]
            table = tables[select_table]

            # display available columns
            available_col = list(table[0].keys())
            print("\nAvailable columns:")
            for column_name in enumerate(available_col, start=1):
                print(column_name[1])

            cols = input("\nEnter columns for projection (comma-separated): ").split(',')
            cols = [col.strip() for col in cols]
            result = projection(table, cols)
            print("Result:", result)

        elif choice == '3':
            """Join"""
            join_col = input("Enter the column to join on: ")
            result = join(tables[0], tables[1], join_col)
            print("Result", result)

        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
