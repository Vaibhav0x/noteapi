# Note Taking API

This is a simple note-taking RESTful API built using Django Framework.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd noteapi
    ```
    Or
    ```bash
    git clone https://github.com/Vaibhav0x/noteapi.git
    cd noteapi
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the PostgreSQL database:
    - Create a new database in PostgreSQL.
    - Update the `DATABASES` setting in `noteapi/settings.py` with your database credentials.

    -PostgreSQL Download Link: `https://www.enterprisedb.com/downloads/postgres-postgresql-downloads`

    -After downloading and setup simply run the pgAdmin4 then enter password and in server in databases create new database to click on databases.
    -Enter the database name and owner is user that use in your `notes/settings.py` file to give update database name, user and password. 

4. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access Swagger documentation at:
    ```bash
    http://127.0.0.1:8000/swagger/
    ```

## API Endpoints

- `POST /api/notes/`: Create a new note.
- `GET /api/notes/<id>/`: Fetch a note by its primary key.
- `GET /api/notes?title=<substring>`: Query notes by title substring.
- `PUT /api/notes/<id>/update`: Update an existing note of this <id>.
- `DELETE /api/notes/<id>/update`: Delete an existing note of this <id>.

## Testing

Run tests using:
```bash
python manage.py test
