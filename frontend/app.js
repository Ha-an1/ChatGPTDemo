const display = document.querySelector('#display');
const status = document.querySelector('#status');
let firstValue = null;
let operation = null;

function setDisplay(value) {
  display.value = value;
}

async function calculate() {
  const secondValue = Number(display.value);

  if (firstValue === null || operation === null) return;

  status.textContent = 'Calculating...';

  try {
    const response = await fetch('/api/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ operation, a: firstValue, b: secondValue })
    });

    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Calculation failed');

    setDisplay(data.result);
    status.textContent = '';
    firstValue = null;
    operation = null;
  } catch (error) {
    status.textContent = error.message;
  }
}

document.querySelector('.keys').addEventListener('click', (event) => {
  const button = event.target.closest('button');
  if (!button) return;

  if (button.dataset.value !== undefined) {
    setDisplay(display.value === '0' ? button.dataset.value : display.value + button.dataset.value);
    return;
  }

  if (button.dataset.action === 'clear') {
    firstValue = null;
    operation = null;
    setDisplay('0');
    status.textContent = '';
    return;
  }

  if (button.dataset.op) {
    firstValue = Number(display.value);
    operation = button.dataset.op;
    setDisplay('0');
    return;
  }

  if (button.dataset.action === 'equals') calculate();
});
