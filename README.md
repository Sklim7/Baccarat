# 🃏 Baccarat Simulator in Python

This project is a full-featured simulation of the Baccarat card game using Python. It models hand drawing, total calculations, third-card rules, and result tracking across thousands of rounds. 

---

## 📂 Project Features

- 🎴 **Card Drawing Logic** — Simulates real Baccarat card values (Ace = 1, Face cards = 0).
- ♠️ **Player & Banker Rules** — Applies third-card rules per official Baccarat guidelines.
- 📊 **Result Logging** — Stores each round's hands, totals, and winner in a CSV.
- 💾 **CSV Output** — Easily export and analyze results in Excel, Python, or data tools.

---

## 🧠 Game Logic Overview

- **Card Values:**
  - Ace = 1
  - 2–9 = Face value
  - 10, J, Q, K = 0

- **Hand Total Calculation:**
  - Total = (Sum of card values) % 10

- **Third Card Rules:**
  - Player draws a third card if total < 6.
  - Banker’s draw depends on Player's third card and Banker's total per Baccarat rules.

---

## 📁 Output Files

| File Name              | Description                                |
|------------------------|--------------------------------------------|
| `baccarat_results.csv` | All rounds with hands, totals, and results |

---

## 🧪 How to Run the Simulation

```bash
python baccarat_simulator.py
