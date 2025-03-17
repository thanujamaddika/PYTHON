async function checkText() {
    const inputText = document.getElementById("inputText").value;

    const response = await fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: inputText }),
    });

    if (response.ok) {
        const result = await response.json();

        // Display corrected text
        document.getElementById("correctedText").innerText = result.corrected_text;

        // Display grammar errors
        const grammarErrorsList = document.getElementById("grammarErrors");
        grammarErrorsList.innerHTML = ""; // Clear previous errors

        if (result.grammar_errors.length > 0) {
            result.grammar_errors.forEach(error => {
                const li = document.createElement("li");
                li.innerText = error;
                grammarErrorsList.appendChild(li);
            });
        } else {
            const li = document.createElement("li");
            li.innerText = "No grammar errors found.";
            grammarErrorsList.appendChild(li);
        }
    } else {
        console.error("Error:", response.statusText);
    }
}
