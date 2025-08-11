#!/usr/bin/env python3
"""
Python Sample Application - Hello World
A simple Python application to demonstrate basic Python programming concepts.
"""

def greet_user(name="World"):
    """
    Greet a user with a personalized message.
    
    Args:
        name (str): The name of the person to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome to Python programming!"

def main():
    """Main function to run the application."""
    print("=" * 50)
    print("Python Sample Application")
    print("=" * 50)
    
    # Basic greeting
    print(greet_user())
    print()
    
    # Interactive greeting
    try:
        user_name = input("Enter your name (or press Enter for default): ").strip()
        if user_name:
            print(greet_user(user_name))
        else:
            print(greet_user())
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        return
    
    print("\n" + "=" * 50)
    print("Application completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main() 