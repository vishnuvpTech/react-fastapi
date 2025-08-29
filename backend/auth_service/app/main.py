from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.user_app import routers as user_routers


app = FastAPI(
    title="Auth Service",
    description="Authentication microservice with multiple login options",
    version="1.0.0",
    docs_url="/docs",       # Swagger UI (default: /docs)
    redoc_url="/redoc",     # ReDoc (default: /redoc)
    openapi_url="/openapi.json"  # OpenAPI schema
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    html_content = """
    <html>
        <head>
            <title>Auth Service</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    text-align: center; 
                    margin-top: 100px;
                }
                h1 { color: #333; }
                .btn {
                    display: inline-block;
                    margin: 10px;
                    padding: 12px 24px;
                    font-size: 16px;
                    font-weight: bold;
                    text-decoration: none;
                    color: white;
                    background-color: #007BFF;
                    border-radius: 6px;
                }
                .btn:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <h1>🚀 Welcome to Auth Service API</h1>
            <a href="/docs" class="btn">Swagger Docs</a>
            <a href="/redoc" class="btn">ReDoc</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

app.include_router(user_routers.router)
