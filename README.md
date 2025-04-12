todo_app
This is simple ToDo project made in Python utilizing Swagger (due to problems with working with Docker I choose to not use it, it would always create errors that I couldn't locate and fix). Guide for installation and use:

Install dependencies: bash Copy pip install -r requirements.txt
Run the application: docker-compose up --build
Access the application: Swagger will be at: http://localhost:8080/docs

Authentication:
You can authenticate by sending a POST request to /token with the username and password.
Please replace `username` and `password` in `DATABASE_URL` with your PostgreSQL credentials. The implementation is kept simple for educational purposes and lacks robust user management and security measures. Make sure to implement real authentication logic and secure your secret key.