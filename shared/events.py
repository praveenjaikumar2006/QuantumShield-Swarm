from typing import Any, Dict
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum
import uuid

class EventType(str, Enum):
    NEW_TRANSACTION = "NEW_TRANSACTION"
    VIOLATION_DETECTED = "VIOLATION_DETECTED"
    RISK_FORECASTED = "RISK_FORECASTED"
    REMEDIATION_PLAN_CREATED = "REMEDIATION_PLAN_CREATED"
    REMEDIATION_APPLIED = "REMEDIATION_APPLIED"
    PROOF_GENERATED = "PROOF_GENERATED"

class Event(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    type: EventType
    payload: Any
    source_agent: str
