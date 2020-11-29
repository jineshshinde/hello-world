FROM python:3

WORKDIR /usr/src/app

# COPY requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python test_hello.py

CMD ["python","hello_world.py"]
