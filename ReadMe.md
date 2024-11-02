# Setup

### Required:
- Python 3.13.0 must be installed on your computer. You can download it from the official Python website.

### Setup Instructions:

1. Open Command Prompt (CMD).
2. Navigate to the directory where you've downloaded the project with GitHub Desktop. 
   ```bash
   cd path\to\your\project\directory
   ```

3. Run the following commands to set up the environment:

   ```bash
   pip install pipenv
   pipenv install
   pipenv install django
   pipenv shell  # Enter virtual environment
   python -c "import django; print(django.get_version())"  # Check if Django is installed
   ```

This will set up the project with Django in a virtual environment.

4. **When using Visual Studio Code**:
   - Open a new terminal within VS Code.
   - Run the command:
     ```bash
     pipenv shell  # Enter virtual environment
     ```
     
   - Then start the Django server with:
     ```bash
     python manage.py runserver
     ```

This will set up the project with Django in a virtual environment and start the development server.
### Technology Stack
- Web Framework: Django
- Database: PostgreSQL or SQLite
