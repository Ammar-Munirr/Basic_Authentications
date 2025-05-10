## Setup and Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
2. Navigate to the project directory:
    ```bash
   cd Basic_Authentications
3. Create a virtual environment (recommended) and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
4. Crete a .env file within the project directory and setup the variables refer to the .env.example file:

5. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
## Usage

1. Migrate the database:

   ```bash
   python manage.py migrate
2. Start the development server:

    ```bash
    python manage.py runserver
3. Access the app in your web browser at http://localhost:8000/.
