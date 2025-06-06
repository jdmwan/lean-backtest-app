function runBacktest() {
    const short = document.getElementById("short").value;
    const long = document.getElementById("long").value;
    const cash = document.getElementById("cash").value;

    // Show the loading indicator
    const loading = document.getElementById("loading-indicator");
    loading.style.display = "block";
    loading.innerHTML = "<strong style='color: orange;'>Running backtest...</strong>";

    fetch("/run-backtest", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        short_window: parseInt(short),
        long_window: parseInt(long),
        starting_cash: parseInt(cash)
      })
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").textContent = JSON.stringify(data, null, 2);
      loading.innerHTML = "<strong style='color: green;'>Backtest complete.</strong>";
      setTimeout(() => loading.style.display = "none", 1500);  // hide after 1.5s
    })
    .catch(err => {
      document.getElementById("output").textContent = "Error: " + err;
      loading.innerHTML = "<strong style='color: red;'>Error running backtest</strong>";
    });
  }