FROM python:3.13.0a4-alpine3.18

WORKDIR /app
COPY . /app
COPY requirement.txt .
RUN pip install -r ./requirement.txt
CMD ["python","./src/app.py"]
