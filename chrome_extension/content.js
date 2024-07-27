chrome.runtime.sendMessage({
    action: "getUrl",
    url: window.location.href
});
