import pyperclip
import boto3
import credentials

class ClipBoard:
    def __init__(self):
        self.current_content = ""
        self.aws_access_key_id = credentials.aws_access_key_id
        self.aws_secret_access_key = credentials.aws_secret_access_key
        self.aws_region = 'us-east-2'
        self.bucket_name = 'clipboardbucket'

    def run(self):
        while True:
            try:
                self.current_content = pyperclip.waitForNewPaste()
                s3_client = boto3.client('s3', aws_access_key_id=self.aws_access_key_id,
                                         aws_secret_access_key=self.aws_secret_access_key, region_name=self.aws_region)
                s3_client.put_object(Bucket=self.bucket_name, Key='clipboard_contents.txt', Body=self.current_content)
                print(self.current_content)
            except KeyboardInterrupt:
                print("Application stopped")
                break
