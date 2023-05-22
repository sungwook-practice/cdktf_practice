#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.s3_bucket import S3Bucket


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here
        AwsProvider(self, "aws", region="ap-northeast-2", profile="default")

        # create s3 bucket using cdktf
        self.bueckt_name = "choilab-test-cdktf"
        S3Bucket(self, "test_bucket", bucket=self.bueckt_name)


app = App()
MyStack(app, "helloworld")

app.synth()
