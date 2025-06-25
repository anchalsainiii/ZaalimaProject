import streamlit as st
import requests
from celery import Celery

st.title('PyAutomate AI UI')

st.header('Document Classifier')
text = st.text_area('Enter text to classify:')
if st.button('Classify'):
    resp = requests.post('http://localhost:8000/classify', json={'text': text})
    st.write('Prediction:', resp.json().get('label'))

st.header('Trigger Automation Task')
task_name = st.text_input('Task name:', 'demo_task')
if st.button('Run Automation Task'):
    celery_app = Celery('frontend', broker='pyamqp://guest@localhost//')
    result = celery_app.send_task('worker.run_automation_task', args=[task_name])
    st.write('Task submitted! Task ID:', result.id)

st.header('Desktop Automation: Take Screenshot')
if st.button('Take Screenshot'):
    import subprocess
    import time
    # Run the PyAutoGUI demo script
    subprocess.run(['python', '../automation/pyautogui_demo.py'], check=True)
    time.sleep(1)  # Wait a moment for the screenshot to be saved
    st.success('Screenshot taken!')
    st.image('../automation/desktop_screenshot.png', caption='Desktop Screenshot') 