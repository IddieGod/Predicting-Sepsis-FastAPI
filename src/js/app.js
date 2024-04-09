// Wait for the DOM content to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    var form = document.getElementById('predictionForm');

    // Add a submit event listener to the form
    form.addEventListener('submit', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Get the form data
        var formData = new FormData(form);

        // Validate form inputs
        if (validateForm(formData)) {
            // Prepare the data for submission
            var jsonData = {};
            formData.forEach(function(value, key) {
                jsonData[key] = value;
            });

            // Convert the data to JSON
            var jsonDataString = JSON.stringify(jsonData);

            // Send a POST request to the prediction endpoint
            fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonDataString
            })
            .then(function(response) {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Failed to make prediction. Please try again.');
                }
            })
            .then(function(data) {
                // Handle the prediction response
                handlePredictionResponse(data);
            })
            .catch(function(error) {
                // Display an error message if prediction fails
                alert(error.message);
            });
        }
    });
});

// Function to validate form inputs
function validateForm(formData) {
    // Implement your form validation logic here
    // For simplicity, we'll assume all inputs are required and not empty
    for (var value of formData.values()) {
        if (!value) {
            alert('All fields are required. Please fill in all fields.');
            return false;
        }
    }
    return true;
}

// Function to handle prediction response
function handlePredictionResponse(data) {
    // Implement your logic to handle the prediction response here
    // For example, you can display the prediction result in a modal or update the UI accordingly
    if (data && data.output) {
        alert(data.output); // Display prediction output in an alert for demonstration
    } else {
        alert('Prediction response is invalid. Please try again.');
    }
}
