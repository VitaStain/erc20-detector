import taskiq_fastapi
from taskiq_aio_pika import AioPikaBroker

from src.config.base import settings

broker = AioPikaBroker(url=settings.rabbitmq.get_url(), max_priority=10)

taskiq_fastapi.init(broker, "src.config.application:get_app")
