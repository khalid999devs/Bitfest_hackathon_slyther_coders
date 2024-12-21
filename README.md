# Mofa’s Kitchen Buddy

## Project Overview

Mofa’s Kitchen Buddy is a backend system designed to help manage ingredients and suggest recipes based on available items. It includes a chatbot interface for personalized recipe recommendations.

---

## Steps to Run Locally

### Prerequisites

1. Install [Python](https://www.python.org/) (version 3.8 or above).
2. Install [Git](https://git-scm.com/).
3. Ensure you have a package manager like pip installed.

### Setup Instructions

1. Clone the repository:

   git clone <repository-url>

2. Navigate to the project directory:

   cd project-root/challenge_2

3. Create a virtual environment and activate it:

   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

4. Install dependencies:

   pip install -r requirements.txt

5. Run the backend server:

   python app.py

### Navigating the Application

1. _Ingredient Management_:
   - Use endpoints to add, update, or retrieve ingredients.
2. _Recipe Management_:
   - Manage recipes via API endpoints.
3. _Chatbot Interaction_:
   - Query the chatbot for personalized recipe suggestions.

### Testing (Optional)

1. Run test cases:

   pytest tests/

### apis

```json
{
  "id": 1,
  "name": "Potato",
  "quantity": 20.0,
  "unit": "5"
}
```

- Route: http://127.0.0.1:8000/kitchen/input-ingredients
  Method: POST
  Sample Payload:

```json
{
  "name": "Potato",
  "quantity": 20,
  "unit": 5
}
```

---

## Contributions

1. Fork the repository and create a feature branch.
2. Commit changes and open a pull request.

---

## License

This project is licensed under the MIT License.
