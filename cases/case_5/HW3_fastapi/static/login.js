document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Collect input data from the form
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Make a POST request to the FastAPI authentication endpoint
    fetch('/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `grant_type=password&username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Login failed');
        }
        return response.json();
    })
    .then(data => {
        // Handle successful login, e.g., store access token and redirect to main page
        localStorage.setItem('access_token', data.access_token);
        window.location.href = '/'; // Redirect to the main page
    })
    .then(data => {
        // Handle successful login, e.g., store access token and redirect to main page
        localStorage.setItem('access_token', data.access_token);
        window.location.href = 'index.html'; // Redirect to the index page
    })
    
    .catch(error => {
        console.error('Login Error:', error);
        document.getElementById("loginResult").innerText = 'Login failed. Please check your credentials.';
    });
});
