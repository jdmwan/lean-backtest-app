let strategies = document.querySelectorAll('.draggable');
let workzone = document.querySelector('.workspace');

strategies.forEach(strategy => {
    strategy.addEventListener('dragstart', (event)=>{
        event.dataTransfer.setData('text/plain', strategy.innerHTML)
    })
});
workzone.addEventListener('dragover', (event) =>{
    event.preventDefault();
});
workzone.addEventListener('drop', (event) => {
    event.preventDefault();
    const data = event.dataTransfer.getData('text/plain');
    workZone.innerHTML += '<div class = "math-block">${data}</div>';
});

function runBacktest() {
    const short = document.getElementById("short").value;
    const long = document.getElementById("long").value;
    const cash = document.getElementById("cash").value;
    let lists = [];
    let sliders = document.querySelectorAll('.workspace input[type="range"]');
    sliders.forEach(slider => {
        lists.push({param:slider.id, value:slider.value})
    })
    payload = JSON.stringify(lists,null,2)
    // Show the loading indicator
    const loading = document.getElementById("loading-indicator");
    loading.style.display = "block";
    loading.innerHTML = "<strong style='color: orange;'>Running backtest...</strong>";

    fetch("/run-backtest", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: payload
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
