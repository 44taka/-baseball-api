from pathlib import Path
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from configs.database import db
from loggings.costum_logging import CustomizeLogger
from routers import deposit


logger = logging.getLogger(__name__)

app = FastAPI()
app.logger = CustomizeLogger.make_logger(
    config_path=Path('/app/loggings/logging_config.json')
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(deposit.router)


@app.on_event('startup')
async def startup():
    logger.debug('db connect startup!')
    await db.connect()


@app.on_event('shutdown')
async def shutdown():
    logger.debug('db connect shutdown...')
    await db.disconnect()
