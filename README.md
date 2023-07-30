# Main Sources
 *  Twilio: https://console.twilio.com/?frameUrl=/console
 *  Docs: https://www.twilio.com/docs/verify/api

# Features
 * Development, Staging, Production environments are supported -> https://django-configurations.readthedocs.io/en/stable/
 * 

# How to Install
 * git clone
 * cp .env.example .env
 * python3 -m pip install --user --upgrade pip
 * python3 -m pip install --user virtualenv
 * python3 -m venv env
 * source env/bin/activate
 * which python
 * pip install -r requirements.txt
 * python3 manage.py makemigrations
 * python3 manage.py migrate
 * python3 manage.py createsuperuser
 * python3 manage.py runserver

# How to Test
 * Option 1 -> python3 manage.py test
 * Option 2 -> A sample POSTMAN collection is provided in the root folder
 * Option 3 -> DRF browsable API is enabled
 * Option 4 -> Django Admin is enabled
 * Option 5 -> Frontend is enabled
   * /register, /login, /logout, /verify