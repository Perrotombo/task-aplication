from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return "task aplication"

print ("Hello word")
