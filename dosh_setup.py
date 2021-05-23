from secrets import dosh_secret
from aws_utils import get_client, create_secret, dynamo_setup


if __name__ == "__main__":
    dynamo_setup()
    secrets_client = get_client(service_name='secretsmanager')
    create_secret(secrets_client, 'dosh-dev', str(dosh_secret))
