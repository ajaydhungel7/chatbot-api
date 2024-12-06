# Chatbot API with AWS CDK and Amazon Bedrock

This project implements a chatbot API using AWS CDK, API Gateway, Lambda, and Amazon Bedrock, allowing interaction with various language models.

## Prerequisites

- **AWS CLI**: Installed and configured
- **AWS CDK**: Installed
- **Python**: Ensure you have Python installed
- **Access to Amazon Bedrock**: Ensure you have access to the required models in your AWS account

## Deployment

1. Bootstrap your AWS environment (if not done already):

   ```bash
   cdk bootstrap
   ```

2. Deploy the stack:

   ```bash
   cdk deploy
   ```

## Usage

After deployment, you will receive an API endpoint. Use this endpoint to send POST requests to interact with the chatbot.

Example request:

```bash
curl -X POST https://your-api-endpoint/chat -d '{"prompt": "Hello, how are you?"}'
```

## Important Notes

- Ensure you have permissions to access the Bedrock models in your AWS account.
- Adjust the `modelId` in the Lambda function code as necessary.

## Troubleshooting

If you encounter issues:

- Verify your AWS credentials and permissions.
- Check access to the specified Bedrock model in your AWS console.
- Review CloudWatch logs for the Lambda function.

## Contributing

Contributions are welcome! Please submit pull requests or open issues for improvements or bug fixes.
