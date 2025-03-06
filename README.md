# Task Manager

## Overview
Task Manager is a web application built with Django that allows users to manage their tasks efficiently. Users can create, update, and delete tasks, set due dates, and organize their workload.

## Features
- User authentication and authorization
- Task creation, update, and deletion
- Due date management
- Responsive design

## Prerequisites
- Python 3.x
- Django 3.x
- Git

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/jeffslaziraugeight/task.git
   cd task_manager
2. **Create and activate a virtual environment:**
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`

3. **Install Dependencies**
   pip install -r requirements.txt


4. **Apply Migrations**
    python manage.py migrate
   
5. **Run the Development server**
    python manage.py runserver
