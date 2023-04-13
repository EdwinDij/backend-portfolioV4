FROM python:3-slim-buster
WORKDIR /backend
COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
