import json

def canary(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "mensaje": "Respuesta desde Serverless",
            "version": "with canary v5"
        })
    }


def general(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "mensaje": "Respuesta desde Serverless",
            "version": "general canary"
        })
    }