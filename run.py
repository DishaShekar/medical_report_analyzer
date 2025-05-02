import subprocess

# Start FastAPI server
backend_process = subprocess.Popen(["uvicorn", "backend:app", "--reload"])

# Start Streamlit server
frontend_process = subprocess.Popen(["streamlit", "run", "app.py"])

# Keep both running
backend_process.wait()
frontend_process.wait()
