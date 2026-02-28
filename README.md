# Professional Scientific Calculator

A modern, professional scientific calculator built with a Python (Flask) backend and a sleek web frontend.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, division.
- **Scientific Operations**:
  - Trigonometry: `sin`, `cos`, `tan` (in degrees).
  - Logarithms: `log` (base 10), `ln` (natural log).
  - Powers & Roots: `sqrt`, `x^y`, `exp`.
  - Others: Factorials (`x!`).
- **Professional UI**:
  - Modern dark-themed design.
  - Responsive grid layout.
  - Interactive buttons with hover effects.
  - Previous operand display for better context.

## Project Structure

- `web_calculator/`
  - `app.py`: Flask backend serving the UI and calculation API.
  - `calculator_logic.py`: Core mathematical logic using Python's `math` module.
  - `templates/index.html`: The HTML structure of the calculator.
  - `static/`
    - `style.css`: Modern CSS styling.
    - `script.js`: Frontend logic and API communication.

## How to Run

1. **Install Dependencies**:
   ```bash
   pip install flask
   ```

2. **Run the Application**:
   ```bash
   python web_calculator/app.py
   ```

3. **Access the Calculator**:
   Open your browser and go to `http://127.0.0.1:5000`.

## Automated Testing

A Playwright-based verification script is included to ensure the calculator works as expected.

### Prerequisites for Testing
```bash
pip install playwright
playwright install chromium
```

### Running Tests
```bash
python verify_calculator.py
```
