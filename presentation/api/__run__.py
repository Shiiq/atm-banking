import uvicorn


if __name__ == "__main__":
    uvicorn.run("presentation.api.main:app", reload=True)
