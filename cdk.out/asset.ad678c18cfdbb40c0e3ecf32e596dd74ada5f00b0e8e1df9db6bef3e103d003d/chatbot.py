import json
import boto3
import os

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

def handler(event, context):
    body = json.loads(event['body'])
    user_input = body['input']
    context_prompt = os.environ['CONTEXT_PROMPT']
    model_id = os.environ['BEDROCK_MODEL_ID']
    
    prompt = f"{context_prompt}: {user_input}"
    
    try:
        response = bedrock_runtime.invoke_model(
            modelId=model_id,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "inputText": prompt,
                "textGenerationConfig": {
                    "maxTokenCount": 512,
                    "temperature": 0.7,
                    "topP": 0.9
                }
            })
        )
        response_body = json.loads(response['body'].read())
        ai_response = response_body['results'][0]['outputText']
        
        return {
            'statusCode': 200,
            'body': json.dumps({'response': ai_response})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }