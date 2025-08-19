from uuid import UUID
from app import schemas, crud
from app.models import TaskStatus


def test_create_task(db):
    task_data = schemas.TaskCreate(
        title="Test Task", description="Test Description", status=TaskStatus.CREATED
    )

    task = crud.create_task(db, task_data)

    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.status == TaskStatus.CREATED
    assert isinstance(task.id, str)
    # Проверяем что это валидный UUID
    UUID(task.id)  # Не должно вызывать исключение


def test_get_task(db):
    task_data = schemas.TaskCreate(title="Test Task", description="Test Description")

    # Создадим задачу
    created_task = crud.create_task(db, task_data)

    # Получим её
    retrieved_task = crud.get_task(db, created_task.id)

    assert retrieved_task is not None
    assert retrieved_task.id == created_task.id
    assert retrieved_task.title == "Test Task"


def test_get_tasks(db):
    # Создаём несколько задач
    for i in range(3):
        task_data = schemas.TaskCreate(
            title=f"Task {i}", description=f"Description {i}"
        )
        crud.create_task(db, task_data)

    tasks = crud.get_tasks(db)

    assert len(tasks) == 3
    assert all(task.title.startswith("Task") for task in tasks)


def test_update_task(db):
    task_data = schemas.TaskCreate(
        title="Original Title", description="Original Description"
    )

    # Создаём задачу
    created_task = crud.create_task(db, task_data)

    update_data = schemas.TaskUpdate(
        title="Updated Title", status=TaskStatus.IN_PROGRESS
    )

    # Обновляем
    updated_task = crud.update_task(db, created_task.id, update_data)

    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Original Description"
    assert updated_task.status == TaskStatus.IN_PROGRESS


def test_delete_task(db):
    task_data = schemas.TaskCreate(
        title="Task to delete", description="Will be deleted"
    )

    # Создаём задачу
    created_task = crud.create_task(db, task_data)

    # Убедимся что задача существует
    assert crud.get_task(db, created_task.id) is not None

    # Удаляем её
    deleted_task = crud.delete_task(db, created_task.id)

    # Убедимся что задача удалена
    assert deleted_task is not None
    assert crud.get_task(db, created_task.id) is None
