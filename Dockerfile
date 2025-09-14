FROM python:3.11-alpine

RUN apk update && \
    apk add --no-cache xdg-utils

RUN python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
