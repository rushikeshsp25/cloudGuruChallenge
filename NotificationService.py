import boto3
import Secret

def getSNSClient():
    client = boto3.client(
        "sns",
        aws_access_key_id = Secret.aws_access_key_id,
        aws_secret_access_key = Secret.aws_secret_access_key,
        region_name = Secret.aws_region
    )
    return client

class SNSNotification:
    __instance = None
    @staticmethod
    def getInstance():
        if SNSNotification.__instance == None:
            SNSNotification()
        return SNSNotification.__instance
    def notify(self,no_rows_added):
        self.sns_client.publish(
            TargetArn = Secret.topic_arn,
            Message = str(no_rows_added)+" rows are added!",
        )
    def __init__(self):
        if SNSNotification.__instance != None:
            raise Exception("Instance already exists, use getInstace() instead")
        else:
            self.sns_client = getSNSClient()
            SNSNotification.__instance = self


if __name__=="__main__":
    SNSNotification.getInstance().notify(10)