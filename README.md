## This project was done with:

* Python 3.8.5
* Django 3.1.5
* Django Ninja 0.10.1
* Python Decouple 3.4

## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Create .env run contrib/env_gen.py
* Run the migrations.

```
git clone https://github.com/liviocunha/API-wholesale-footwear-catalog.git
cd API-wholesale-footwear-catalog
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 contrib/env_gen.py
python3 manage.py migrate
```
