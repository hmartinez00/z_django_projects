const loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", function(e) {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  // Validate username and password
  if (username === "admin" && password === "password") {
    window.location.href = "success.html";
  } else {
    alert("Invalid username or password!");
    loginForm.reset();
  }
});
