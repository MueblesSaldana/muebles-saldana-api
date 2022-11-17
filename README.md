# muebleria-saldana-api

Install Virtual Enviroment 
python -m venv venv 

Inicialize VENV
venv\Scrips\activate.bat 

Install requirements
pip install -r requirements.txt

Inicialize API 
uvicorn app.main:app --reload
