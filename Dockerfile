#pull official base image
FROM python:3

#set envionment variables
ENV PYTHONUNBUFFERED 1
#
## Adding requirements file
#ADD requirements.txt ToDoApp/ToDoApp
#
##set work directory
#WORKDIR /ToDoApp/ToDoApp

#install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["python", "./ToDoApp/manage.py runserver 0.0.0.0:8000"]
