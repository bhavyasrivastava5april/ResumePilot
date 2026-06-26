document.querySelector("button").addEventListener("click", () => {

    const btn = document.querySelector("button");

    btn.innerHTML = "Analyzing...";

    setTimeout(() => {
        btn.innerHTML = "Analysis Complete";
    }, 2000);

});