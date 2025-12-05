console.log('hello from whoami.js')

// Test function
const button = document.getElementById("whoami-button");

button.addEventListener("click", async () => {
    const response = await fetch("http://localhost:8000/api/whoami/", {
        method: "GET",
        credentials: "include",
    });
    const data = await response.json();
    console.log(data);
});