# Create our image based on Python 3.8
FROM python:3.8

# Expose ports
EXPOSE 5000

# Tell Python to not generate .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Turn off buffering
ENV PYTHONUNBUFFERED 1

# Install requirements using pip
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

# Set working directory and addour Flask API files
WORKDIR /app
ADD . /app
ARG FLASK_APP=app
CMD ["python","-m","flask", "run","--host", "0.0.0.0","--port","5000"]

#CMD ["gunicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
