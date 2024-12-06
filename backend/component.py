from constructs import Construct
from aws_cdk import Stack
from backend.api.infrastructure import ChatbotApi

class ChatbotBackend(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ChatbotApi(self, "ChatbotApi")