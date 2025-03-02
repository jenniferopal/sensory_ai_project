import fastapi
import uvicorn

app = fastapi.FastAPI() 

@app.get("/health")
def health():
    return {"status": "ok"}

print("Starting application...")

if __name__ == "__main__":
    print("Running application...")
    uvicorn.run(app, host="0.0.0.0", port=8080)

# import os
# print("Starting application...")
# print(f"Current directory: {os.getcwd()}")
# print("Listing files:")
# print(os.listdir("."))
# print("Application started!")

# # Keep the container running
# while True:
#     pass
