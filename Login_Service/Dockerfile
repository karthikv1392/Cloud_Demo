FROM python:3.7

COPY app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8895

CMD [ "python", "./app.py" ]