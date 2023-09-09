import subprocess, logging, sys, boto3
from json import load
from os import environ
# #from lib.helper.helper import get_ssm_parameters

# # Initialize Log handler
# logger = logging.getLogger("wrapper")
# logger.setLevel(logging.DEBUG)

# h1 = logging.StreamHandler(sys.stdout)
# h1.setLevel(logging.DEBUG)
# h1.addFilter(lambda record: record.levelno <= logging.INFO)
# h2 = logging.StreamHandler()
# h2.setLevel(logging.WARNING)
# logger.addHandler(h1)
# logger.addHandler(h2)

print(environ["ENV_NAME"])
# print(environ["AWS_ACCESS_KEY_ID"])
# print(environ["AWS_SECRET_ACCESS_KEY"])

print(environ["ENVIRONMENT"])
print(environ["ACCESS_KEY"])
print(environ["SECRET_KEY"])

# # Get Variables from GitHub Actions
# access_key = environ["AWS_ACCESS_KEY_ID"]
# secret_key = environ["AWS_SECRET_ACCESS_KEY"]
## region = environ["AWS_DEFAULT_REGION"]
# target_account = environ["cdk_account"]
# target_role_name = environ["cdk_role"]

# # authenticate with user credentials
# session = boto3.Session(
#     aws_access_key_id=access_key,
#     aws_secret_access_key=secret_key,
#     region_name=region
# )