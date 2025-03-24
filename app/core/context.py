"""
Core context management module for the MCP server.
"""
from typing import Dict, Optional, List
from datetime import datetime
from uuid import uuid4

class Context:
    """Represents a model context."""
    def __init__(self, name: str, content: Dict, metadata: Optional[Dict] = None):
        self.id = str(uuid4())
        self.name = name
        self.content = content
        self.metadata = metadata or {}
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, content: Dict, metadata: Optional[Dict] = None):
        """Update context content and metadata."""
        self.content = content
        if metadata:
            self.metadata.update(metadata)
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> Dict:
        """Convert context to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "content": self.content,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class ContextManager:
    """Manages model contexts."""
    def __init__(self):
        self._contexts: Dict[str, Context] = {}

    def create_context(self, name: str, content: Dict, metadata: Optional[Dict] = None) -> Context:
        """Create a new context."""
        context = Context(name, content, metadata)
        self._contexts[context.id] = context
        return context

    def get_context(self, context_id: str) -> Optional[Context]:
        """Get a context by ID."""
        return self._contexts.get(context_id)

    def update_context(self, context_id: str, content: Dict, metadata: Optional[Dict] = None) -> Optional[Context]:
        """Update an existing context."""
        context = self.get_context(context_id)
        if context:
            context.update(content, metadata)
        return context

    def delete_context(self, context_id: str) -> bool:
        """Delete a context."""
        if context_id in self._contexts:
            del self._contexts[context_id]
            return True
        return False

    def list_contexts(self) -> List[Dict]:
        """List all contexts."""
        return [context.to_dict() for context in self._contexts.values()]