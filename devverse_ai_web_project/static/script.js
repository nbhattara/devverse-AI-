async function sendMessage() {
  const user_input = document.getElementById("userInput").value;
  const responseBox = document.getElementById("responseBox");

  responseBox.textContent = "Thinking...";

  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ user_input }),
  });

  const data = await res.json();
  responseBox.textContent = data.response || data.error || "No response.";
}
