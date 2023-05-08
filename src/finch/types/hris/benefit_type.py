# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

__all__ = ["BenefitType"]

BenefitType = Optional[
    Literal[
        "401k",
        "401k_roth",
        "401k_loan",
        "403b",
        "403b_roth",
        "457",
        "457_roth",
        "s125_medical",
        "s125_dental",
        "s125_vision",
        "hsa_pre",
        "hsa_post",
        "fsa_medical",
        "fsa_dependent_care",
        "simple_ira",
        "simple",
        "commuter",
        "custom_post_tax",
        "custom_pre_tax",
    ]
]
