# Mofa's Kitchen Buddy

## Project Overview

Mofa’s Kitchen Buddy is a backend system designed to help manage ingredients and suggest recipes based on available items. It includes a chatbot interface for personalized recipe recommendations, making it easy to cook with what you have!

---

## Steps to Run Locally

### Prerequisites

1. Install [Python](https://www.python.org/) (version 3.8 or above).
2. Install [Git](https://git-scm.com/).
3. Ensure you have a package manager like pip installed.

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the project directory:**

   ```bash
   cd project-root/challenge_2
   ```

3. **Create a virtual environment and activate it:**

   - For macOS/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the backend server:**
   ```bash
   python app.py
   ```

---

## Navigating the Application

1. **Ingredient Management:**

   - Use endpoints to add, update, or retrieve ingredients from the kitchen.

2. **Recipe Management:**

   - Manage recipes via API endpoints, including adding and retrieving recipes.

3. **Chatbot Interaction:**
   - Query the chatbot for personalized recipe suggestions based on available ingredients.

---

## API Endpoints

### 1. Add Ingredients

- **Route:** `/kitchen/input-ingredients`
- **Method:** `POST`

  **Sample Payload:**

  ```json
  {
    "name": "Potato",
    "quantity": 20,
    "unit": 5
  }
  ```

  **Response:**

  ```json
  {
    "id": 1,
    "name": "Potato",
    "quantity": 20.0,
    "unit": "5"
  }
  ```

---

### 2. Get Ingredients

- **Route:** `/kitchen/get-ingredients`
- **Method:** `GET`

  **Response:**

  ```json
  [
    {
      "id": 1,
      "name": "Potato",
      "quantity": 30.0,
      "unit": "5"
    }
  ]
  ```

---

### 3. Update Ingredients

- **Route:** `/kitchen/get-ingredients`
- **Method:** `PUT`

  **Sample Payload:**

  ```json
  {
    "name": "Potato",
    "quantity": 30,
    "unit": 5
  }
  ```

  **Response:**

  ```json
  {
    "id": 1,
    "name": "Potato",
    "quantity": 30.0,
    "unit": "5"
  }
  ```

---

### 4. Input Recipe

- **Route:** `/kitchen/input-recipe`
- **Method:** `POST`

  **Sample Payload:**

  ```json
  {
    "name": "Mushroom Risotto",
    "taste": "Savory",
    "cuisine_type": "Italian",
    "preparation_time": 40,
    "instructions": "Sauté mushrooms and garlic, cook rice in broth, stir in cheese.",
    "reviews": 5
  }
  ```

  **Response:**

  ```json
  {
    "id": 2,
    "name": "Mushroom Risotto",
    "instructions": "Sauté mushrooms and garlic, cook rice in broth, stir in cheese.",
    "taste": "Savory",
    "cuisine_type": "Italian",
    "preparation_time": 40,
    "reviews": "5",
    "ingredients": []
  }
  ```

---

### 5. Retrieve Recipes

- **Route:** `/kitchen/retrive`
- **Method:** `GET`

  **Response:**

  ```json
  {
    "message": "Recipes tuned successfully"
  }
  ```

---

### 6. Chat with the Bot

- **Route:** `/kitchen/chat`
- **Method:** `POST`

  **Sample Payload:**

  ```json
  {
    "user_input": "I want something sweet today"
  }
  ```

  **Response:**

  ```json
  {
    "response": "It sounds like you're craving something sweet! How about trying a simple yet delicious chocolate chip cookie recipe? Here's how you can make them:\n\n**Ingredients:**\n- 1 cup butter (softened)\n- 3/4 cup white sugar\n- 3/4 cup brown sugar (packed)\n- 2 eggs\n- 1 tsp vanilla extract\n- 2 1/4 cups all-purpose flour\n- 1/2 tsp baking soda\n- 1/2 tsp salt\n- 2 cups semi-sweet chocolate chips\n\n**Instructions:**\n1. Preheat your oven to 375°F (190°C).\n2. In a large bowl, cream together the softened butter, white sugar, and brown sugar until smooth.\n3. Add the eggs one at a time, beating well after each addition, and then stir in the vanilla extract.\n4. In a separate bowl, combine the flour, baking soda, and salt.\n5. Gradually add the dry ingredients to the wet mixture, stirring until well combined.\n6. Fold in the chocolate chips.\n7. Drop rounded spoonfuls of dough onto ungreased baking sheets, spacing them about 2 inches apart.\n8. Bake in the preheated oven for 10 minutes, or until the edges are golden brown.\n9. Allow the cookies to cool on the sheets for a few minutes before transferring them to wire racks to cool completely.\n\nEnjoy your freshly baked chocolate chip cookies! They’re perfect with a glass of milk or just as a treat on their own."
  }
  ```

---

## Contributions

1. Fork the repository and create a feature branch.
2. Commit changes and open a pull request for review.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

### Let me know if you'd like further details or improvements to this!
