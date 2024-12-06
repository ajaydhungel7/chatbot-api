import json
import boto3
import os

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

def handler(event, context):
    # Extracting input and configuration details
    body = json.loads(event['body'])
    user_input = body['input']
    context_prompt = os.environ['CONTEXT_PROMPT']
    model_id = os.environ['BEDROCK_MODEL_ID']
    
    # Constructing the prompt
    prompt = f"{context_prompt}: {user_input}"
    
    try:
        # Adjust the request to match the new API reference
        request_body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 200,
            "top_k": 250,
            "stopSequences": [],
            "temperature": 1,
            "top_p": 0.999,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        }
        
        # Invoke the model
        response = bedrock_runtime.invoke_model(
            modelId=model_id,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(request_body)
        )
        
        # Parsing the response
        response_body = json.loads(response['body'].read())
        ai_response = response_body.get('completion', {}).get('content', "No response from model.")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'response': ai_response})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
