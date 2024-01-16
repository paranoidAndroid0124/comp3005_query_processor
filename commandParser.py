class CommandParser:
    def __init__(self):
        self.commands = {
            "SELECT": self.handle_select,
            "PROJECT": self.handle_project,
            "JOIN": self.handle_join
        }

    def parse(self, command):
        tokens = command.split()
        # convert input to upper case
        command_type = tokens[0].upper()
        if command_type in self.commands:
            self.commands[command_type](tokens[1:])
        else:
            print(f"Unknown command: {command_type}")

    def handle_select(self, args):
        # Handle SELECT command
        print(f"Handling SELECT with args: {args}")

    def handle_project(self, args):
        # Handle PROJECT command
        print(f"Handling PROJECT with args: {args}")

    def handle_join(self, args):
        # Handle JOIN command
        print(f"Handling JOIN with args: {args}")

# Example Usage
# parser.parse("SELECT column1, column2 FROM table")
# parser.parse("PROJECT column3")
# parser.parse("JOIN table1, table2")
