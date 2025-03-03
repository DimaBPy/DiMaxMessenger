from fastapi import FastAPI, Request
from loguru import logger
from starlette.responses import JSONResponse

logger.add("info.log", level="INFO")
app = FastAPI(title='DiMax', version='0.0.1')


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    with logger.contextualize():
        try:
            response = await call_next(request)
            if response.status_code in [401, 402, 403, 404]:
                logger.warning(f"Request to {request.url.path} failed")
            else:
                logger.info('Successfully accessed ' + request.url.path)
        except Exception as ex:
            logger.error(f"Request to {request.url.path} failed: {ex}")
            response = JSONResponse(content={"success": False},
                                    status_code=500)
        return response


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
