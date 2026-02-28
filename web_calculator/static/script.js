let currentOperand = '0';
let previousOperand = '';
let operation = undefined;

const currentOperandDisplay = document.getElementById('current-operand');
const previousOperandDisplay = document.getElementById('previous-operand');

function updateDisplay() {
    currentOperandDisplay.innerText = currentOperand;
    if (operation != null) {
        let opSymbol = '';
        switch(operation) {
            case 'add': opSymbol = '+'; break;
            case 'subtract': opSymbol = '-'; break;
            case 'multiply': opSymbol = '×'; break;
            case 'divide': opSymbol = '÷'; break;
            case 'power': opSymbol = '^'; break;
        }
        previousOperandDisplay.innerText = `${previousOperand} ${opSymbol}`;
    } else {
        previousOperandDisplay.innerText = '';
    }
}

function appendNumber(number) {
    if (number === '.' && currentOperand.includes('.')) return;
    if (currentOperand === '0' && number !== '.') {
        currentOperand = number.toString();
    } else {
        currentOperand = currentOperand.toString() + number.toString();
    }
    updateDisplay();
}

function clearDisplay() {
    currentOperand = '0';
    previousOperand = '';
    operation = undefined;
    updateDisplay();
}

function deleteNumber() {
    if (currentOperand === '0') return;
    currentOperand = currentOperand.toString().slice(0, -1);
    if (currentOperand === '') currentOperand = '0';
    updateDisplay();
}

function chooseOperation(op) {
    if (currentOperand === '') return;
    if (previousOperand !== '') {
        compute();
    }
    operation = op;
    previousOperand = currentOperand;
    currentOperand = '0';
    updateDisplay();
}

async function compute() {
    if (operation === undefined || previousOperand === '' || currentOperand === '') return;

    const response = await fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            operation: operation,
            num1: previousOperand,
            num2: currentOperand
        }),
    });

    const data = await response.json();
    if (data.result !== undefined) {
        currentOperand = data.result.toString();
        operation = undefined;
        previousOperand = '';
    } else {
        currentOperand = 'Error';
    }
    updateDisplay();
}

async function appendScientific(op) {
    if (currentOperand === '') return;

    const response = await fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            operation: op,
            num: currentOperand
        }),
    });

    const data = await response.json();
    if (data.result !== undefined) {
        currentOperand = data.result.toString();
    } else {
        currentOperand = 'Error';
    }
    updateDisplay();
}

updateDisplay();
