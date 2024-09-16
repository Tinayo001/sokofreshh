#!/usr/bin/env python3

from app import create_app

"""
This script sets up and runs the Flask application.

Key components:
1. Import the create_app function from the app module
2. Call create_app() to initialize the Flask application
3. Check if this script is being run directly (not imported)
4. If so, run the application in debug mode
"""

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    """
    This block runs when the script is executed directly (not imported).
    It sets up the application and starts running it.
    """
    # Run the application in debug mode
    app.run(debug=True)

