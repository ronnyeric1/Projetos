const redSlider = document.getElementById('red');
const greenSlider = document.getElementById('green');
const blueSlider = document.getElementById('blue');
const redValueSpan = document.getElementById('redValue');
const greenValueSpan = document.getElementById('greenValue');
const blueValueSpan = document.getElementById('blueValue');
const colorPreview = document.querySelector('.color-preview');
const rgbCodeSpan = document.getElementById('rgbCode');

function updateColor() {
    const red = redSlider.value;
    const green = greenSlider.value;
    const blue = blueSlider.value;

    const rgbColor = `rgb(${red}, ${green}, ${blue})`;
    colorPreview.style.backgroundColor = rgbColor;
    rgbCodeSpan.textContent = rgbColor;
    redValueSpan.textContent = red;
    greenValueSpan.textContent = green;
    blueValueSpan.textContent = blue;
}

redSlider.addEventListener('input', updateColor);
greenSlider.addEventListener('input', updateColor);
blueSlider.addEventListener('input', updateColor);

// Inicializar a cor ao carregar a página
updateColor();