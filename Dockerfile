FROM python:3-alpine3.18

WORKDIR /app

# COPY src /app
# COPY requirement.txt .

# RUN pip install -r requirement.txt
# EXPOSE 5000
# CMD python ./app.py
EXPOSE 5000

COPY requirement.txt ./
RUN pip install -r requirement.txt

COPY src /app/
CMD ["python", "app.py"]
