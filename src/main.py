import stackprinter
import uvicorn

from src.api import routers
from src.config import app

for router in routers:
    app.include_router(router)


if __name__ == "__main__":
    stackprinter.set_excepthook()
    uvicorn.run(app, host="127.0.0.1", port=8000)
