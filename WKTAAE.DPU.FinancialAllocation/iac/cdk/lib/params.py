import os
from json import loads

props = {
    "environment_name": "#{ENV_NAME}",
    "financial_allocation": loads("""
        #{FINANCIAL_ALLOCATION_CONFIG}
    """)
}
