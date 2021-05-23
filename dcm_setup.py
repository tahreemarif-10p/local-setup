from secrets import auth_api_secret, dcm_rds_secret
from aws_utils import get_client, create_secret, create_queue


def dcm_setup():

    secrets_client = get_client(service_name='secretsmanager')

    create_secret(secrets_client, 'develop/AuthAPI/TestSecret1', str(auth_api_secret))
    create_secret(secrets_client, 'dev/DCMService/RDSSecrets', str(dcm_rds_secret))

    sqs_client = get_client(service_name='sqs')
    create_queue(sqs_client, queue_name='dcm-dev-force-reset-queue')


if __name__ == "__main__":
    dcm_setup()
