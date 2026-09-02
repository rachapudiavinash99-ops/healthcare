from fastapi import FastAPI

app = FastAPI(title='HealthCareHub API')

@app.get('/')
def root():
    return {'message': 'Welcome to HealthCareHub'}
