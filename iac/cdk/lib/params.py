import os
from json import loads

props = {
    "env_name": os.getenv('cdk_environment'),
    "ecr": {"lifecycle_policy_count": os.getenv('ecr_lifecycle_policy_count')},
}
