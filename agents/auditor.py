import re
from typing import List
from agents.base import BaseAgent
from agents.lawyer import LawyerAgent
from shared.events import Event, EventType
from shared.domain import Transaction, ComplianceViolation, SystemLog

class AuditorAgent(BaseAgent):
    def __init__(self, lawyer: LawyerAgent):
        super().__init__(name="Auditor", subscribed_events=[EventType.NEW_TRANSACTION])
        self.lawyer = lawyer
        self.color = "yellow"

    def process(self, event: Event):
        if event.type == EventType.NEW_TRANSACTION:
            self.audit_transaction(event.payload)

    def audit_transaction(self, transaction: Transaction):
        self.log(f"Auditing transaction {transaction.id}...")
        rules = self.lawyer.get_rules()
        
        # Check raw data for sensitive patterns
        for rule in rules:
            if re.search(rule["pattern"], transaction.raw_data):
                self.log(f"[bold red]VIOLATION DETECTED![/bold red] Rule: {rule['id']}")
                # Return a violation event
                violation = ComplianceViolation(
                    source_id=transaction.id,
                    rule_id=rule['id'],
                    severity="HIGH",
                    description=f"Found sensitive data matching {rule['id']} in transaction raw data."
                )
                return Event(type=EventType.VIOLATION_DETECTED, payload=violation, source_agent=self.name)
        
        self.log("Transaction Clean.")
        return None
