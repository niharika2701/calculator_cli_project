# Calculator Project

A professional command-line calculator built with Python, following TDD (Test-Driven Development) and software engineering best practices such as AAA (Arrange-Act-Assert) and DRY (Don't-Repeat-Yourself) principles.

## Features

- **Basic arithmetic operations**: Addition, subtraction, multiplication, division
- **Interactive command-line interface**: User-friendly menu-driven interface
- **100% test coverage**: Comprehensive test suite with unit and parameterized tests
- **Clean, well-documented code**: Following PEP 8 and professional standards
- **Error handling**: Graceful handling of invalid inputs and division by zero

## Technologies Used

- Python 3.9+
- pytest (testing framework)
- pytest-cov (test coverage)
- Git (version control)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/calculator_project.git
cd calculator_project
```

### 2. Create and activate virtual environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running the Calculator
```bash
python -m src.cli
```

### Example Session
```
Welcome to the Calculator!

=== Calculator ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose operation (1-5): 1
Enter first number: 10
Enter second number: 5
Result: 15.0
```

## Running Tests

### Run all tests
```bash
pytest tests/
```

### Run tests with verbose output
```bash
pytest tests/ -v
```

### Run tests with coverage report
```bash
pytest tests/ --cov=src --cov-report=html --cov-report=term
```

### View HTML coverage report
```bash
open htmlcov/index.html
```

## Project Structure
```
calculator_project/
├── src/
│   ├── __init__.py
│   ├── calculator.py       # Core calculator logic
│   └── cli.py             # Command-line interface
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py # Calculator unit tests
│   └── test_cli.py        # CLI tests
├── venv/                  # Virtual environment (not in git)
├── htmlcov/               # Coverage reports (not in git)
├── .gitignore            # Git ignore file
├── .coveragerc           # Coverage configuration
├── README.md             # This file
└── requirements.txt      # Project dependencies
```

## Development Principles

This project follows industry best practices:

- **TDD (Test-Driven Development)**: Tests written before implementation
- **DRY (Don't Repeat Yourself)**: Parameterized tests to avoid code duplication
- **AAA Pattern**: Arrange-Act-Assert structure in all tests
- **Clean Code**: Well-structured, readable, and documented code
- **Version Control**: Meaningful git commits throughout development
- **100% Test Coverage**: Full confidence in code quality

## Testing Strategy

### Unit Tests
- Individual test methods for each calculator operation
- Edge cases (negative numbers, zeros, mixed signs)
- Error handling (division by zero)

### Parameterized Tests
- Uses `@pytest.mark.parametrize` for DRY testing
- Multiple test cases per operation
- Comprehensive input validation

### Test Coverage
- 100% code coverage achieved
- All functions and edge cases tested
- Coverage reports available in `htmlcov/`

## Git Workflow

This project uses meaningful commit messages following best practices:
```bash
# Example commits
git commit -m "Add Calculator.add() method with test"
git commit -m "Refactor tests to use parameterization (DRY)"
git commit -m "Add interactive CLI with tests"
```

## Future Enhancements

Potential features for future development:

- [ ] Additional operations (power, square root, modulo)
- [ ] Command-line arguments support
- [ ] Calculation history
- [ ] GUI interface
- [ ] Scientific calculator mode
- [ ] Unit conversions

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests for your changes
4. Implement your changes
5. Ensure all tests pass (`pytest tests/`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Requirements

- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment support

## Dependencies

See `requirements.txt` for full list:

- pytest>=7.4.0
- pytest-cov>=4.1.0

## License

This project is created for educational purposes as part of IS 601 - Python for Web API course at NJIT.

## Author

**Niharika Jadhav**
- Course: IS 601 - Python for Web API
- Institution: New Jersey Institute of Technology (NJIT)
- Semester: [Spring2026]

## Acknowledgments

- Built following TDD, AAA, DRY and other software engineering best practices
- Inspired by professional Python development standards
- Created as part of NJIT IS 601 coursework