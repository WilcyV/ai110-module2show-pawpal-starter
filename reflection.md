# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler.
The Owner class stores the owner's name, available time, and preferences.
The Pet class stores pet information and a list of tasks.
The Task class represents an individual pet care task with attributes such as title, duration, priority, and completion status.
The Scheduler class is responsible for sorting tasks, generating a daily plan, and explaining the plan.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, my design changed during implementation. At first, I thought of placing most of the scheduling behavior inside the Pet class. Later, I moved that logic into a separate Scheduler class because it made the design cleaner and more modular. This made it easier to test the scheduling behavior separately from the pet data.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler considers available time, task priority, and completion status.
The most important constraints were time and priority because the project scenario focuses on helping a busy pet owner choose the most important tasks that fit into the day.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is that it uses a simple greedy strategy instead of a more advanced optimization algorithm. It selects higher-priority tasks first and then checks whether they fit into the available time. This tradeoff is reasonable because the project is small, and the simpler logic makes the system easier to understand, explain, and test.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI tools for brainstorming the system design, generating class ideas, helping with debugging, and improving test cases. The most helpful prompts were the ones that asked for class responsibilities, scheduling logic ideas, and ways to simplify the implementation while still meeting the project requirements.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

There was a moment when I did not accept an AI suggestion exactly as it was given. I compared the suggestion to the actual project requirements and decided to simplify it so the final design would stay clean and readable. I verified the final code by running the app and by using pytest tests.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion, adding tasks to a pet, task sorting by priority, respecting available time, and excluding completed tasks from the daily plan. These tests were important because they checked the core behaviors of the scheduler.


**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident that my scheduler works correctly for the main required behaviors. If I had more time, I would also test more edge cases such as empty task lists, equal priorities, and invalid user input.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The part I am most satisfied with is separating the scheduling logic into its own class. This made the project more organized and easier to understand.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the UI so users could edit tasks more easily and I would add stronger preference-based scheduling.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned is that designing the system first makes implementation easier. I also learned that AI can be very useful, but I still need to verify and adjust its suggestions carefully.