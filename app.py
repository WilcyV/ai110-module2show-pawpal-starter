import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+.

This app helps a pet owner plan daily care tasks based on available time and task priority.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

with st.expander("What this app does", expanded=True):
    st.markdown(
        """
At minimum, this system:
- Represents pet care tasks
- Represents the pet and the owner
- Builds a daily plan based on constraints
- Explains why tasks were selected
"""
    )

st.divider()

st.subheader("Owner + Pet Info")
owner_name = st.text_input("Owner name", value="Jordan")
available_minutes = st.number_input(
    "Available time today (minutes)", min_value=1, max_value=600, value=60
)
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.divider()

st.subheader("Tasks")
st.caption("Add pet care tasks with duration and priority.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {
            "title": task_title,
            "duration_minutes": int(duration),
            "priority": priority,
        }
    )
    st.success(f"Added task: {task_title}")

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)

    st.markdown("### Manage tasks")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(
                f"{i + 1}. {task['title']} - {task['duration_minutes']} min - {task['priority']}"
            )
        with col2:
            if st.button(f"Delete {i+1}", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Daily Schedule")

if st.button("Generate schedule"):
    owner = Owner(name=owner_name, available_minutes=int(available_minutes))
    pet = Pet(name=pet_name, species=species)

    for task_data in st.session_state.tasks:
        pet.add_task(
            Task(
                title=task_data["title"],
                duration_minutes=task_data["duration_minutes"],
                priority=task_data["priority"],
            )
        )

    scheduler = Scheduler()
    plan = scheduler.generate_daily_plan(owner, pet)
    explanations = scheduler.explain_plan(plan["selected"], plan["skipped"], owner)

    st.markdown("### Selected Tasks")
    if plan["selected"]:
        selected_data = [
            {
                "Task": task.title,
                "Duration": task.duration_minutes,
                "Priority": task.priority,
            }
            for task in plan["selected"]
        ]
        st.table(selected_data)
        st.success(
            f"Plan created. Time used: {plan['time_used']} min | Time left: {plan['time_left']} min"
        )
    else:
        st.warning("No tasks could be scheduled.")

    st.markdown("### Skipped Tasks")
    if plan["skipped"]:
        skipped_data = [
            {
                "Task": task.title,
                "Duration": task.duration_minutes,
                "Priority": task.priority,
            }
            for task in plan["skipped"]
        ]
        st.table(skipped_data)
    else:
        st.info("No tasks were skipped.")

    st.markdown("### Why this plan was chosen")
    for reason in explanations:
        st.write(f"- {reason}")
        

        