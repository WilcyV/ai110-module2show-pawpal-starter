from dataclasses import dataclass, field
from typing import List


PRIORITY_VALUES = {
    "high": 3,
    "medium": 2,
    "low": 1,
}


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    category: str = "general"
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def priority_value(self) -> int:
        """Return numeric value for sorting priority."""
        return PRIORITY_VALUES.get(self.priority.lower(), 0)


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def edit_task(self, index: int, new_task: Task) -> bool:
        """Edit a task by index."""
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            return True
        return False

    def remove_task(self, index: int) -> bool:
        """Remove a task by index."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

    def get_incomplete_tasks(self) -> List[Task]:
        """Return only incomplete tasks."""
        return [task for task in self.tasks if not task.completed]


@dataclass
class Owner:
    name: str
    available_minutes: int
    preferences: List[str] = field(default_factory=list)


class Scheduler:
    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by priority first, then by shorter duration."""
        return sorted(
            tasks,
            key=lambda task: (-task.priority_value(), task.duration_minutes, task.title.lower())
        )

    def generate_daily_plan(self, owner: Owner, pet: Pet) -> dict:
        """
        Build a daily plan based on available time and task priority.
        Higher priority tasks are chosen first.
        If priorities tie, shorter tasks come first.
        """
        available_tasks = pet.get_incomplete_tasks()
        sorted_tasks = self.sort_tasks(available_tasks)

        selected = []
        skipped = []
        time_used = 0
        time_left = owner.available_minutes

        for task in sorted_tasks:
            if task.duration_minutes <= time_left:
                selected.append(task)
                time_left -= task.duration_minutes
                time_used += task.duration_minutes
            else:
                skipped.append(task)

        return {
            "selected": selected,
            "skipped": skipped,
            "time_used": time_used,
            "time_left": time_left,
        }

    def explain_plan(self, selected: List[Task], skipped: List[Task], owner: Owner) -> List[str]:
        """Explain why tasks were selected or skipped."""
        explanations = []

        for task in selected:
            explanations.append(
                f"Included '{task.title}' because it fit within the {owner.available_minutes} available minutes "
                f"and had {task.priority} priority."
            )

        for task in skipped:
            explanations.append(
                f"Skipped '{task.title}' because there was not enough time left in the day."
            )

        return explanations