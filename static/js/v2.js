document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();
  
    // Form fields
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirmPassword = document.getElementById("confirmPassword").value.trim();
  
    // Error elements
    const usernameError = document.getElementById("usernameError");
    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");
    const confirmPasswordError = document.getElementById("confirmPasswordError");
  
    // Reset error messages
    usernameError.style.display = "none";
    emailError.style.display = "none";
    passwordError.style.display = "none";
    confirmPasswordError.style.display = "none";
  
    let isValid = true;
  
    // Username validation
    if (username.length < 3) {
      usernameError.textContent = "Username must be at least 3 characters.";
      usernameError.style.display = "block";
      isValid = false;
    }
  
    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      emailError.textContent = "Invalid email format.";
      emailError.style.display = "block";
      isValid = false;
    }
  
    // Password validation
    if (password.length < 6) {
      passwordError.textContent = "Password must be at least 6 characters.";
      passwordError.style.display = "block";
      isValid = false;
    }
  
    // Confirm Password validation
    if (password !== confirmPassword) {
      confirmPasswordError.textContent = "Passwords do not match.";
      confirmPasswordError.style.display = "block";
      isValid = false;
    }
  
    // If valid, redirect to success page
    if (isValid) {
      window.location.href = "";
    }
  });
  