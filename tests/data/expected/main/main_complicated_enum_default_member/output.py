# generated by datamodel-codegen:
#   filename:  complicated_enum.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ProcessingStatus(Enum):
    COMPLETED = 'COMPLETED'
    PENDING = 'PENDING'
    FAILED = 'FAILED'


class Kind(BaseModel):
    __root__: str


class ProcessingStatusUnion(ProcessingStatus):
    pass


class ProcessingTask(BaseModel):
    processing_status_union: Optional[ProcessingStatusUnion] = 'COMPLETED'
    processing_status: Optional[ProcessingStatus] = ProcessingStatus.COMPLETED
    name: Optional[str] = None
    kind: Optional[Kind] = None
