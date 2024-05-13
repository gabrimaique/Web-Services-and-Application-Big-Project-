# Flask Pubs Management Application

This Flask application is designed to manage a database of pubs, including functionalities for adding, updating, and deleting pub entries. It features a user-friendly web interface and an API to handle requests.

## Initial Setup

### Dependencies
- Flask
- SQLAlchemy
- MySQL

### Configuration
- The application connects to a MySQL database at `pubs_db`.
- Ensure the database credentials are set in your configuration files.

## File Descriptions

### `app.py`
- **Functionality**: Manages the Flask application setup, routes, and API endpoints.
- **Database Setup**: Utilizes SQLAlchemy for ORM capabilities.
- **Routes**:
  - Index (`/`): Returns `index.html`, the homepage.
  - API endpoints for handling multiple pubs (`/api/pubs`) with GET and POST requests.
  - API endpoints for handling a single pub (`/api/pubs/<int:pub_id>`) with GET, PUT, and DELETE requests.

### `index.html`
- **Overview**: Serves as the front-end interface.
- **Features**: Form for adding/updating pubs, list of pubs, and client-side scripts for interaction.
- **Scripts**: Includes jQuery for DOM manipulation and AJAX operations.

### `scripts.js`
- **Purpose**: Handles AJAX requests to the Flask API, form submissions, and dynamic content updates.
- **Key Functions**:
  - `fetchPubs()`: Fetches and displays pubs.
  - Form submission handler: Manages add and update operations.
  - `editPub()`: Loads pub data for editing.
  - `deletePub()`: Handles the deletion of pub entries.

## Running the Application

1. Ensure all dependencies are installed:
   ```bash
   pip install flask sqlalchemy mysql-connector-python
