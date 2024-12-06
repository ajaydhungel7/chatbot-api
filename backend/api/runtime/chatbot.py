import json
import boto3
import os

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

def handler(event, context):
    # Extracting input and configuration details
    print(event)
    body = json.loads(event['body'])
    user_input = body['input']
    context_prompt = os.environ['CONTEXT_PROMPT']
    model_id = os.environ['BEDROCK_MODEL_ID']
    
    # Constructing the prompt
    prompt = f"{context_prompt}: {user_input}"
    
    try:
        # Construct the request body correctly
        request_body = {
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 8192,
                "stopSequences": [],
                "temperature": 0,
                "topP": 1
            }
        }
        
        # Invoke the model
        response = bedrock_runtime.invoke_model(
            modelId="amazon.titan-text-express-v1",  # Use the correct model ID
            contentType="application/json",
            accept="application/json",
            body=json.dumps(request_body)
        )
        
        # Parsing the response
        response_body = json.loads(response['body'].read())
        ai_response = response_body.get('results', [{}])[0].get('outputText', "No response from model.")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'response': ai_response})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }