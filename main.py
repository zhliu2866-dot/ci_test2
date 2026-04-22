from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD 部署成功！这是公网接口"}

@app.get("/hello")
def hello():
    return {"say": "hello world", "from": "render + github actions"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
