# PyAutomate AI

PyAutomate AI is an enterprise-grade automation and AI platform that combines RPA, AI, data processing, workflow automation, and modern deployment practices.

## Project Phases

1. **Automation Framework & RPA**
2. **AI Model Integration & API Development**
3. **Data Processing & Decision System**
4. **Workflow Automation & UI**
5. **Deployment & Security**
6. **Monitoring, Alerts & Final Touch**

## Folder Structure

- `automation/` - RPA scripts
- `ai_models/` - ML/DL models
- `data_processing/` - ETL & processing scripts
- `api/` - FastAPI/Flask endpoints
- `frontend/` - React or Streamlit UI
- `workflow_engine/` - Celery workers
- `config/` - Settings & secrets
- `docs/` - Documentation
- `tests/` - Unit & Integration tests

# PyAutomate AI – Basic Project

## Setup

### 1. Create and Activate Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

### 2. Install Python Dependencies
```powershell
pip install -r pyautomate_ai/requirements.txt
```

### 3. Install Tesseract OCR (for OCR demo)
- Download from: https://github.com/tesseract-ocr/tesseract/releases
- Run the installer and add `C:\Program Files\Tesseract-OCR` to your PATH

### 4. Run Demo Scripts

#### Selenium Demo
```powershell
python pyautomate_ai/automation/selenium_demo.py
```

#### PyAutoGUI Demo
```powershell
python pyautomate_ai/automation/pyautogui_demo.py
```

#### OCR Demo
If Tesseract is not in your PATH, edit `ocr_demo.py` and set:
```python
pytesseract.pytesseract.tesseract_cmd = r'C\\Program Files\\Tesseract-OCR\\tesseract.exe'
```
Then run:
```powershell
python pyautomate_ai/automation/ocr_demo.py
```

## Running the PyAutoGUI Automation Demo

This demo moves the mouse and takes a screenshot of your desktop.

### Prerequisites
- Make sure you have installed all dependencies:
  ```powershell
  pip install -r pyautomate_ai/requirements.txt
  ```
- For screenshots, ensure you are not running in a headless environment (must have a visible desktop session).

### Run the Demo
```powershell
python pyautomate_ai/automation/pyautogui_demo.py
```

The screenshot will be saved as `desktop_screenshot.png` in the `automation/` folder.

## Phase 2: API & AI Model Demo

### 1. Install new dependencies
```powershell
pip install -r pyautomate_ai/requirements.txt
```

### 2. Run the FastAPI server
```powershell
uvicorn pyautomate_ai.api.main:app --reload
```

### 3. Test the API
- Open your browser at: http://127.0.0.1:8000/docs
- Use the `/classify` endpoint to POST text and get a label ("invoice", "resume", or "unknown"). 

## Phase 3: Data Processing & Decision System

### 1. Install new dependencies
```powershell
pip install -r pyautomate_ai/requirements.txt
```

### 2. Run the data processing script
```powershell
python pyautomate_ai/data_processing/scrape_and_clean.py
```

### 3. (Optional) Save to PostgreSQL
- Uncomment and set your DB URL in `scrape_and_clean.py`:
  ```python
  db_url = 'postgresql://user:password@localhost:5432/yourdb'
  save_to_postgres(df_clean, 'gdp_table', db_url)
  ```
- Make sure PostgreSQL is running and accessible. 

## Phase 4: Workflow Automation & UI

### 1. Start RabbitMQ (for Celery)
```powershell
docker-compose -f pyautomate_ai/docker-compose.yml up -d rabbitmq
```
- RabbitMQ management UI: http://localhost:15672 (user: guest, pass: guest)

### 2. Start the Celery worker
```powershell
celery -A pyautomate_ai.workflow_engine.worker worker --loglevel=info
```

### 3. Start the FastAPI server (if not already running)
```powershell
uvicorn pyautomate_ai.api.main:app --reload
```

### 4. Start the Streamlit UI
```powershell
streamlit run pyautomate_ai/frontend/streamlit_app.py
```

- Use the UI to classify text or trigger an automation task!
