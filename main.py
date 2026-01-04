import time
import asyncio
from typing import List
from rich.console import Console
from rich.panel import Panel

from shared.events import Event, EventType
from shared.domain import Transaction
from agents.base import BaseAgent
from agents.lawyer import LawyerAgent
from agents.auditor import AuditorAgent

console = Console()

class BossAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Boss", subscribed_events=[EventType.VIOLATION_DETECTED])
        self.color = "magenta"

    def process(self, event: Event):
        if event.type == EventType.VIOLATION_DETECTED:
            violation = event.payload
            self.log(f"Received Violation Report: {violation.rule_id}. Initiating escalation protocol.")

def main():
    console.print(Panel.fit("[bold cyan]QuantumShield Swarm[/bold cyan] Initializing...", border_style="cyan"))

    # Initialize Agents
    lawyer = LawyerAgent()
    auditor = AuditorAgent(lawyer=lawyer) # Auditor needs access to Lawyer's rules
    boss = BossAgent()

    agents: List[BaseAgent] = [lawyer, auditor, boss]

    # Simple Event Loop
    event_queue: List[Event] = []

    # Mock Data Generation
    console.print("[dim]Simulating incoming transactions...[/dim]")
    
    # 1. Clean Transaction
    t1 = Transaction(
        merchant_id="M123",
        amount=100.0,
        currency="USD",
        raw_data="User ID: 555 purchased Item A",
    )
    event_queue.append(Event(type=EventType.NEW_TRANSACTION, payload=t1, source_agent="System"))

    # 2. Dirty Transaction (Contains a fake Credit Card)
    t2 = Transaction(
        merchant_id="M456",
        amount=250.0,
        currency="USD",
        raw_data="Log dump: payment processed for card 4111-1111-1111-1111 success",
    )
    event_queue.append(Event(type=EventType.NEW_TRANSACTION, payload=t2, source_agent="System"))

    # Processing Loop
    while event_queue:
        current_event = event_queue.pop(0)
        
        for agent in agents:
            # Agent processes event and might return a new event (reaction)
            # In a real system, this would be async/pub-sub
            if current_event.type in agent.subscribed_events:
                response_event = agent.process(current_event)
                if isinstance(response_event, Event):
                    event_queue.append(response_event)
        
        time.sleep(1) # Slow down for demo effect

    console.print("[bold green]Simulation Complete.[/bold green]")

if __name__ == "__main__":
    main()
