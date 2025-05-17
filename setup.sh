py -m venv .venv
source .venv/Scripts/activate
pip install -r tusi-web/requirements.txt
cd tusi-web
py manage.py runserver
