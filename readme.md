# Bank security console
This is an internal repository for  the employees of the bank "Siianie". If you got to this repository by accident, then you will not be able to run it, since you have not access to DB, bot you can still use layout code or learn out how are DB queries realized.
Security console is a site with possibilities to connect to remote DB of our employees visits and passcards.

## How to install
- Python3 is needed to be installed
- Create your virtual environment to isolate your project:
```
python3 virtualenv yourenv
source yourenv/bin/activate
```
- Use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install - r requirements.txt 
```
- Create db_settings.env named file and store there all secret configurations for ensure your data security:
```
SECRET_KEY=yoursecretkey
ALLOWED-HOSTS=localhost
DATABASE_URL in the following format: ENGINE://USER:PASSWORD@HOST:PORT/NAME 
```



## How to use
Use command ```python3 manage.py runserver``` than click on given link in the terminal, you will be redirected to web browser.
