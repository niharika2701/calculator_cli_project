from src.calculator import Calculator


class CLI:
    
    def __init__(self):
        
        self.calc = Calculator()
        self.operations = {
            '1': ('Addition', self.calc.add),
            '2': ('Subtraction', self.calc.subtract),
            '3': ('Multiplication', self.calc.multiply),
            '4': ('Division', self.calc.divide),
        }
    
    def display_menu(self):
        
        print("\n=== Calculator ===")
        for key, (name, _) in self.operations.items():
            print(f"{key}. {name}")
        print("5. Exit")
    
    def get_numbers(self):
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numbers.")
            return None, None
    
    def run_once(self):
        
        self.display_menu()
        choice = input("Choose operation (1-5): ")
        
        if choice == '5':
            return False
        
        if choice not in self.operations:
            print("Invalid choice. Please try again.")
            return True
        
        a, b = self.get_numbers()
        if a is None or b is None:
            return True
        
        try:
            operation_name, operation_func = self.operations[choice]
            result = operation_func(a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        
        return True
    
    def run(self):
        
        print("Welcome to the Calculator!")
        
        while True:
            continue_running = self.run_once()
            if not continue_running:
                print("Goodbye!")
                break


def main():
    
    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main()