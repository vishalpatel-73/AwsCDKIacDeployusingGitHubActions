from aws_cdk import (
    aws_ssm
)
from constructs import Construct
from .store_secure_parameter import SSMSecretParameter
from distutils.util import strtobool

def update_param_store(scope: Construct, parameters_to_store: dict) -> None:
    if parameters_to_store:
        for parameterKey, parameterValue in parameters_to_store.items():
            if isinstance(parameterValue, dict) and parameterValue.get('encrypted', False):
                SSMSecretParameter(
                    scope,
                    f"SecureParameter{parameterKey}",
                    name=parameterKey,
                    value=parameterValue.get('value')
                )
            else:
                aws_ssm.CfnParameter(
                    scope,
                    f"StringParameters{parameterKey}",
                    type="String",
                    name=parameterKey,
                    value=parameterValue
                )

def get_ssm_parameters(session, param_filter: list):

    ssm = session.client('ssm')
    result = []

    p = ssm.get_paginator('describe_parameters')
    paginator = p.paginate(
        ParameterFilters=[
            {
                'Key': 'Name',
                'Option': 'BeginsWith',
                'Values': param_filter
            }
        ],
        PaginationConfig={
            'PageSize': 10
        }
    )
    
    for page in paginator:
        if page.get('Parameters'):
            r = ssm.get_parameters(Names=[v.get('Name') for v in page.get('Parameters')])
            for parameter in r.get('Parameters'):
                result.append('-c')
                result.append(f"{'_'.join(parameter.get('Name').split('/')[2:])}={parameter.get('Value')}")

    return result

def try_get_bool_context(scope: Construct, key: str):
    value = scope.node.try_get_context(key)
    if value:
        value = strtobool(value)

    return bool(value)