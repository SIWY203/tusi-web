if ! command -v py &> /dev/null && ! command -v python &> /dev/null
then
    echo "Python is not installed. Please install Python 3.x from https://www.python.org/downloads/"
    exit 1
fi

py -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
cd tusi-web
py manage.py runserver
