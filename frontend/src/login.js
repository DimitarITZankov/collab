import getCookie from './getCookie.js'

const csrftoken = getCookie("csrftoken");

const form = document.getElementById("login-form");
const statusText = document.getElementById("status");

console.log('csrftoken:', csrftoken)
console.log('hello from login.js')

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value;
    console.log('username', username)
    const password = document.getElementById("password").value;
    console.log('username', username)

    const response = await fetch("http://localhost:8000/api/login/", {
        method: "POST",
        credentials: "include",  // This allows cookies to be sent/received
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (response.ok) {
        statusText.textContent = "Logged in!";
    } else {
        statusText.textContent = "Error: " + data.detail;
    }
});