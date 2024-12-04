# Interactive Grant Tracker Backend

This repository contains the backend implementation for the Interactive Grant Tracker. It is built using Flask and Flask-SQLAlchemy.

## Setup Instructions
  1. Clone the repository:
     ```bash
     git clone https://github.com/your-username/your-repo-name.git
     cd your-repo-name
     ```

  2. Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

  3. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

  4. Run the application:
     ```bash
     python run.py
     ```

  ## Repository Structure
  ```plaintext
  backend/
  ├── app/
  │   ├── __init__.py      # App factory and initialization
  │   ├── models.py        # Database models
  │   ├── routes.py        # API routes
  │   ├── services.py      # Business logic
  │   ├── utils.py         # Utility functions
  ├── config.py            # Configuration settings
  ├── requirements.txt     # Python dependencies
  ├── run.py               # Application entry point
  ├── venv/                # Virtual environment (not tracked in Git)
  └── .gitignore           # Ignored files
  ```

  ## Contributing
  Contributions are welcome! Please open an issue or submit a pull request.
  ```
