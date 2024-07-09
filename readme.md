## Setting Up Flask To-Do Application with Keycloak

### Prerequisites
- Docker Compose installed on your system.
### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Aadilkhan2001/todo_graphql_backend.git
   cd todo_graphql_backend
   ```

2. **Create a `.env` File**

   Create a `.env` file in the root directory with the following environment variables:

   ```
   ENVIRONMENT=<env-mode>
   DATABASE_NAME=<your-database-name>
   DATABASE_USER=<your-database-name>
   DATABASE_PASSWORD=<your-database-password>
   DATABASE_HOST=<your-database-host>
   KEYCLOAK_SERVER_URL=http://keycloak:8080
   KEYCLOAK_REALM=<your-realm-name>
   KEYCLOAK_USER=<your-admin-user>
   KEYCLOAK_PASSWORD=<your-admin-password>
   KEYCLOAK_CLIENT_ID=<your-client-name>
   KEYCLOAK_CLIENT_SECRET=<your-client-secret>
   ```
   
3. **Update `etc/hosts` (Linux/macOS) or `hosts` file (Windows)**

   Add the following entry to your `etc/hosts` (Linux/macOS) or `hosts` file (Windows):

   ```
   127.0.0.1   keycloak
   ```

   This allows your system to resolve `keycloak` to `localhost`.

4. **Docker Compose**

   Run the following command to build and start the Docker containers:

   ```bash
   docker-compose up --build
   ```

   This command will build your Docker images and start the flask and keyclaok services.

5. **Keycloak Configuration**

   - Access Keycloak admin console at `http://keycloak:8080/auth`.
   - Log in using the admin credentials (specified in env vars).
   - Create a new realm.
   - Create a client with Client ID and configure its settings (e.g., set Access Type to `confidential` and configure Valid Redirect URIs to `http://localhost:5173/auth/*`.
   - Note : `http://localhost:5173/auth/*` - This should be frontend url

6. **Run the Application**

   After Docker containers are up and running, you can access your Flask application at `http://localhost:5000`. Ensure that Keycloak and Flask services are running as expected.

### Accessing the Application

- **Flask Application**: `http://localhost:5000`
- **Keycloak Admin Console**: `http://keycloak:8080/auth`
