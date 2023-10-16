FROM python:3.10-bookworm

ENV REPOSITORY=IN_MEMORY

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT uvicorn app.main:app --host 0.0.0.0 --port 8000