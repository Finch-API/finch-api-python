# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Job", "Department", "HiringTeam", "HiringTeamHiringManager", "HiringTeamRecruiter"]


class Department(BaseModel):
    name: Optional[str]


class HiringTeamHiringManager(BaseModel):
    name: Optional[str]


class HiringTeamRecruiter(BaseModel):
    name: Optional[str]


class HiringTeam(BaseModel):
    hiring_managers: Optional[List[HiringTeamHiringManager]]

    recruiters: Optional[List[HiringTeamRecruiter]]


class Job(BaseModel):
    id: str

    closed_at: Optional[datetime]

    created_at: Optional[datetime]

    department: Department

    hiring_team: HiringTeam

    name: Optional[str]

    status: Optional[Literal["open", "closed", "on_hold", "draft", "archived"]]
