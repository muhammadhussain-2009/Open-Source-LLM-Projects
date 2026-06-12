import uuid 
from collections.abc import AsyncGenerator
from collections.abc import Sequence 
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.models import Task
from app.schemas import TaskCreate, TaskRead, TaskUpdate

async def create_task(session: AsyncSession, task_create: TaskCreate) -> Task:
    task = Task(title=task_create.title, description=task_create.description)
    session.add(task)
    await session.flush()
    await session.commit()
    await session.refresh(task)
    return task 

async def get_task(session: AsyncSession, task_id: uuid.UUID) -> Task|None:
    return await session.get(Task, task_id)
    
async def list_tasks(session: AsyncSession, *, only_pending: bool = False) -> Sequence[Task]:
    stmt = select(Task)
    if only_pending:
        # assume Task has a boolean 'completed' field
        try:
            stmt = stmt.where(Task.completed == False)
        except AttributeError:
            # fallback: if 'completed' doesn't exist, return empty list
            return []

    result = await session.execute(stmt)
    return result.scalars().all()

async def update_task(session: AsyncSession, task_id: uuid.UUID, task_update: TaskUpdate) -> Task|None:
    task = await session.get(Task, task_id)
    if not task:
        return None
    changes= task_update.model_dump(exclude_unset=True)
    for key, value in changes.items():
        setattr(task, key, value)
    await session.flush()
    await session.refresh(task)
    return task

async def delete_task(session: AsyncSession, task_id: uuid.UUID) -> bool:
    task = await session.get(Task, task_id)
    if not task:
        return False
    await session.delete(task)
    await session.flush()
    return True