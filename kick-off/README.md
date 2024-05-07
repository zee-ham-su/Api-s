# FastAPI Tutorial

## setup

setting up your virtual environment

```bash
python -m venv venv
.\env\Scripts\activate
pip install -r requirements.txt
```

If you're running Linux or MacOS you'll instead run

```bash
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

## Running the app

`uvicorn main:app --reload`
