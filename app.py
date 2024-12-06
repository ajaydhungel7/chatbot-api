#!/usr/bin/env python3
import aws_cdk as cdk
from backend.component import ChatbotBackend

app = cdk.App()
ChatbotBackend(app, "ChatbotBackend")
app.synth()