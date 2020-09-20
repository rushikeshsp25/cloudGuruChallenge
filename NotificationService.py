import boto3
import Secret

def getSNSClient():
    client = boto3.client(
        "sns",
        aws_access_key_id = Secret.aws_access_key_id,
        aws_secret_access_key = Secret.aws_secret_access_key,
        region_name="us-east-2"
    )
    return client

class SNSNotification:
    __instance = None
    @staticmethod
    def getInstance():
        if SNSNotification.__instance == None:
            SNSNotification()
        return SNSNotification.__instance
    def notify(self):
        print(self.sns_client)
        print("Notifying")
        self.sns_client.publish(
            PhoneNumber="+917775910607",
            Message="Hello World!"
        )
    def __init__(self):
        if SNSNotification.__instance != None:
            raise Exception("Instance already exists, use getInstace() instead")
        else:
            self.sns_client = getSNSClient()
            SNSNotification.__instance = self


# Send your sms message.
# client.publish(
#     PhoneNumber="+12223334444",
#     Message="Hello World!"
# )

SNSNotification.getInstance().notify()