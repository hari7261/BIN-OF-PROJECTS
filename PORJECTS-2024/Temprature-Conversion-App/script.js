function convertTemperature() {
    const temp = parseFloat(document.getElementById('tempInput').value);
    const unit = document.getElementById('unitInput').value;
    let celsius, fahrenheit, kelvin;

    if (unit === 'celsius') {
        celsius = temp;
        fahrenheit = (temp * 9/5) + 32;
        kelvin = temp + 273.15;
    } else if (unit === 'fahrenheit') {
        celsius = (temp - 32) * 5/9;
        fahrenheit = temp;
        kelvin = celsius + 273.15;
    } else if (unit === 'kelvin') {
        celsius = temp - 273.15;
        fahrenheit = (celsius * 9/5) + 32;
        kelvin = temp;
    }

    document.getElementById('results').innerHTML = `
        <p>Celsius: ${celsius.toFixed(2)}°C</p>
        <p>Fahrenheit: ${fahrenheit.toFixed(2)}°F</p>
        <p>Kelvin: ${kelvin.toFixed(2)}K</p>
    `;
}
