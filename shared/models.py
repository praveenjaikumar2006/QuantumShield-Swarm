from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Finding(BaseModel):
    id: str = Field(..., description="Unique finding id")
    source: str = Field(..., description="Source agent or system")
    rule: str = Field(..., description="Which rule was violated or matched")
    severity: str = Field(..., description="low|medium|high")
    excerpt: Optional[str] = Field(None, description="Snippet showing the finding")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ScanRequest(BaseModel):
    path: str = Field(..., description="File or directory path to scan")
