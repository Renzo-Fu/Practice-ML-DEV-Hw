document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Collect input data from the form
    const inputData = {
        N_Days: document.getElementById("N_Days").value,
        Age: document.getElementById("Age").value,
        Bilirubin: document.getElementById("Bilirubin").value,
        Cholesterol: document.getElementById("Cholesterol").value,
        Albumin: document.getElementById("Albumin").value,
    };

    // Make a POST request to the FastAPI endpoint
    fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(inputData),
    })
    .then(response => response.json())
    .then(data => {
        // Display the prediction result
        document.getElementById("predictionResult").innerText = `Prediction Result: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("predictionResult").innerText = 'Error: Could not retrieve prediction.';
    });
});
