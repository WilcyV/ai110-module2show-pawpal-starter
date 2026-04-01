from pawpal_system import Owner, Pet, Task, Scheduler


def test_mark_complete():
    task = Task(title="Give medicine", duration_minutes=5, priority="high")
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet(name="Mochi", species="dog")
    task = Task(title="Morning walk", duration_minutes=20, priority="high")
    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].title == "Morning walk"


def test_scheduler_sorts_high_priority_first():
    scheduler = Scheduler()
    tasks = [
        Task(title="Brush fur", duration_minutes=15, priority="low"),
        Task(title="Feed pet", duration_minutes=10, priority="high"),
        Task(title="Play time", duration_minutes=20, priority="medium"),
    ]

    sorted_tasks = scheduler.sort_tasks(tasks)

    assert sorted_tasks[0].title == "Feed pet"
    assert sorted_tasks[1].title == "Play time"
    assert sorted_tasks[2].title == "Brush fur"


def test_scheduler_respects_available_time():
    owner = Owner(name="Jordan", available_minutes=25)
    pet = Pet(name="Mochi", species="dog")
    scheduler = Scheduler()

    pet.add_task(Task(title="Morning walk", duration_minutes=20, priority="high"))
    pet.add_task(Task(title="Feed pet", duration_minutes=10, priority="high"))
    pet.add_task(Task(title="Brush fur", duration_minutes=15, priority="low"))

    plan = scheduler.generate_daily_plan(owner, pet)

    assert plan["time_used"] <= owner.available_minutes


def test_completed_tasks_are_not_scheduled():
    owner = Owner(name="Jordan", available_minutes=60)
    pet = Pet(name="Mochi", species="dog")
    scheduler = Scheduler()

    completed_task = Task(
        title="Give medicine",
        duration_minutes=5,
        priority="high",
        completed=True
    )
    pet.add_task(completed_task)

    plan = scheduler.generate_daily_plan(owner, pet)

    assert len(plan["selected"]) == 0