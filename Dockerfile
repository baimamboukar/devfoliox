FROM python:latest

WORKDIR /

COPY / ./app
COPY requirements.txt ./app
COPY app.py ./app
COPY gunicorn.conf.py ./app
RUN pip install -r /app/requirements.txt

# Set the FLASK_APP environment variable
ENV FLASK_APP=/app/app.py
RUN set FLASK_APP=/app/app.py

# Expose the Flask port (default is 5000)
EXPOSE 5000

# Define the command to run your application
CMD ["flask", "run", "--host=0.0.0.0"]