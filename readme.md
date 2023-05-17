1. To run this App, you need to install Python 3.10.1
2. Please install virtual environment on this folder by using this command : on windows " py -m venv env " and for mac, use this command " python3 -m venv env " 
3. After that, activate on this folder by using this command : on windows " source env/Scripts/activate " and for mac, use this command " source env/bin/activate "
4. Install required libraries by using this commmand : " pip install -r requirements.txt "
5. Setup your environment by exporting all required environment. For example, open file ".env.example"
6. After that, you can migrate the tables, step by step using these commands : "flask db init" -> "flask db migrate" -> "flask db upgrade"
7. To run this app, you can start flask by using this command : " flask run "