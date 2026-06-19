
## Exercise 11.2

### Framework

_Selenium_


### Installation Steps

```bash
pip install -r frontend/e2e/selenium/requirements.txt
```


### Application startup

Start the devcontainer then execute the following commands:

```bash
export DATABASE_URL="sqlite:///./test_db.sqlite"
uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload

cd frontend
npm run dev
```


### Test command

```bash
# Outside the devcontainer execute one of the following commands
pytest frontend/e2e/selenium/test_messages_quiz.py
pytest frontend/e2e/selenium/test_messages_quiz.py -v -s
```