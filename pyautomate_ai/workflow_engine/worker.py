from celery import Celery
import time

app = Celery('worker', broker='pyamqp://guest@localhost//')

@app.task
def run_automation_task(task_name):
    print(f"Running automation task: {task_name}")
    time.sleep(2)
    return f"Task {task_name} completed!" 