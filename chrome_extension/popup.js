document.addEventListener('DOMContentLoaded', function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        const activeTab = tabs[0];
        const apiUrl = "http://127.0.0.1:8000/check_url/"; // Your Django endpoint
        fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: activeTab.url })
        })
        .then(response => response.json())
        .then(data => {
            const statusDiv = document.getElementById('status');
            if (data.result === 1) {
                statusDiv.textContent = "Warning: This website is a phishing site!";
                statusDiv.className = "phishing";
            } else {
                statusDiv.textContent = "This website is legitimate.";
                statusDiv.className = "legitimate";
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
