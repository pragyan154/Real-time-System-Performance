
# Real-time System Performance Monitoring

## Overview
The Real-time System Performance Monitoring project is a web application that provides real-time monitoring of system performance metrics such as CPU usage, memory usage, disk usage, and network traffic. The application displays the performance data in a web page and also stores it in a MySQL database for future analysis and reporting.

## Features
- Real-time monitoring of system performance metrics.
- Display of performance data in a tabular format on a web page.
- Storage of performance data in a MySQL database.
- Automatic data updates at regular intervals.
- Highlighting of CPU usage exceeding a threshold (6% in this implementation).
- Socket-based communication between the Flask server and the web page for real-time updates.

## Technologies Used
- Python
- Flask
- Flask-SocketIO
- MySQL Connector/Python
- psutil
- HTML
- CSS
- JavaScript

## Project Structure
- app.py: The main Python script containing the Flask application and the performance monitoring logic.
- templates/index.html: The HTML template for the home page that displays real-time performance data.
- templates/performance.html: The HTML template for the performance data table page.