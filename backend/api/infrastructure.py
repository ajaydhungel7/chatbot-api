from constructs import Construct
from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_iam as iam,
)
from aws_cdk.aws_lambda_python_alpha import PythonFunction
import constants

class ChatbotApi(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Create Lambda function
        chatbot_lambda = PythonFunction(
            self, constants.LAMBDA_FUNCTION_NAME,
            entry="backend/api/runtime",
            index="chatbot.py",
            handler="handler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            environment={
                "CONTEXT_PROMPT": "Answer like I am 5 years old",
                "BEDROCK_MODEL_ID": constants.BEDROCK_MODEL_ID
            }
        )

        # Grant Bedrock permissions to Lambda
        chatbot_lambda.add_to_role_policy(iam.PolicyStatement(
            actions=[
                "bedrock:InvokeModel",
                "bedrock:ListFoundationModels"
            ],
            resources=["*"]
        ))

        # Create API Gateway
        api = apigw.LambdaRestApi(
            self, constants.API_GATEWAY_NAME,
            handler=chatbot_lambda,
            proxy=False
        )

        chat = api.root.add_resource("chat")
        chat.add_method("POST")