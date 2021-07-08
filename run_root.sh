source venv/bin/activate
pip install flask
pip install -e .
export FLASK_RUN_PORT=80
export FLASK_APP=handslap
export FLASK_ENV=development
flask run
