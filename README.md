# CrudRest_API

Project Details:

1. This project is a simple RESTful API for managing client information in a MySQL database. It provides endpoints for creating, reading, updating, and deleting client records.
2. The API is built using the Flask framework and connects to the MySQL database using the pymysql library.

Installation Instructions:

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running pip install flask pymysql in your command prompt or terminal.
3. Set up a MySQL database and configure the connection details in the config.py file.
4. Copy the provided code into a Python file (e.g., app.py).
5. Run the application by executing the Python file (python app.py).

Database Schema:

1. The code assumes the existence of a MySQL database with a table named clients_info to store client information.
    The clients_info table should have the following columns:
        customer_id: INT (Primary Key) - The unique identifier for each client.
        customer_name: VARCHAR - The name of the client.
        customer_number: VARCHAR - The contact number of the client.
        customer_email_address: VARCHAR - The email address of the client.

Usage Examples:

1. To add a new client, send a POST request to the /create endpoint with the client details in the request body.
2. To retrieve all clients, send a GET request to the /get endpoint.
3. To retrieve a specific client by ID, send a GET request to the /get/<customer_id> endpoint, replacing <customer_id> with the actual ID.
4. To update a client, send a PUT request to the /update endpoint with the updated client details in the request body.
5. To delete a client by ID, send a DELETE request to the /delete/<customer_id> endpoint, replacing <customer_id> with the actual ID.

Error Handling:

1. The API includes error handling for different scenarios.
2. If an invalid token is provided in the Authorization header, a JSON response with an error message and a 401 status code (Unauthorized) is returned.
3. If a requested resource is not found (e.g., no clients found for a given ID), a JSON response with an appropriate error message and a 404 status code (Not Found) is returned.
4. If an unexpected exception occurs during the execution of the API endpoints, a generic error message and a 500 status code (Internal Server Error) are returned.


Additional Information:

1. The API uses token-based authentication. The authentication token is generated using the secrets module and printed when the application starts. You can modify the authentication mechanism according to your needs.
2. The API connects to the MySQL database using the connection details specified in the config.py file. Make sure to update the database configuration accordingly.
3. Error handling is implemented for cases such as invalid tokens, missing records, and general exceptions. The API returns appropriate JSON responses with status codes for different scenarios.
4. The application runs in debug mode (debug=True) to enable helpful error messages during development. Make sure to disable debug mode in a production environment.
5. The provided code is a basic implementation of CRUD operations and can be extended or modified to suit specific project requirements.