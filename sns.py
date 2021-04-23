import boto3


def create_sns_topic(sns, topic_name, attributes={}):
    topic = sns.create_topic(
        Name=topic_name,
        Attributes=attributes
    )
    return topic


if __name__ == "__main__":
    session = boto3.session.Session(profile_name='localstack')
    sns = session.client('sns', endpoint_url="http://localhost:4566")
    topic_name = input("Please enter the sns topic name : ")
    topic = create_sns_topic(sns, topic_name)
    print('Topic Arn :', topic['TopicArn'])
