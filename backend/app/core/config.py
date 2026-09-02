import os

class Settings:
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/healthcare')
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')

settings = Settings()
