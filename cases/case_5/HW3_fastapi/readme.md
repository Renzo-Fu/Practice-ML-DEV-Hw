# Cirrhosis Prediction Service

## Overview

This project is a machine learning service built with FastAPI to predict cirrhosis based on patient data. The service is complemented by a simple HTML form for user interaction.

# Running the FastAPI Service

1. **Install Dependencies**: Ensure you have the required Python packages installed. You can use a virtual environment for better isolation.

    ```bash
    pip install -r requirements.txt
    ```

2. **Run FastAPI Server**: Start the FastAPI server using Uvicorn.

    ```bash
    uvicorn main:app --reload
    ```

    The server will be running at http://127.0.0.1:8000.

3. **Run HTML Interface**: Open a new terminal and navigate to the directory containing the `index.html` file.

    ```bash
    python -m http.server
    ```

    The HTML form will be available at http://127.0.0.1:8000/index.html.

4. **Access the Application**: Open your web browser and navigate to http://localhost:8000/index.html. You should see the Cirrhosis Prediction form.

## Cirrhosis Prediction Form

Fill in the required patient data and click the "Predict" button to submit the form. The prediction result will be displayed on the page.

![Cirrhosis Prediction Form](https://github.com/Renzo-Fu/Practice-ML-DEV-Hw/blob/master/cases/case_5/HW3_fastapi/myapp.png)


Certainly! Below is an example of how you might write the instructions for running a service using Docker and Uvicorn in a `README.md` file for a GitHub repository. This example assumes you have a FastAPI application and you are looking to containerize it for easy deployment and execution.

---

# Running the Service with Docker and Uvicorn

This guide provides step-by-step instructions on how to run the service using Docker and Uvicorn. Docker simplifies deployment by packaging the application and its environment into a container. Uvicorn is an ASGI server implementation, perfect for running our FastAPI application.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker: [Get Docker](https://docs.docker.com/get-docker/)
- Docker Compose (optional, for multi-container deployment): [Install Docker Compose](https://docs.docker.com/compose/install/)

## Steps

1. **Clone the Repository:**
   Start by cloning the repository to your local machine.

   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Create a Dockerfile:**
   If you haven't already, create a `Dockerfile` in the root of your project with the following content:

   ```Dockerfile
   # Use an official Python runtime as a parent image
   FROM python:3.8-slim

   # Set the working directory in the container
   WORKDIR /usr/src/app

   # Copy the current directory contents into the container at /usr/src/app
   COPY . .

   # Install any needed packages specified in requirements.txt
   RUN pip install --no-cache-dir -r requirements.txt

   # Make port available to the world outside this container
   EXPOSE 8000

   # Define environment variable
   ENV NAME World

   # Run app.py when the container launches
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

   Replace `main:app` with the appropriate module and application instance for your FastAPI app.

3. **Build the Docker Image:**
   Build your Docker image using the following command:

   ```bash
   docker build -t my-fastapi-app .
   ```

4. **Run the Docker Container:**
   Once the build completes, run your container:

   ```bash
   docker run -d --name my-container -p 8000:8000 my-fastapi-app
   ```

   This command runs the container in detached mode, maps port 8000 inside the container to port 8000 on your host machine, and names the container `my-container`.

5. **Verify the Deployment:**
   Your FastAPI application should now be running on `http://localhost:8000`. You can access it using your web browser or tools like `curl`.

6. **Stopping the Container:**
   To stop the running container, use:

   ```bash
   docker stop my-container
   ```

## Using Docker Compose (Optional)

If you prefer to use Docker Compose, create a `docker-compose.yml` file with the following content:

```yaml
version: '3'
services:
  web:
    build: .
    command: uvicorn main:app --host 0.0.0.0 --port 8000
    ports:
      - "8000:8000"
```

Then, you can start your service with:

```bash
docker-compose up
```

And stop it with:

```bash
docker-compose down
```


## Troubleshooting

If you encounter any issues, please check the terminal where the FastAPI server is running for error messages. Ensure all dependencies are installed and that the servers are running simultaneously.

## Author

Renzo Flores

Feel free to reach out for any questions or improvements!
