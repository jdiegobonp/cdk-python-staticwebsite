from aws_cdk import (
    Stack,
    aws_s3,
)
from constructs import Construct

class StaticwebsiteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cors_rule = aws_s3.CorsRule(
            allowed_methods=[aws_s3.HttpMethods.GET, aws_s3.HttpMethods.POST],
            allowed_origins=["*"],
            allowed_headers=["*"],
            exposed_headers=["ETag"],
            id="staticwebsite",
            max_age=3000,
        )

        aws_s3.Bucket(
            self,
            's3-staticwebsite-poc-jd',
            bucket_name = 's3-staticwebsite-poc-jd-102321',
            cors = [cors_rule],
            access_control = aws_s3.BucketAccessControl.PUBLIC_READ,
        )