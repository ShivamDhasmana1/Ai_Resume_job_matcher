# Move into the Backend directory
Set-Location "C:\Users\mkdha\Mini project\ai_resume_job_matcher\Backend"

# Activate virtual environment
Write-Host "🔹 Activating Virtual Environment..."
& ".\venv\Scripts\activate"

# Start the FastAPI server
Write-Host "🚀 Starting FastAPI server at http://127.0.0.1:8000 ..."
uvicorn Main_app.main:app --reload
