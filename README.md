# PUMA
An application developed for getting live crypto data, save it to DB and feed RabbitMQ queues to run user created bots in  isolated trading simulation system

# First run this command
pip install -r requirements.txt

# Flask Back-End
by running command python3 -m uvicorn main:app --reload in your terminal inside /project-puma/DataAcquisitionService

# to run FLASK Back-End API
run command python3 app.py in /project-puma/api folder
