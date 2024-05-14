# Web Services and Application Project 
This Flask application manages a database of pubs, enabling features such as adding, updating, and deleting pub entries through a web interface and an API.

## Initial Setup

### Dependencies
- Flask
- SQLAlchemy
- MySQL

### Configuration
- Initialize Flask and configure it to connect to a MySQL database named `pubs_db`.
- Connection string and credentials should be properly set up in your Flask application configuration.

## Application Structure

### `app.py`

#### Imports and Configurations
- Necessary modules such as Flask, SQLAlchemy, and other Flask extensions are imported.
- The Flask app is initialized and connected to the MySQL database.

#### Database Setup with SQLAlchemy
- An SQLAlchemy object is linked to the Flask app to integrate with an SQL database.
- Defines a `Pub` class as a model for the database table with fields like `id`, `name`, `address`, and others.

#### Web Routes and API Endpoints
- **Index Route (`/`)**: Returns the `index.html` as the homepage.
- **API Endpoints for Handling Multiple Pubs (`/api/pubs`)**:
  - **GET Request**: Fetches a list of all pubs in JSON format.
  - **POST Request**: Adds a new pub to the database and returns details of the added pub in JSON.
- **API Endpoints for Handling a Single Pub (`/api/pubs/<int:pub_id>`)**:
  - **GET Request**: Returns details of a specific pub.
  - **PUT Request**: Updates specific fields of a pub.
  - **DELETE Request**: Deletes a pub from the database.

### `index.html`

#### Document Structure and Metadata
- Defines the document type and language.
- Includes metadata such as character set, viewport settings, and page title.

#### Content and Layout
- **Header**: Displays the main heading "Pubs in Ireland."
- **Main Section**:
  - **Form**: Allows adding or updating pubs.
  - **List of Pubs**: Dynamically displays pubs fetched from the database.

#### Client-Side Scripts
- Utilizes jQuery for DOM manipulations and AJAX operations.

### `scripts.js`

#### Functionality
- Handles HTTP requests, DOM manipulation, and event handling using jQuery.
- **Functions**:
  - **fetchPubs()**: Fetches and displays the list of pubs.
  - **Form Submission Handler**: Manages add and update operations.
  - **editPub()**: Loads pub data into the form for editing.
  - **deletePub()**: Confirms and deletes a pub.

## Running the Application

Ensure all dependencies are installed:
```bash
pip install flask sqlalchemy mysql-connector-python

