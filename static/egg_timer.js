function startTimer(seconds) {
    let remaining = seconds;

    const display = document.getElementById("countdown");

    const interval = setInterval(() => {
        let mins = Math.floor(remaining / 60);
        let secs = remaining % 60;

        display.textContent = `${mins}:${secs.toString().padStart(2, "0")}`;

        if (remaining <= 0) {
            clearInterval(interval);
            display.textContent = "Your egg is ready! 🍳";
            alert("Your egg is ready!");
        }

        remaining--;
    }, 1000);
}
