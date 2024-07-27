chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getUrl") {
        const apiUrl = "http://127.0.0.1:8000/check_url/"; // Your Django endpoint
        fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: request.url })
        })
        .then(response => response.json())
        .then(data => {
            if (data.result === 1) {
                alert("Warning: This website is a phishing site!");
            } else {
                alert("This website is legitimate.");
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }
});
