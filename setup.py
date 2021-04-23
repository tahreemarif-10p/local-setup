import boto3
from secrets import secret


def create_secret(name, secret_value):
    session = boto3.session.Session(profile_name='localstack')
    secrets_client = session.client(
        service_name='secretsmanager',
        endpoint_url='http://localhost:4566'
    )
    try:
        secrets_client.create_secret(Name=name, SecretString=secret_value)
    except Exception:
        secrets_client.update_secret(SecretId=name, SecretString=secret_value)


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


if __name__ == "__main__":
    dynamo_setup()
    create_secret('dosh-test', str(secret))
