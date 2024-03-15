#Flask Page

This is a web application project developed with Flask, a Python microframework. The application is a simple web page that uses PostgreSQL as its database.

#Project Structure

/FLASK_PAGE
    run.py
    docker-compose.yml
    Dockerfile
    requirements.txt    
    /app_page
        /static
            /css
            /images
        /templates
            index.html
            models.py
            views.py
        __init__.py
        database.py
        models.py
        views.py

#Environment Variables

This project uses environment variables to configure the PostgreSQL database. Create a .env file in the same directory as the docker-compose.yml file with the following variables:

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=database_name

Replace user, password, and database_name with your PostgreSQL username, password, and database name, respectively.

#How to Run the Project

Clone this repository to your local machine.
Navigate to the project directory.
Run the command docker-compose up --build to start the Docker services.
Access http://localhost:5000 in your browser to see the application running.

#Technologies Used

Python: Programming language used to develop the application.
Flask: Python microframework used to create the web application.
PostgreSQL: Database management system used to store the application's data.
Docker: Platform used to containerize the application and its dependencies.
Contributions
Contributions to this project are welcome! Please open an issue or a pull request to contribute.

#License

This project is licensed under the MIT license. See the LICENSE file for more details.
