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


def enumerate_available_tables(available_tables):
    print("\nAvailable tables:")
    for index, table_name in enumerate(available_tables, start=1):
        print(f"{index}. {table_name}")


def main():
    print("""
        __ _   _   _    ___   _ __   _   _                     
       / _` | | | | |  / _ \ | '__| | | | |                    
      | (_| | | |_| | |  __/ | |    | |_| |                    
       \__, |  \__,_|  \___| |_|     \__, |                    
       _ _|_|  _ __    ___     ___   |___/  ___    ___    _ __ 
      | '_ \  | '__|  / _ \   / __|  / _ \ / __|  / _ \  | '__|
      | |_) | | |    | (_) | | (__  |  __/ \__ \ | (_) | | |   
      | .__/  |_|     \___/   \___|  \___| |___/  \___/  |_|   
      |_|  
    """)

    file_name = 'data.json'

    with open(file_name, 'r') as file:
        data = json.load(file)

    # Dynamically create the table dictionary
    tables = {key: value for key, value in data.items()}

    # Create list of available tables
    available_tables = list(tables.keys())

    while True:
        command = input("Enter query:")
        if command.lower() == 'exit':
            break
        # parse_command(command)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
