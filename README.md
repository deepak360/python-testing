# python-testing
This repo demonstrate how to test application with pytest a python testing library with multiple examples.

# How to run flask app.
`
python3 -m venv env
source /env/bin/activate
pip3 install -r requirements.txt
flask shell
from app import db
db.create_all()
exit()
flask run
`


# How to Run all test cases.

`pytest`

OR

`PYTHONPATH=. pytest`

OR

`PYTHONPATH=. pytest -v`
