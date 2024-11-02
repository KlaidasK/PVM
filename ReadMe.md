# Python 3.13.0 Version Setup

### Required:
- Python 3.13.0 must be installed on your computer. You can download it from the official Python website.

### Setup Instructions:

```bash
pip install pipenv
pipenv install
pipenv install django
pipenv shell  # Enter virtual environment
python -c "import django; print(django.get_version())"  # Check if Django is installed
