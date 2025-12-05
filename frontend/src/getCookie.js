console.log('hello from getCOokie.js');

export default function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {
        // Split cookie string into individual key=value pairs
        const cookies = document.cookie.split(";");

        console.log('inside getCookie', cookies)

        for (let cookie of cookies) {
            cookie = cookie.trim(); // remove leading/trailing spaces

            // Check if cookie starts with "name="
            if (cookie.startsWith(name + "=")) {
                // Decode the value and return
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}
