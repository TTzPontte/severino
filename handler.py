import json
import boto3


def textract(event, context):
    # Document
    body = json.loads(event["body"])

    #s3BucketName = "pontte-upload-docs-staging"
    #documentName = "public/6Eh16y8KQL29p2ztdn7GQgf61681d5-532e-482c-a24d-6157029b35ba/Documento-pessoal_241120212024854.jpg"
    # Amazon Textract client
    textract = boto3.client('textract')
    # Call Amazon Textract
    blocks = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': body["bucket"],
                'Name': body["file"]
            }
        })["Blocks"]
    texts = [item.get("Text")
                for item in blocks
                if item.get("BlockType") == "LINE"]
    nome = texts[texts.index("NOME") + 1]
    cpf = texts[texts.index("DATA NASCIMENTO") + 1].replace()
    
    response = {
        "statusCode": 200,
        "body": json.dumps(dict(nome=nome, cpf=cpf))
    }
    
    return response


if __name__ == "__main__":
    response = textract(
        {
            "body": json.dumps({
                "bucket": "pontte-upload-docs-staging",
                "file": "public/6Eh16y8KQL29p2ztdn7GQgf61681d5-532e-482c-a24d-6157029b35ba/Documento-pessoal_241120212024854.jpg"
            })
        },
        {}
    )

    print(response["body"])

