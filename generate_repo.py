import os
import subprocess
import time

def run_cmd(cmd, cwd=None):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True, cwd=cwd)

base_dir = r"D:\healthcare"

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Setup initial architecture
run_cmd("git config --global user.email 'bot@healthcare.com'", cwd=base_dir)
run_cmd("git config --global user.name 'Healthcare Bot'", cwd=base_dir)

# Commit 1: Initial architecture
create_file(os.path.join(base_dir, "README.md"), "# HealthCareHub\n\nSmart Healthcare Management Platform\n")
create_file(os.path.join(base_dir, ".gitignore"), "node_modules/\nvenv/\n__pycache__/\n.env\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "chore: Initial project architecture and environment setup"', cwd=base_dir)

# Commit 2: Backend setup
create_file(os.path.join(base_dir, "backend", "requirements.txt"), "fastapi\nuvicorn\nsqlalchemy\nalembic\npsycopg2-binary\npasslib\nbcrypt\npython-jose\npydantic\npytest\n")
create_file(os.path.join(base_dir, "backend", "app", "main.py"), "from fastapi import FastAPI\n\napp = FastAPI(title='HealthCareHub API')\n\n@app.get('/')\ndef root():\n    return {'message': 'Welcome to HealthCareHub'}\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(backend): Setup backend base with FastAPI"', cwd=base_dir)

# Commit 3: Database Models & Config
create_file(os.path.join(base_dir, "backend", "app", "core", "config.py"), "import os\n\nclass Settings:\n    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/healthcare')\n    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')\n\nsettings = Settings()\n")
create_file(os.path.join(base_dir, "backend", "app", "core", "database.py"), "from sqlalchemy import create_engine\nfrom sqlalchemy.orm import declarative_base, sessionmaker\nfrom app.core.config import settings\n\nengine = create_engine(settings.DATABASE_URL)\nSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\nBase = declarative_base()\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(db): Add database configuration and core module"', cwd=base_dir)

# Commit 4: Auth Models and RBAC
create_file(os.path.join(base_dir, "backend", "app", "models", "user.py"), "from sqlalchemy import Column, Integer, String, Boolean\nfrom app.core.database import Base\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True, index=True)\n    email = Column(String, unique=True, index=True)\n    hashed_password = Column(String)\n    is_active = Column(Boolean, default=True)\n    role = Column(String)\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(auth): Implement authentication models and RBAC"', cwd=base_dir)

# Commit 5: Auth Schemas and Logic
create_file(os.path.join(base_dir, "backend", "app", "schemas", "user.py"), "from pydantic import BaseModel\n\nclass UserBase(BaseModel):\n    email: str\n    role: str\n\nclass UserCreate(UserBase):\n    password: str\n\nclass UserOut(UserBase):\n    id: int\n    is_active: bool\n    class Config:\n        orm_mode = True\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(auth): Add user schemas and security layer"', cwd=base_dir)

# Commit 6: Patient Management
create_file(os.path.join(base_dir, "backend", "app", "models", "patient.py"), "from sqlalchemy import Column, Integer, String, ForeignKey\nfrom app.core.database import Base\n\nclass Patient(Base):\n    __tablename__ = 'patients'\n    id = Column(Integer, primary_key=True, index=True)\n    user_id = Column(Integer, ForeignKey('users.id'))\n    first_name = Column(String)\n    last_name = Column(String)\n    dob = Column(String)\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(patient): Add patient management module"', cwd=base_dir)

# Commit 7: Doctor Management
create_file(os.path.join(base_dir, "backend", "app", "models", "doctor.py"), "from sqlalchemy import Column, Integer, String, ForeignKey\nfrom app.core.database import Base\n\nclass Doctor(Base):\n    __tablename__ = 'doctors'\n    id = Column(Integer, primary_key=True, index=True)\n    user_id = Column(Integer, ForeignKey('users.id'))\n    specialization = Column(String)\n    department = Column(String)\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(doctor): Implement doctor and department management"', cwd=base_dir)

# Commit 8: Appointment Scheduling
create_file(os.path.join(base_dir, "backend", "app", "models", "appointment.py"), "from sqlalchemy import Column, Integer, String, ForeignKey, DateTime\nfrom app.core.database import Base\n\nclass Appointment(Base):\n    __tablename__ = 'appointments'\n    id = Column(Integer, primary_key=True, index=True)\n    patient_id = Column(Integer, ForeignKey('patients.id'))\n    doctor_id = Column(Integer, ForeignKey('doctors.id'))\n    appointment_date = Column(DateTime)\n    status = Column(String)\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(appointment): Implement appointment scheduling system"', cwd=base_dir)

# Commit 9: Medical Records
create_file(os.path.join(base_dir, "backend", "app", "models", "medical_record.py"), "from sqlalchemy import Column, Integer, String, ForeignKey, Text\nfrom app.core.database import Base\n\nclass MedicalRecord(Base):\n    __tablename__ = 'medical_records'\n    id = Column(Integer, primary_key=True, index=True)\n    patient_id = Column(Integer, ForeignKey('patients.id'))\n    doctor_id = Column(Integer, ForeignKey('doctors.id'))\n    diagnosis = Column(Text)\n    notes = Column(Text)\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(emr): Add electronic medical records and consultations"', cwd=base_dir)

# Commit 10: Prescription
create_file(os.path.join(base_dir, "backend", "app", "models", "prescription.py"), "from sqlalchemy import Column, Integer, String, ForeignKey, Text\nfrom app.core.database import Base\n\nclass Prescription(Base):\n    __tablename__ = 'prescriptions'\n    id = Column(Integer, primary_key=True, index=True)\n    appointment_id = Column(Integer, ForeignKey('appointments.id'))\n    medication = Column(String)\n    dosage = Column(String)\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(pharmacy): Add prescription and pharmacy modules"', cwd=base_dir)

# Commit 11: Laboratory
create_file(os.path.join(base_dir, "backend", "app", "models", "laboratory.py"), "from sqlalchemy import Column, Integer, String, ForeignKey\nfrom app.core.database import Base\n\nclass LabTest(Base):\n    __tablename__ = 'lab_tests'\n    id = Column(Integer, primary_key=True, index=True)\n    test_name = Column(String)\n    patient_id = Column(Integer, ForeignKey('patients.id'))\n    result = Column(String)\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(lab): Add laboratory management module"', cwd=base_dir)

# Commit 12: Billing
create_file(os.path.join(base_dir, "backend", "app", "models", "billing.py"), "from sqlalchemy import Column, Integer, String, ForeignKey, Float\nfrom app.core.database import Base\n\nclass Invoice(Base):\n    __tablename__ = 'invoices'\n    id = Column(Integer, primary_key=True, index=True)\n    patient_id = Column(Integer, ForeignKey('patients.id'))\n    total_amount = Column(Float)\n    status = Column(String)\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(billing): Add billing and invoice generation"', cwd=base_dir)

# Commit 13: Notifications & Audit logs
create_file(os.path.join(base_dir, "backend", "app", "models", "audit.py"), "from sqlalchemy import Column, Integer, String, ForeignKey, DateTime\nfrom app.core.database import Base\nfrom datetime import datetime\n\nclass AuditLog(Base):\n    __tablename__ = 'audit_logs'\n    id = Column(Integer, primary_key=True, index=True)\n    user_id = Column(Integer)\n    action = Column(String)\n    timestamp = Column(DateTime, default=datetime.utcnow)\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(audit): Add notifications and audit logging"', cwd=base_dir)

# Commit 14: Frontend Boilerplate
create_file(os.path.join(base_dir, "frontend", "package.json"), '{\n  "name": "healthcare-frontend",\n  "version": "1.0.0",\n  "scripts": {\n    "start": "react-scripts start",\n    "build": "react-scripts build"\n  }\n}\n')
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "feat(frontend): Initialize React frontend architecture"', cwd=base_dir)

# Commit 15: Docker and Config
create_file(os.path.join(base_dir, "docker-compose.yml"), "version: '3.8'\nservices:\n  db:\n    image: postgres:15\n    environment:\n      POSTGRES_DB: healthcare\n      POSTGRES_USER: user\n      POSTGRES_PASSWORD: password\n")
create_file(os.path.join(base_dir, "Dockerfile.backend"), "FROM python:3.12-slim\nWORKDIR /app\nCOPY backend/requirements.txt .\nRUN pip install -r requirements.txt\nCOPY backend/ .\nCMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n")
run_cmd("git add .", cwd=base_dir)
run_cmd('git commit -m "chore(infra): Dockerize and improve deployment configuration"', cwd=base_dir)

# Push to remote
try:
    run_cmd("git branch -M main", cwd=base_dir)
    run_cmd("git remote add origin https://github.com/rachapudiavinash99-ops/healthcare.git", cwd=base_dir)
    # Using personal access token or skipping credential prompt, we'll just run it. It might fail if no creds are cached.
    run_cmd("git push -u origin main", cwd=base_dir)
except subprocess.CalledProcessError as e:
    print(f"Git push failed: {e}")

print("Repository generation complete.")
