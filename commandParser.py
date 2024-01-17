class CommandParser:
    def __init__(self, data):
        # Dynamically create the table dictionary
        self.tables = {key: value for key, value in data.items()}
        self.commands = {
            "SELECT": self.handle_select,
            "PROJECT": self.handle_project,
            "JOIN": self.handle_join
        }

    def parse(self, command):
        # Convert command to upper case
        tokens = command.split()
        command_type = tokens[0].upper()

        if command_type == "SELECT":
            if "FROM" in tokens:
                from_index = tokens.index("FROM")
                columns = tokens[1:from_index]

                table = tokens[from_index+1]
                table = table.lower()
                self.commands[command_type](columns, table)
            else:
                print("Syntax error while using select")

    @staticmethod
    def selection(table, columns):
        """Select rows where column equals value"""
        return [{col: row.get(col, None) for col in columns} for row in table]

    def handle_select(self, columns, table):
        if table in self.tables:
            if all(col in self.tables[table][0].keys() for col in columns):
                result = self.selection(self.tables[table], columns)
                print(result)
            else:
                print("invalid columns")
        else:
            print(f"No such table: {table}")

    def handle_project(self, args):
        # Handle PROJECT command
        print(f"Handling PROJECT with args: {args}")

    def handle_join(self, args):
        # Handle JOIN command
        print(f"Handling JOIN with args: {args}")


# Example Usage
# parser.parse("SELECT column1 column2 FROM table")
# parser.parse("PROJECT column3")
# parser.parse("JOIN table1, table2")
