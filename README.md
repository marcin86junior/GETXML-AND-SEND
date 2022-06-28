PackageSearchEngineREST
=======================

![alt text](http://marcin86.pythonanywhere.com/static/PythonSearchREST.JPG)

Overview
--------

PackageSearchEngineREST is an open-source website for checking new python package. 
Django/REST technology is used for searching in database. 

Requirements:
-------------

	Python 3.8.x (3.9.1 working in Docker)
	Django 3.2.12
	Djangorestframework 3.13.x

Installation:
-------------


	Create new folder "PackageSearchEngineREST" and open it:
	git clone https://github.com/marcin86junior/PackageSearchEngineREST.git .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	cd django_rest_imageupload_backend\
	python manage.py migrate
	python manage.py makemigrations
	python manage.py migrate	
	python .\manage.py runserver
	http://127.0.0.1:8000/
	*python manage.py createsuperuser (marcin/123)


Testing:
--------

	python manage.py test
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test
	coverage report (or) coverage html


Docker:
-------

	Create new folder "MegaPictureUploadREST" and open it:
	git clone https://github.com/marcin86junior/MegaPictureUploadREST.git .
	cd django_rest_imageupload_backend\
	"Open Doker Desktop"
	format file in \django_rest_imageupload_backend\docker-entrypoint.sh    CRLF->LF
	docker-compose up
	http://127.0.0.1:8000/api/
	Test:
	docker-compose run web python3 manage.py test


Fixtures
--------


	Data included in fixtures:

	User / Password / Assigned group / Added pictures to model
	b1 / 123 / Basic / 2
	p2 / 123 / Premium / 2
	e3 / 123 / Enterprice/ 2 
	c4 / 123 / Custom/ 2


Issues
------


	At the moment there are few issuse:

	- In enterprise and custom group we don't have expire tokens yet. We can check only
	  expire date / created date. This function will be added shortly.
	- docker have differnt main PATH (/code/) - should be corrected in web: / media
	- docker should have migrations in entrypoint.sh (almost fixed)
	- missing some view test (low coverage)

	Function in the dev/testing phase - token generator:

	http://127.0.0.1:8000/obtain-token/
	log-in: b1 / pass: 123
	-> create token
	http://127.0.0.1:8000/custom-url/login/
	log-in: b1 / pass: 123
	-> POST
	We have: list of tokens of user b1