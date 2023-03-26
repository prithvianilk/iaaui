FROM python:3.9
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3", "/app/app.py" ]