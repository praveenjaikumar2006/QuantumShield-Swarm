from abc import ABC, abstractmethod
from typing import List
from shared.events import Event, EventType
from rich.console import Console

console = Console()

class BaseAgent(ABC):
    def __init__(self, name: str, subscribed_events: List[EventType]):
        self.name = name
        self.subscribed_events = subscribed_events
        self.color = "white"

    def log(self, message: str):
        console.print(f"[{self.color}][{self.name}][/{self.color}] {message}")

    def handle(self, event: Event):
        if event.type in self.subscribed_events:
            self.process(event)

    @abstractmethod
    def process(self, event: Event):
        """Process the event and return a new event or None"""
        pass
