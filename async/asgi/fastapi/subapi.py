from fastapi import FastAPI

app = FastAPI(openapi_prefix="/subapi")


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


app.mount("/subapi", app)
