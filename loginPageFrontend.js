<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Login Page</title>
   <style>
       /* Add CSS styling here */
       body {
           font-family: Arial, sans-serif;
           margin: 0;
           padding: 0;
           text-align: center;
       }
       .container {
           margin-top: 100px;
       }
       input[type="text"], input[type="password"] {
           width: 200px;
           padding: 10px;
           margin-bottom: 10px;
       }
       button {
           padding: 10px 20px;
           background-color: #007bff;
           color: #fff;
           border: none;
           cursor: pointer;
       }
   </style>
</head>
<body>
   <div class="container">
       <h2>Login Page</h2>
       <label for="username">Username:</label><br>
       <input type="text" id="username"><br>
       <label for="password">Password:</label><br>
       <input type="password" id="password"><br><br>
       <button onclick="login()">Login</button>
   </div>


   <script>
       // JavaScript code for login functionality
       function login() {
           var enteredUsername = document.getElementById("username").value;
           var enteredPassword = document.getElementById("password").value;


           // Validation: Check if username and password are not empty
           if (enteredUsername.trim() === "" || enteredPassword.trim() === "") {
               alert("Please enter both username and password.");
               return;
           }


           if (enteredUsername === "user123" && enteredPassword === "user1234") {
               alert("Login Successful. Welcome, user123!");
               // Add code to proceed to the main application or perform further actions
           } else {
               alert("Login Failed. Invalid username or password");
           }
       }
   </script>
</body>
</html>


