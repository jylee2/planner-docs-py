# Planner API

- CRUD for docs

## To Run:

- Install virtualenv
  `pip install virtualenv`
- Create the virtual environment named "env":
  `virtualenv venv` or `python -m venv env` for windows (cmd as admin)
- Add the path to the git ignore file (optional):
  `echo env/ >> .gitignore`
- Activate the virtual env:
  `source env/Scripts/activate` or `.\env\Scripts\activate` for windows
- Install dependencies:
  `pip install pymongo pymongo[srv] fastapi uvicorn python-dotenv`
- Run:
  `uvicorn index:app --reload` or `python -m uvicorn index:app --reload` for windows
- If you encounter `NameError: name 'sys' is not defined` in windows, try:
  `pip install pymongo[srv]`
