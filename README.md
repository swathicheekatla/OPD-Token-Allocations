OPD Token Allocation Engine

This project is a simple backend application used to manage OPD tokens in a hospital.

Patients are assigned tokens based on priority:
Emergency patients are handled first, followed by paid, follow-up, and walk-in patients.

The system automatically manages slot limits and cancellations.

Technologies Used:
- Python
- Flask

How to Run:
1. Install Flask using: pip install flask
2. Run the file: python app.py
3. Open browser and check: http://localhost:5000/status