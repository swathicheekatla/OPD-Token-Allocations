Algorithm Explanation

Each doctor has fixed time slots.
Each slot can handle only a limited number of patients.

When patients book tokens:
- They are sorted based on priority.
- Emergency patients are given preference.

If a slot becomes full:
- Lower priority patients are not allowed.
- Emergency cases are always handled first.

If a patient cancels:
- The slot becomes free automatically.