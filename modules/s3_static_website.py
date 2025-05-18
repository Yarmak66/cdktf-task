# modules/s3_static_website.py
from constructs import Construct
from cdktf import TerraformAsset, AssetType, TerraformOutput
from imports.aws.s3_bucket import S3Bucket, S3BucketWebsite
from imports.aws.s3_bucket_object import S3BucketObject
from imports.aws.s3_bucket_policy import S3BucketPolicy
from html_generator import generate_html

class S3StaticWebsite(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        bucket_name: str,
        asset_path: str,
        index_document: str,
        cloudfront_oai_canonical_user_id: str
    ):
        super().__init__(scope, id)

        self.bucket = S3Bucket(self, "Bucket",
            bucket=bucket_name,
            force_destroy=True,
            website=S3BucketWebsite(index_document=index_document)
        )

        S3BucketObject(self, "HtmlObject",
            bucket=self.bucket.bucket,
            key="index.html",
            source=asset_path,
            content_type="text/html"
        )

        S3BucketPolicy(self, "BucketPolicy",
            bucket=self.bucket.bucket,
            policy=f'''
{{
  "Version": "2012-10-17",
  "Statement": [
    {{
      "Sid": "AllowCloudFrontRead",
      "Effect": "Allow",
      "Principal": {{
        "CanonicalUser": "{cloudfront_oai_canonical_user_id}"
      }},
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::{bucket_name}/*"
    }}
  ]
}}
'''
        )

def generate_and_deploy_html_site(scope: Construct, bucket_name: str, index_document: str, region: str, cloudfront_oai_canonical_user_id: str):
    generate_html()
    asset = TerraformAsset(scope, "HtmlAsset", path="index.html", type=AssetType.FILE)

    site = S3StaticWebsite(scope, "Website",
        bucket_name=bucket_name,
        asset_path=asset.path,
        index_document=index_document,
        cloudfront_oai_canonical_user_id=cloudfront_oai_canonical_user_id
    )

    TerraformOutput(scope, "bucket_name", value=bucket_name)
    TerraformOutput(scope, "note", value="Static site is ready — accessed securely via CloudFront with OAI.")

    return site
