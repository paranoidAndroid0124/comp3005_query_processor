import json
from commandParser import CommandParser





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

    # call parser constructor
    parser = CommandParser(data)

    while True:
        command = input("Enter query:")
        if command.lower() == 'exit':
            break
        parser.parse(command)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
