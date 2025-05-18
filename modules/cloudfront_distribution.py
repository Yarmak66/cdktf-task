from constructs import Construct
from cdktf import TerraformOutput
from imports.aws.cloudfront_distribution import (
    CloudfrontDistribution,
    CloudfrontDistributionOrigin,
    CloudfrontDistributionDefaultCacheBehavior
)
from imports.aws.cloudfront_origin_access_identity import CloudfrontOriginAccessIdentity

class CloudFrontForS3(Construct):
    def __init__(self, scope: Construct, id: str, bucket_domain: str, index_document: str):
        super().__init__(scope, id)

        self.oai = CloudfrontOriginAccessIdentity(self, "OAI",
            comment="Origin Access Identity for S3"
        )

        self.distribution = CloudfrontDistribution(self, "CloudFront",
            enabled=True,
            default_root_object=index_document,
            origin=[
                CloudfrontDistributionOrigin(
                    domain_name=bucket_domain,
                    origin_id="s3-origin",
                    s3_origin_config={
                        "origin_access_identity": self.oai.cloudfront_access_identity_path
                    }
                )
            ],
            default_cache_behavior=CloudfrontDistributionDefaultCacheBehavior(
                target_origin_id="s3-origin",
                viewer_protocol_policy="redirect-to-https",
                allowed_methods=["GET", "HEAD"],
                cached_methods=["GET", "HEAD"],
                forwarded_values={
                    "query_string": False,
                    "cookies": {
                        "forward": "none"
                    }
                },
                compress=True
            ),
            viewer_certificate={
                "cloudfront_default_certificate": True
            },
            restrictions={
                "geo_restriction": {
                    "restriction_type": "none"
                }
            }
        )

        # Terraform Outputs
        TerraformOutput(self, "cloudfront_url",
            value=f"https://{self.distribution.domain_name}",
            description="URL of the CloudFront distribution"
        )

        TerraformOutput(self, "cloudfront_oai_path",
            value=self.oai.cloudfront_access_identity_path,
            description="OAI path used in CloudFront origin"
        )

        TerraformOutput(self, "cloudfront_canonical_user_id",
            value=self.oai.s3_canonical_user_id,
            description="Canonical User ID to use in S3 bucket policy"
        )
