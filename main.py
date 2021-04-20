from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/method/{name}")
def method_name_view(name: str):
	return f"method":{name}