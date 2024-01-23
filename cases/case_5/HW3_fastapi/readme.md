# Cirrhosis Prediction Service

## Overview

This project is a machine learning service built with FastAPI to predict cirrhosis based on patient data. The service is complemented by a simple HTML form for user interaction.

## Running the FastAPI Service

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


## Troubleshooting

If you encounter any issues, please check the terminal where the FastAPI server is running for error messages. Ensure all dependencies are installed and that the servers are running simultaneously.

## Author

Renzo Flores

Feel free to reach out for any questions or improvements!
