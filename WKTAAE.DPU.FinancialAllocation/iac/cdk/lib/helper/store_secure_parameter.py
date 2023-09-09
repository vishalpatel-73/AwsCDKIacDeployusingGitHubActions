from aws_cdk import (
    aws_iam,
    aws_logs
)
from aws_cdk.custom_resources import (
    AwsCustomResource,
    AwsCustomResourcePolicy,
    AwsSdkCall,
    PhysicalResourceId,
)
from constructs import Construct

class SSMSecretParameter(Construct):
    """Imports the public key from an RSA key pair
    Arguments:
        :param name  -- Parameter name
        :param value -- Parameter string value
    """

    def __init__(self,
        scope: Construct,
        id: str,
        name: str,
        value: str) -> None:

        super().__init__(scope, id)

        resource_type = 'Custom::AWS-SSM-SecureString'

        on_create = AwsSdkCall(
            action='putParameter',
            service='SSM',
            parameters={
                "Name": name,
                "Value": value,
                "Type": "SecureString",
                "Overwrite": True
            },
            physical_resource_id=PhysicalResourceId.of(id=id)
        )

        AwsCustomResource(
            scope=scope,
            id=f"StoreSecureParameter{name}",
            policy=AwsCustomResourcePolicy.from_sdk_calls(resources=AwsCustomResourcePolicy.ANY_RESOURCE),
            on_create=on_create,
            on_update=on_create,
            on_delete=AwsSdkCall(
                action='deleteParameter',
                service='SSM',
                parameters={
                    "Name": name
                }
            ),
            log_retention=aws_logs.RetentionDays.ONE_MONTH,
            resource_type=resource_type,
            role=aws_iam.Role(
                self,
                f"{id}-LambdaRole",
                assumed_by=aws_iam.ServicePrincipal(service="lambda.amazonaws.com"),
                managed_policies=[
                    aws_iam.ManagedPolicy.from_aws_managed_policy_name(managed_policy_name="service-role/AWSLambdaBasicExecutionRole")
                ]
            )
        )