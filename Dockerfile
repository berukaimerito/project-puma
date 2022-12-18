# 
FROM python:3.10

# 
WORKDIR /DataAcquisitionService

# 
COPY ./requirements.txt /DataAcquisitionService/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /DataAcquisitionService/requirements.txt

# 
COPY ./DataAcquisitionService /DataAcquisitionService/app

# 
CMD ["python3 -m uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
