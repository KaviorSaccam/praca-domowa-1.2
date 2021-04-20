from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world!"}

@app.get("/method")
def get_method():
	return {"method":"GET"}

@app.put("/method")
def put_method():
	return {"method":"PUT"}

@app.options("/method")
def options_method():
	return {"method":"OPTIONS"}

@app.delete("/method")
def delete_method():
	return {"method":"DELETE"}

@app.post("/method")
def post_method():
	return {"method":"POST"}