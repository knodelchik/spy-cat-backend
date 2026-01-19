# Spy Cat Agency - Backend API

This is the RESTful API for the Spy Cat Agency (SCA) management system. It handles the logic for managing spy cats, their missions, and specific targets. Built with **Django** and **Django REST Framework**.

## Features

- **Spy Cats Management:** CRUD operations for agents with validation.
- **Breed Validation:** Automatic validation of cat breeds via external `TheCatAPI`.
- **Mission Control:**
  - Create missions with 1-3 targets.
  - Assign cats to missions.
  - Strict validation (cannot delete a mission if a cat is assigned).
- **Target Tracking:**
  - Update notes and completion status.
  - **Logic Lock:** Notes become frozen (read-only) once the target or mission is completed.
  - Auto-completion of missions when all targets are finished.

## Tech Stack

- **Python 3.10+**
- **Django 4.2**
- **Django REST Framework**
- **SQLite** (Default database)
- **CORS Headers** (For frontend integration)

## Installation & Setup

1. Clone the repository:

    git clone <YOUR_BACKEND_REPO_URL>
    cd spy-cat-backend

2. Create and activate a virtual environment:

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    .\venv\Scripts\activate

3. Install dependencies:

    pip install -r requirements.txt

4. Apply migrations:

    python manage.py migrate

5. Run the development server:

    python manage.py runserver

The API will be available at http://127.0.0.1:8000/

## API Endpoints

### Spy Cats
- GET /cats/ - List all cats
- POST /cats/ - Create a new cat
- GET /cats/{id}/ - Retrieve a specific cat
- DELETE /cats/{id}/ - Remove a cat
- PATCH /cats/{id}/ - Update salary

### Missions & Targets
- POST /missions/ - Create a mission with targets (JSON body required)
- DELETE /missions/{id}/ - Delete a mission
- PATCH /missions/{id}/assign_cat/ - Assign a cat to a mission
- PATCH /targets/{id}/ - Update target notes or mark as complete

## Testing

The API is fully testable via Postman. Ensure validation rules (e.g., correct breeds) are followed when creating resources.