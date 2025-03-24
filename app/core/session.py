"""
Core session management module for the MCP server.
"""
from typing import Dict, Optional, List
from datetime import datetime
from uuid import uuid4

class Session:
    """Represents a model context session."""
    def __init__(self, name: str, context_id: str, metadata: Optional[Dict] = None):
        self.id = str(uuid4())
        self.name = name
        self.context_id = context_id
        self.metadata = metadata or {}
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        self.active = True

    def update(self, metadata: Optional[Dict] = None):
        """Update session metadata."""
        if metadata:
            self.metadata.update(metadata)
        self.updated_at = datetime.utcnow()

    def end(self):
        """End the session."""
        self.active = False
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> Dict:
        """Convert session to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "context_id": self.context_id,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "active": self.active
        }

class SessionManager:
    """Manages model context sessions."""
    def __init__(self):
        self._sessions: Dict[str, Session] = {}

    def create_session(self, name: str, context_id: str, metadata: Optional[Dict] = None) -> Session:
        """Create a new session."""
        session = Session(name, context_id, metadata)
        self._sessions[session.id] = session
        return session

    def get_session(self, session_id: str) -> Optional[Session]:
        """Get a session by ID."""
        return self._sessions.get(session_id)

    def update_session(self, session_id: str, metadata: Optional[Dict] = None) -> Optional[Session]:
        """Update an existing session."""
        session = self.get_session(session_id)
        if session:
            session.update(metadata)
        return session

    def end_session(self, session_id: str) -> Optional[Session]:
        """End a session."""
        session = self.get_session(session_id)
        if session:
            session.end()
        return session

    def list_sessions(self, active_only: bool = False) -> List[Dict]:
        """List all sessions."""
        sessions = self._sessions.values()
        if active_only:
            sessions = filter(lambda s: s.active, sessions)
        return [session.to_dict() for session in sessions]

    def get_sessions_by_context(self, context_id: str, active_only: bool = False) -> List[Dict]:
        """Get all sessions for a specific context."""
        sessions = [s for s in self._sessions.values() if s.context_id == context_id]
        if active_only:
            sessions = [s for s in sessions if s.active]
        return [session.to_dict() for session in sessions]