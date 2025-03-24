"""
API endpoints for context management.
"""
from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, List, Optional
from app.core.context import ContextManager
from pydantic import BaseModel

router = APIRouter()
context_manager = ContextManager()

class ContextCreate(BaseModel):
    """Request model for context creation."""
    name: str
    content: Dict
    metadata: Optional[Dict] = None

class ContextUpdate(BaseModel):
    """Request model for context update."""
    content: Dict
    metadata: Optional[Dict] = None

@router.post("/", response_model=Dict)
async def create_context(context: ContextCreate):
    """Create a new context."""
    result = context_manager.create_context(
        name=context.name,
        content=context.content,
        metadata=context.metadata
    )
    return result.to_dict()

@router.get("/{context_id}", response_model=Dict)
async def get_context(context_id: str):
    """Get a context by ID."""
    context = context_manager.get_context(context_id)
    if not context:
        raise HTTPException(status_code=404, detail="Context not found")
    return context.to_dict()

@router.put("/{context_id}", response_model=Dict)
async def update_context(context_id: str, update: ContextUpdate):
    """Update an existing context."""
    context = context_manager.update_context(
        context_id=context_id,
        content=update.content,
        metadata=update.metadata
    )
    if not context:
        raise HTTPException(status_code=404, detail="Context not found")
    return context.to_dict()

@router.delete("/{context_id}")
async def delete_context(context_id: str):
    """Delete a context."""
    success = context_manager.delete_context(context_id)
    if not success:
        raise HTTPException(status_code=404, detail="Context not found")
    return {"status": "success", "message": "Context deleted"}

@router.get("/", response_model=List[Dict])
async def list_contexts():
    """List all contexts."""
    return context_manager.list_contexts()