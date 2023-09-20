# My_Chatroom
My Chatroom is web based chat application for chat application over web. It is based on Flask framework

# Real-Time Chat Application with Flask and MongoDB

This is a simple real-time chat application built with Flask, MongoDB, and WebSocket support. It allows users to create accounts, log in, join chat rooms, and send and receive messages in real time.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features

- User account creation and authentication
- Sending and receiving messages
- MongoDB for data storage
- Dockerized for easy deployment

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- Docker and Docker Compose installed
- MongoDB server (either installed locally or accessible via a connection URI)

## Installation

1. Clone this repository:
   git clone https://github.com/HaziqAli001/My_Chatroom.git
   cd My_Chatroom

2. RUN the command on for downloading necessary dependencies:
    pip install -r requirements.txt

3. Build the docker containers:
   docker-compose up --build

## Usage
1- Start application using the following command:
  docker-compose up
2- Access the application in your web browser at http://localhost:5000

## Project Structure
- testapp -> Contains the Flask application code
  - app.py =>  Initializes the Flask app and configures routes
  - auth.py => Contains the  paths of application that require user login 
  - database.py => Contains the database congfigurations for our flask application
  - docker-compose.yml => Docker Compose configuration for running the app and MongoDB
  - Dockerfile => Dockerfile configurations for containerizing and making the docker image of our application
  - main.py => Contains the  paths of application that do not require user login
  - requirements.txt => Contains the dependencies for our Flask Application
  - user.py => Contains the User class for storing user data required by flask_login

