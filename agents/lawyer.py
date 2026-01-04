from typing import List, Dict
from agents.base import BaseAgent
from shared.events import Event, EventType
from shared.domain import SensitivityLevel

class LawyerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Lawyer", subscribed_events=[])
        self.rules = self._load_rules()
        self.color = "blue"

    def _load_rules(self) -> List[Dict]:
        # Mocking complex regulation parsing
        return [
            {
                "id": "PCI-DSS-3.4",
                "description": "PAN must be unreadable anywhere it is stored.",
                "pattern": r"\b(?:\d[ -]*?){13,16}\b", # Simple regex for credit cards
                "level": SensitivityLevel.RESTRICTED
            },
            {
                "id": "GDPR-PII",
                "description": "Email addresses must be treated as PII.",
                "pattern": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
                "level": SensitivityLevel.CONFIDENTIAL
            }
        ]
    
    def get_rules(self):
        return self.rules

    def process(self, event: Event):
        pass # Lawyer is passive mostly, providing rules to others
