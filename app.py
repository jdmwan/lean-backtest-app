import json
import subprocess
import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/run-backtest', methods=['POST'])
def run_backtest():
    data = request.json
    short = int(data.get("short_window", 10))
    long = int(data.get("long_window", 30))
    cash = int(data.get("starting_cash", 100000))

    # Step 1: Write params.json
    param_path = os.path.join("strategies", "MyProject", "params.json")
    with open(param_path, "w") as f:
        json.dump(data, f)

    # Step 2: Run lean backtest
    subprocess.run(["lean", "backtest", "strategies/MyProject"], stdout=subprocess.DEVNULL)

    # Step 3: Find most recent summary.json
    backtest_dir = os.path.join("strategies", "MyProject", "backtests")
    latest = sorted(os.listdir(backtest_dir))[-1]
    summary_path = os.path.join(backtest_dir, latest)

    # Look for the file that ends in -summary.json
    summary_file = next((f for f in os.listdir(summary_path) if "summary" in f), None)
    if not summary_file:
        return jsonify({"error": "No summary found"}), 500

    with open(os.path.join(summary_path, summary_file)) as f:
        summary_data = json.load(f)
    statistics = summary_data.get("totalPerformance", {}).get("tradeStatistics", {})

    general_statistics = {
        "Sharpe ratio": statistics.get("sharpeRatio", {})
    }
    return jsonify(general_statistics)

if __name__ == '__main__':
    app.run(debug=True)
