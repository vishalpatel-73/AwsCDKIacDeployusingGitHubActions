from constructs import Construct
from aws_cdk import Duration, RemovalPolicy, Stack, aws_iam as iam, aws_ecr as ecr


class FinancialAllocation(Stack):
    def __init__(self, scope: Construct, construct_id: str, props, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        print("Started AWS CDK Python!")
        environment_name = str(props.get("env_name"))
        ecr_config = props.get("ecr")

        ###
        # IAM User Creation
        # Manage Infrastructure as Code using AWS CDK Python
        ###

        iam_user = iam.User(
            self,
            f"FinancialAllocationIamUser",
            user_name=f"FinancialAllocation-{environment_name}",
        )

        iam_user_access_key = iam.CfnAccessKey(
            self, f"FinancialAllocationIamUserAccessKey", user_name=iam_user.user_name
        )

        ###
        # ECR Creation
        # 3 ECR for Workers, 1st for financialinfomation, 2nd for statementinit, 3rd for accountingsolutionfeedback.
        ###
              
        ecr_lifecycle_rule = ecr.LifecycleRule(
            description="Expire images after x deployments",
            max_image_count=4,
            # tag_status="any",
            rule_priority=1,
        )

        # Financial Infomation Worker ECR
        financialinfomation_worker_ecr = ecr.Repository(
            self,
            id="FinancialInfomationWorkerECR",
            repository_name=f"{environment_name}.financialinfomation.worker".lower(),
            lifecycle_rules=[ecr_lifecycle_rule],
            removal_policy=RemovalPolicy.DESTROY,
        )

        # Statement Init Worker ECR
        statementinit_worker_ecr = ecr.Repository(
            self,
            id="StatementInitWorkerECR",
            repository_name=f"{environment_name}.statementinit.worker".lower(),
            lifecycle_rules=[ecr_lifecycle_rule],
            removal_policy=RemovalPolicy.DESTROY,
        )

        # Accounting Solution Feedback Worker ECR
        accountingsolutionfeedback_worker_ecr = ecr.Repository(
            self,
            id="AccountingSolutionFeedbackWorkerECR",
            repository_name=f"{environment_name}.accountingsolutionfeedback.worker".lower(),
            lifecycle_rules=[ecr_lifecycle_rule],
            removal_policy=RemovalPolicy.DESTROY,
        )

        # Updateding IAM Policy for ECRs
        iam.Policy(
            self,
            id=f"FinancialAllocationUserIamPolicy",
            policy_name=f"FinancialAllocationUserIamPolicy-{environment_name}",
            statements=[
                iam.PolicyStatement(
                    actions=["ecr:*", "s3:*"],
                    effect=iam.Effect.ALLOW,
                    resources=[
                        financialinfomation_worker_ecr.repository_arn,
                        statementinit_worker_ecr.repository_arn,
                        accountingsolutionfeedback_worker_ecr.repository_arn,
                    ],
                ),
            ],
            users=[iam_user],
        )
