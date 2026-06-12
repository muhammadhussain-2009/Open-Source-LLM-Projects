import asyncio
import uuid
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.database import init_db, kill_engine, get_session
from app import crud
from app.schemas import TaskCreate, TaskRead, TaskUpdate


app = FastAPI(title="Async TODO API")


async def _get_db():
	async with get_session() as session:
		yield session


@app.on_event("startup")
async def on_startup() -> None:
	await init_db()


@app.on_event("shutdown")
async def on_shutdown() -> None:
	await kill_engine()


@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc: ValidationError):
	return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": exc.errors()})


@app.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate, session=Depends(_get_db)):
	return await crud.create_task(session, task)


@app.get("/tasks", response_model=List[TaskRead])
async def read_tasks(only_pending: bool = False, session=Depends(_get_db)):
	return await crud.list_tasks(session, only_pending=only_pending)


@app.get("/tasks/{task_id}", response_model=TaskRead)
async def read_task(task_id: uuid.UUID, session=Depends(_get_db)):
	task = await crud.get_task(session, task_id)
	if not task:
		raise HTTPException(status_code=404, detail="Task not found")
	return task


@app.patch("/tasks/{task_id}", response_model=TaskRead)
async def patch_task(task_id: uuid.UUID, task_update: TaskUpdate, session=Depends(_get_db)):
	task = await crud.update_task(session, task_id, task_update)
	if not task:
		raise HTTPException(status_code=404, detail="Task not found")
	return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_task(task_id: uuid.UUID, session=Depends(_get_db)):
	ok = await crud.delete_task(session, task_id)
	if not ok:
		raise HTTPException(status_code=404, detail="Task not found")
	return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)


@app.get("/")
async def root():
	return {"status": "ok"}


if __name__ == "__main__":
	import uvicorn

	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
