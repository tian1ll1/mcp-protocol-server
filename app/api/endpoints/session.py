"""
API endpoints for session management.
"""
from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, List, Optional
from app.core.session import SessionManager
from pydantic import BaseModel

router = APIRouter()
session_manager = SessionManager()

class SessionCreate(BaseModel):
    """Request model for session creation."""
    name: str
    context_id: str
    metadata: Optional[Dict] = None

class SessionUpdate(BaseModel):
    """Request model for session update."""
    metadata: Optional[Dict] = None

@router.post("/", response_model=Dict)
async def create_session(session: SessionCreate):
    """Create a new session."""
    result = session_manager.create_session(
        name=session.name,
        context_id=session.context_id,
        metadata=session.metadata
    )
    return result.to_dict()

@router.get("/{session_id}", response_model=Dict)
async def get_session(session_id: str):
    """Get a session by ID."""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session.to_dict()

@router.put("/{session_id}", response_model=Dict)
async def update_session(session_id: str, update: SessionUpdate):
    """Update an existing session."""
    session = session_manager.update_session(
        session_id=session_id,
        metadata=update.metadata
    )
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session.to_dict()

@router.post("/{session_id}/end", response_model=Dict)
async def end_session(session_id: str):
    """End a session."""
    session = session_manager.end_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session.to_dict()

@router.get("/", response_model=List[Dict])
async def list_sessions(active_only: bool = False):
    """List all sessions."""
    return session_manager.list_sessions(active_only=active_only)

@router.get("/context/{context_id}", response_model=List[Dict])
async def get_sessions_by_context(context_id: str, active_only: bool = False):
    """Get all sessions for a specific context."""
    return session_manager.get_sessions_by_context(
        context_id=context_id,
        active_only=active_only
    )