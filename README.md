# Interactive Strategy Backtester

This project is a browser-based backtesting tool for quantitative trading strategies, built with Flask and integrated with the QuantConnect Lean CLI. It features a dynamic user interface with real-time parameter adjustment, enabling rapid experimentation with moving average crossover strategies.

## Features

- Real-time backtesting triggered by slider inputs
- JSON output of key performance metrics (Sharpe Ratio, Annual Return, Drawdown, etc.)
- Parameter tuning for:
  - Short Moving Average window
  - Long Moving Average window
  - Starting cash amount
- Automatic injection of parameters into Lean strategy files
- Live loading indicator while backtest is running
- Backend powered by Flask, frontend by vanilla HTML and JavaScript

## Tech Stack

- Python 3
- Flask for backend routing
- QuantConnect Lean CLI for strategy execution
- HTML and JavaScript for the frontend

## Acknowledgment

This project was initially scaffolded with guidance from interactive AI coding tools and documentation. All ongoing development, system design, and feature enhancements are independently authored.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/lean-backtest-webapp.git
   cd lean-backtest-webapp
   ```
2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install flask:
   ```
   pip install flask
   ```
4. Install Lean via pipx:
   ```
   pipx install lean
   lean init
   ```
5. setup Lean project:
   ```
   lean create-project strategies/MyProject --language python
   ```
6. Run the app:
   ```
   python3 app.py
   ```
Then check the output to find the link to input to your browser.

## Current folder structure
backTestWebApp/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css, script.js (optional)
├── strategies/
│   └── MyProject/
│       ├── main.py
│       ├── params.json
│       └── backtests/
├── .gitignore
└── README.md
## Contact
Feel free to contact me on LinkedIn!
