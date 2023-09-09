#!/usr/bin/env python3

import os
import aws_cdk as core

from lib.financial_allocation import FinancialAllocation
from lib.params import props

app = core.App()

print(f"Deploying Financial Allocation to Environment: {props.get('env_name')}")

FinancialAllocation(
    app,
    "FinancialAllocation",
    props,
    stack_name=f"FinancialAllocation-{props.get('env_name')}",
    env=core.Environment(
        account=os.getenv("cdk_account"), region=os.getenv("cdk_default_region")
    ),
)

app.synth()
