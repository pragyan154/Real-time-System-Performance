from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import psutil
# import mysql.connector
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    return render_template('index2.html')


# @app.route('/performance')
# def view_performance():
#     connection = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='root1234',
#         database='activity'
#     )
#     # print(connection)
#     cursor = connection.cursor()

#     cursor.execute("SELECT * FROM performance")
#     data = cursor.fetchall()
#     # print(data)

#     cursor.close()
#     connection.close()

#     return render_template('performance.html', data=data)


@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.start_background_task(get_performance_info)


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


# def create_performance_table():
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='root1234',
#             database='activity'
#         )
#         cursor = connection.cursor()

#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS performance (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 cpu_usage FLOAT,
#                 memory_usage FLOAT,
#                 disk_usage FLOAT,
#                 bytes_sent BIGINT,
#                 bytes_received BIGINT,
#                 timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#             )
#         ''')

#         connection.commit()
#         cursor.close()
#         connection.close()

#         print("Performance table created successfully")
#     except mysql.connector.Error as error:
#         print("Error connecting to MySQL:", error)


def get_performance_info():
    # connection = mysql.connector.connect(
    #     host='localhost',
    #     user='root',
    #     password='root1234',
    #     database='activity'
    # )
    # cursor = connection.cursor()

    while True:
        socketio.sleep(3)
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        bytes_sent = psutil.net_io_counters().bytes_sent
        bytes_received = psutil.net_io_counters().bytes_recv

        # if cpu_percent > 8:
        #     query = "INSERT INTO performance (cpu_usage, memory_usage, disk_usage, bytes_sent, bytes_received) " \
        #             "VALUES (%s, %s, %s, %s, %s)"
        #     cursor.execute(query, (cpu_percent, mem_percent, disk_percent, bytes_sent, bytes_received))
        #     connection.commit()

        socketio.emit('performance_info', {
            'CPU Usage': f'{cpu_percent}%',
            'Memory Usage': f'{mem_percent}%',
            'Disk Usage': f'{disk_percent}%',
            'Network Bytes Sent': bytes_sent,
            'Network Bytes Received': bytes_received
        })

    # cursor.close()
    # connection.close()


if __name__ == '__main__':
    # create_performance_table()
    socketio.run(app ,host='0.0.0.0', port=5001, allow_unsafe_werkzeug=True)
