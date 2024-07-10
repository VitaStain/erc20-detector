from pydantic import BaseModel
from yarl import URL


class RabbitmqSettings(BaseModel):
    host: str = "rabbitmq"
    port: int = 5672
    user: str = "rabbitmq"
    password: str = "rabbitmq"

    def get_url(self) -> URL:
        """Assemble RabbitMQ URL from settings"""
        return URL.build(
            scheme="amqp",
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
        )
