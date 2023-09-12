import subprocess, logging, sys, boto3

from json import load
from os import environ
from lib.helper.helper import get_ssm_parameters

# Initialize Log handler
logger = logging.getLogger("wrapper")
logger.setLevel(logging.DEBUG)

h1 = logging.StreamHandler(sys.stdout)
h1.setLevel(logging.DEBUG)
h1.addFilter(lambda record: record.levelno <= logging.INFO)
h2 = logging.StreamHandler()
h2.setLevel(logging.WARNING)
logger.addHandler(h1)
logger.addHandler(h2)

# print(environ["ENV_NAME"])
# # print(environ["AWS_ACCESS_KEY_ID"]) # Not working
# # print(environ["AWS_SECRET_ACCESS_KEY"]) # Not working

# print(environ["ENVIRONMENT"])
# print(environ["ACCESS_KEY"])
# print(environ["SECRET_KEY"])

# print(environ["TARGET_ACCOUNT_ID_FOR_CDK"])
# print(environ["MANAGEMENT_AWS_REGION"])
# print(environ["TARGET_AWS_REGION"])
# print(environ["TARGET_ROLE_NAME"])

# Get Variables from GitHub Actions
env_name = environ["ENVIRONMENT"]
access_key = environ["ACCESS_KEY"]
secret_key = environ["SECRET_KEY"]
target_account = environ["TARGET_ACCOUNT_ID"]
region = environ["MANAGEMENT_AWS_REGION"]
target_region = environ["TARGET_AWS_REGION"]
target_role_name = environ["TARGET_ROLE_NAME"]

# Authenticate with User Credentials
session = boto3.Session(
    aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region
)

# Assume Target Role
sts = session.client("sts")
role_credentials = sts.assume_role(
    RoleArn=f"arn:aws:iam::{target_account}:role/{target_role_name}",
    RoleSessionName="cdk1",
)

# export environment variables with AWS credentials
environ["AWS_ACCESS_KEY_ID"] = role_credentials.get("Credentials").get("AccessKeyId")
environ["AWS_SECRET_ACCESS_KEY"] = role_credentials.get("Credentials").get(
    "SecretAccessKey"
)
environ["AWS_SESSION_TOKEN"] = role_credentials.get("Credentials").get("SessionToken")
environ["AWS_DEFAULT_REGION"] = target_region
environ["CDK_DEFAULT_ACCOUNT"] = target_account
environ["CDK_DEFAULT_REGION"] = target_region

# as we need some parameters created by other stacks or by deployment pipelines on Octopus
# we gather these parameter from SSM Parameters Store and pass then through cdk context
context = []
if env_name != "Management":
    context = get_ssm_parameters(session, param_filter=["/cdk/fas/"])
    target_session = boto3.Session(
        aws_access_key_id=role_credentials.get("Credentials").get("AccessKeyId"),
        aws_secret_access_key=role_credentials.get("Credentials").get(
            "SecretAccessKey"
        ),
        aws_session_token=role_credentials.get("Credentials").get("SessionToken"),
        region_name=target_region,
    )
    # context += get_ssm_parameters(
    #     target_session,
    #     param_filter=[
    #         f"/{env_name}/financial-allocation"
    #     ]
    # )
    if "test" in env_name.lower():
        context += get_ssm_parameters(target_session, param_filter=["/cdk/fas/"])
else:
    context = get_ssm_parameters(session, param_filter=["/cdk/fas/"])


logger.info("Starting CDK synth process...")
r = subprocess.run(
    ["cdk", "synth", "--no-color", "--progress", "--debug" "-vvv" "events"] + context,
    capture_output=True,
    text=True,
)
if r.returncode:
    logger.error(r.stderr)
    raise SystemExit("An error occurred!")
logger.debug(r.stdout)

logger.info("Starting CDK bootstrap process...")
r = subprocess.run(
    [
        "cdk",
        "bootstrap",
        "--destroy",
        "--clean"
        # "--show-template",
        # "--no-color",
        # "--progress",
        # "--debug" "-vvv" "events",
    ]
    + context,
    capture_output=True,
    text=True,
)
if r.returncode:
    logger.error(r.stderr)
    raise SystemExit("An error occurred!")
logger.debug(r.stdout)

# # invoke the cdk deploy command
# logger.info(f"Starting deployment of Reporting Service Stack for {env_name}")
# r = subprocess.run(
#     [
#         "cdk",
#         "deploy",
#         "-vvv",
#         "--all",
#         "--no-color",
#         "--require-approval",
#         "never",
#         "--progress",
#         "events",
#     ]
#     + context,
#     capture_output=True,
#     text=True,
# )
# if r.returncode:
#     logger.error(r.stderr)
#     raise SystemExit("An error occurred!")
# logger.debug(r.stdout)
