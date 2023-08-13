FROM python:3-alpine3.18



WORKDIR /app
COPY . .

COPY requirement.txt .

RUN pip install -r requirement.txt
EXPOSE 5000
CMD ["python", "app.py"]
