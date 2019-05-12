#pull official base image
FROM python:3

#set envionment variables
ENV PYTHONUNBUFFERED 1

#run this before copying requirements
RUN pip install --upgrade pip

#set work directory
WORKDIR /ToDoApp

# Adding requirements file
COPY requirements.txt .

#install dependencies
RUN pip install pipenv
RUN pip install -r requirements.txt

COPY . .

#CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
