def test_create_task_api(client):
    response = client.post(
        "/tasks/",
        json={
            "title": "API Тестовая задача",
            "description": "API Тестовое описание",
            "status": "created",
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "API Тестовая задача"
    assert data["status"] == "created"
    # Проверяем что ID является валидным UUID строкой
    assert len(data["id"]) == 36  # Длина UUID строки


def test_get_task_api(client):
    # Создадим задачу
    create_response = client.post(
        "/tasks/", json={"title": "Test Task", "description": "Тестовое описание"}
    )
    task_id = create_response.json()["id"]

    # Получим её
    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == task_id
    assert data["title"] == "Test Task"


def test_get_nonexistent_task_api(client):
    response = client.get("/tasks/non-existent-uuid")
    assert response.status_code == 404


def test_get_tasks_api(client):
    # Создаём несколько задач
    for i in range(3):
        client.post(
            "/tasks/", json={"title": f"Task {i}", "description": f"Description {i}"}
        )

    response = client.get("/tasks/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3


def test_update_task_api(client):
    # Создаём задачу
    create_response = client.post(
        "/tasks/",
        json={"title": "Original Title", "description": "Original Description"},
    )
    task_id = create_response.json()["id"]

    # Обновляем
    update_response = client.put(
        f"/tasks/{task_id}", json={"title": "Updated Title", "status": "in_progress"}
    )

    assert update_response.status_code == 200
    data = update_response.json()
    assert data["title"] == "Updated Title"
    assert data["status"] == "in_progress"
    assert data["description"] == "Original Description"


def test_delete_task_api(client):
    # Создаём задачу
    create_response = client.post(
        "/tasks/", json={"title": "Task to delete", "description": "Will be deleted"}
    )
    task_id = create_response.json()["id"]

    # Убедимся что задача существует
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200

    # Удаляем её
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200

    # Убедимся что задача удалена
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
