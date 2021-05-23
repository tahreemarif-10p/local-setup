import boto3


def get_client(service_name, profile_name='localstack'):

    session = boto3.session.Session(profile_name=profile_name)
    client = session.client(
        service_name=service_name,
        endpoint_url='http://localhost:4566'
    )
    return client


# =============================================================================================
# SECRET MANAGER UTILS
# =============================================================================================


def create_secret(secrets_client, name, secret_value):
    try:
        secrets_client.create_secret(Name=name, SecretString=secret_value)
    except Exception:
        secrets_client.update_secret(SecretId=name, SecretString=secret_value)
        print('updating secrets')


# =============================================================================================
# SQS UTILS
# =============================================================================================


def create_queue(client, queue_name):
    response = client.create_queue(
        QueueName=queue_name
    )
    print(response)
    return response

# =============================================================================================
# DYNAMO UTILS
# =============================================================================================

def dynamo_setup():
    session = boto3.session.Session(profile_name='aws-local')
    dynamodb = session.client('dynamodb', endpoint_url="http://localhost:8000")

    try:
        dynamodb.create_table(TableName="dosh-dev-payment-requests",
                              AttributeDefinitions=[{"AttributeName": "guid",
                                                     "AttributeType": "S"}],
                              KeySchema=[{'AttributeName': 'guid',
                                          'KeyType': 'HASH'}],
                              ProvisionedThroughput={'ReadCapacityUnits': 1,
                                                     'WriteCapacityUnits': 1})
    except Exception:
        print("Dynamo table already present!")
