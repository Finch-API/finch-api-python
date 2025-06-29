# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["BenefitType"]

BenefitType: TypeAlias = Optional[
    Literal[
        "457",
        "401k",
        "401k_roth",
        "401k_loan",
        "403b",
        "403b_roth",
        "457_roth",
        "commuter",
        "custom_post_tax",
        "custom_pre_tax",
        "fsa_dependent_care",
        "fsa_medical",
        "hsa_post",
        "hsa_pre",
        "s125_dental",
        "s125_medical",
        "s125_vision",
        "simple",
        "simple_ira",
    ]
]
