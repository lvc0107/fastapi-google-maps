import traceback
from contextlib import AsyncExitStack, asynccontextmanager

from aiobotocore.session import AioSession
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.apis import (
    hello_world_router,
)
#from app.app_info import get_version
#from app.healthcheck import register_healthcheck
from app.settings import settings

ROUTERS = [
hello_world_router
]


def general_exception_handler(request, exception):  # NOSONAR
    if isinstance(exception, HTTPException):
        # we are letting the framework handle the known exceptions
        raise exception

    if settings.DEBUG:
        body = {
            "message": f"An error occurred: '{exception}'",
            "traceback": "".join(traceback.format_tb(exception.__traceback__)),
        }
    else:
        body = {"message": "An error occurred"}
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=body)


def validation_exception_handler(request: Request, exc: RequestValidationError):  # NOSONAR
    body = jsonable_encoder({"detail": exc.errors(), "body": exc.body})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=body)


@asynccontextmanager
async def lifespan(app: FastAPI):
    exit_stack = AsyncExitStack()
    """
    region_name = settings.AWS.AWS_REGION_NAME
    session = AioSession()
    s3_client = await exit_stack.enter_async_context(
        session.create_client("s3", region_name=region_name)
    )
    sqs_client = await exit_stack.enter_async_context(
        session.create_client("sqs", region_name=region_name)
    )
    #settings.AWS.SERVICES[settings.AWS.S3_CLIENT] = s3_client
    #settings.AWS.SERVICES[settings.AWS.SQS_CLIENT] = sqs_client
    """
    yield
    await exit_stack.aclose()


def create_app():
    app = FastAPI(
        #root_path=settings.prefix_path,
        title="Test app",
        description="Description of app's responsibilities",
        #version=get_version(),
        #debug=settings.debug,
        openapi_url="/openapi.json",
        docs_url="/documentation",
        lifespan=lifespan,
    )

    #register_healthcheck(app)

    @app.exception_handler(Exception)
    def default_error_handler(request: Request, exception):  # NOSONAR
        return general_exception_handler(request, exception)

    @app.exception_handler(RequestValidationError)
    def validation_error_handler(request: Request, exception: RequestValidationError):
        return validation_exception_handler(request, exception)

    #for router in ROUTERS:
        #app.include_router(router)

    return app
