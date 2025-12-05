const csrftoken = getCookie("csrftoken");

fetch("http://localhost:8000/api/logout/", {
    method: "POST",
    credentials: "include",
    headers: {
        "X-CSRFToken": csrftoken
    },
})
.then(r => r.json())
.then(data => console.log(data));