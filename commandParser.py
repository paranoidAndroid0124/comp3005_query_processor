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

                table = tokens[from_index + 1]
                table = table.lower()
                self.commands[command_type](columns, table)
            else:
                print("Syntax error while using select")

        if command_type == "PROJECT":
            if "FROM" in tokens:
                from_index = tokens.index("FROM")
                columns = tokens[1:from_index]

                table = tokens[from_index + 1]
                table = table.lower()
                self.commands[command_type](columns, table)
            else:
                print("Syntax error while using project")

        if command_type == "JOIN":
            if len(tokens) == 3:
                table1 = tokens[1].lower()
                table2 = tokens[2].lower()

                if table1 in self.tables and table2 in self.tables:
                    result = self.commands[command_type](table1, table2)
                    print(result)
                else:
                    print("Error: one or both tables do not exist")
            else:
                print("Syntax error while joining")

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

    @staticmethod
    def projection(table, columns):
        """Select specific columns from the table"""
        seen = set()
        result = []

        for row in table:
            # Create a tuple with the values of the specified columns
            projected_row = tuple(row[col] for col in columns if col in row)

            # Check if this tuple is unique (not in seen set)
            if projected_row not in seen:
                seen.add(projected_row)  # Mark this tuple as seen

                # Convert the tuple back to a dictionary and add it to the result
                result.append({col: row[col] for col in columns if col in row})

        return result

    def handle_project(self, columns, table):
        if table in self.tables:
            if all(col in self.tables[table][0].keys() for col in columns):
                result = self.projection(self.tables[table], columns)
                print(result)
            else:
                print("invalid columns")
        else:
            print(f"No such table: {table}")

    @staticmethod
    def inner_join(table1, table2, join_column):
        """Perform an inner join between two tables on a specified column."""
        # Creating a dictionary for the second table keyed by the join column
        table2_dict = {row[join_column]: row for row in table2 if join_column in row}

        # Iterating over table1 and assembling the joined rows
        joined_table = []
        for row1 in table1:
            key = row1.get(join_column)
            if key in table2_dict:
                # Combine rows from both tables if the join column value matches
                joined_row = {**row1, **table2_dict[key]}
                joined_table.append(joined_row)

        return joined_table

    def handle_join(self, table1, table2):
        table1 = self.tables[table1]
        table2 = self.tables[table2]

        # Find a common column for joining
        common_columns = set(table1[0].keys()).intersection(table2[0].keys())
        if not common_columns:
            return "Error: No common columns found for JOIN operation"

        join_column = common_columns.pop()  # Using the first common column found
        return self.inner_join(table1, table2, join_column)

# Example Usage
# parser.parse("SELECT column1 column2 FROM table")
# parser.parse("PROJECT column3 FROM table")
# parser.parse("JOIN table1 table2")
