from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'Bye'


if __name__ == "__main__":
    app.run()
    
    
############################### Decorators in Python ######################################
import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        function_run_time = end_time - start_time  
        print(f'{function.__name__} run speed {function_run_time}s')
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()