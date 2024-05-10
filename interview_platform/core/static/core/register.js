// JavaScript function to show a popup with a success message
function showSuccessPopup() {
    alert("Registration successful!");
    window.location.href = '/';  // Redirect to the homepage
}
// Prevent form submission and show success popup
document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("register-form");
    form.addEventListener("submit", function(event) {
        event.preventDefault();  // Prevent default form submission
        showSuccessPopup();       // Show success popup
    });
});