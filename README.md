# Python Sample Application

A simple Python application to learn and demonstrate basic Python programming concepts.

## 🚀 Features

- **Hello World Application**: Basic greeting functionality
- **Interactive Input**: User can input their name for personalized greetings
- **Error Handling**: Graceful handling of keyboard interrupts
- **Documentation**: Well-documented code with docstrings
- **Modular Design**: Clean, organized code structure

## 📁 Project Structure

```
python-sample-app/
├── README.md          # This file - project documentation
├── main.py            # Main Python application
├── requirements.txt   # Python dependencies
└── .gitignore        # Git ignore patterns
```

## 🛠️ Prerequisites

Before running this project, make sure you have:

- **Python 3.6+** installed on your system
- **pip** (Python package installer) available
- **Git** (optional, for version control)

### Checking Python Installation

Open your terminal/command prompt and run:

```bash
python --version
# or
python3 --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

## 🚀 Getting Started

### 1. Clone or Download the Project

```bash
# If using Git
git clone <repository-url>
cd python-sample-app

# Or simply download and extract the project files
```

### 2. Navigate to Project Directory

```bash
cd python-sample-app
```

### 3. Install Dependencies (Optional)

This project currently has no external dependencies, but if you add any:

```bash
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
```

### 4. Run the Application

#### Option 1: Direct Python Execution
```bash
python main.py
# or
python3 main.py
```

#### Option 2: Make it Executable (Unix/Linux/macOS)
```bash
chmod +x main.py
./main.py
```

#### Option 3: Using Python Module
```bash
python -m main
# or
python3 -m main
```

## 🎯 What the Application Does

1. **Displays Welcome Banner**: Shows a formatted header
2. **Default Greeting**: Prints "Hello, World! Welcome to Python programming!"
3. **Interactive Input**: Prompts user to enter their name
4. **Personalized Greeting**: Greets the user with their input name
5. **Completion Message**: Shows success message when finished

## 📝 Code Examples

### Basic Usage
```python
from main import greet_user

# Default greeting
message = greet_user()
print(message)  # Output: Hello, World! Welcome to Python programming!

# Personalized greeting
message = greet_user("Alice")
print(message)  # Output: Hello, Alice! Welcome to Python programming!
```

### Running Tests
```bash
# If you add pytest to requirements.txt
pytest

# Or run specific test file
python -m pytest test_main.py
```

## 🔧 Development

### Adding New Features
1. Create new functions in `main.py`
2. Update the `main()` function to call new features
3. Test your changes
4. Update this README if needed

### Code Style
This project follows PEP 8 Python style guidelines:
- Use 4 spaces for indentation
- Maximum line length of 79 characters
- Descriptive variable and function names
- Comprehensive docstrings

## 🐛 Troubleshooting

### Common Issues

**"python: command not found"**
- Ensure Python is installed and added to PATH
- Try using `python3` instead of `python`

**Permission Denied (Unix/Linux/macOS)**
- Make the file executable: `chmod +x main.py`

**Input/Output Error**
- Ensure you're running in a terminal that supports input
- Some IDEs may not support interactive input

### Getting Help
- Check Python version compatibility
- Verify file permissions
- Ensure you're in the correct directory

## 📚 Learning Resources

- [Python Official Documentation](https://docs.python.org/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Real Python Tutorials](https://realpython.com/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:
- Check the troubleshooting section above
- Review the code comments
- Open an issue in the repository

---

**Happy Python Programming! 🐍✨**
