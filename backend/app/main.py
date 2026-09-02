from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title='HealthCareHub API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock API Endpoints for the buttons
@app.get('/api/stats')
def get_stats():
    return {"patients": 124, "doctors": 12, "appointments_today": 8, "revenue": "$4,200"}

@app.get('/api/patients')
def get_patients():
    return [
        {"id": 1, "name": "John Doe", "age": 45, "condition": "Hypertension"},
        {"id": 2, "name": "Jane Smith", "age": 32, "condition": "Prenatal Checkup"},
        {"id": 3, "name": "Michael Johnson", "age": 58, "condition": "Diabetes Type II"}
    ]

@app.get('/api/doctors')
def get_doctors():
    return [
        {"id": 1, "name": "Dr. Sarah Connor", "specialty": "Cardiology"},
        {"id": 2, "name": "Dr. House", "specialty": "Diagnostic Medicine"},
        {"id": 3, "name": "Dr. Stephen Strange", "specialty": "Neurology"}
    ]

@app.get('/api/appointments')
def get_appointments():
    return [
        {"time": "09:00 AM", "patient": "John Doe", "doctor": "Dr. Sarah Connor", "status": "Confirmed"},
        {"time": "10:30 AM", "patient": "Jane Smith", "doctor": "Dr. House", "status": "In Progress"},
        {"time": "11:15 AM", "patient": "Michael Johnson", "doctor": "Dr. Stephen Strange", "status": "Pending"}
    ]

# Serve Frontend
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend"))
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
def read_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))
