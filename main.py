from constructs import Construct
from cdktf import App, TerraformStack, S3Backend
from modules.s3_static_website import generate_and_deploy_html_site
from modules.cloudfront_distribution import CloudFrontForS3
from imports.aws.provider import AwsProvider
import os

class MyStaticSiteStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str, region: str, bucket_name: str):
        super().__init__(scope, ns)

        S3Backend(self,
            bucket=os.getenv("CDKTF_BACKEND_BUCKET"),
            key=os.getenv("CDKTF_BACKEND_KEY"),
            region=region,
            dynamodb_table=os.getenv("CDKTF_BACKEND_LOCK_TABLE"),
            encrypt=True
        )

        AwsProvider(self, "AWS", region=region)

        cloudfront = CloudFrontForS3(self, "CloudFront",
            bucket_domain=f"{bucket_name}.s3.{region}.amazonaws.com",
            index_document="index.html"
        )

        generate_and_deploy_html_site(
            self,
            bucket_name=bucket_name,
            index_document="index.html",
            region=region,
            cloudfront_oai_canonical_user_id=cloudfront.oai.s3_canonical_user_id
        )


app = App()

env = os.getenv("ENV", "dev")
region = "eu-north-1"

if env == "prod":
    bucket_name = "cdktf-static-site-prod"
    stack_id = "prod-site"
else:
    bucket_name = "cdktf-static-site-dev"
    stack_id = "dev-site"

MyStaticSiteStack(app, stack_id, region=region, bucket_name=bucket_name)
app.synth()
