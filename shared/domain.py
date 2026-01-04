from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum
import uuid

class SensitivityLevel(str, Enum):
    PUBLIC = "PUBLIC"
    INTERNAL = "INTERNAL"
    CONFIDENTIAL = "CONFIDENTIAL" # PII
    RESTRICTED = "RESTRICTED" # PCI/PAN

class Transaction(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    merchant_id: str
    amount: float
    currency: str
    # Simulating raw data that might contain PCI
    raw_data: str 
    metadata: Dict[str, Any] = {}

class SystemLog(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    level: str # INFO, WARN, ERROR
    message: str
    metadata: Dict[str, Any] = {}

class CheckResult(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARNING = "WARNING"

class ComplianceViolation(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    source_id: str # ID of transaction or log
    rule_id: str
    severity: str # HIGH, MEDIUM, LOW
    description: str
    status: str = "OPEN" # OPEN, REMEDIATED

class RiskForecast(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.now)
    risk_score: float # 0-100
    predicted_violations_count: int
    rationale: str
