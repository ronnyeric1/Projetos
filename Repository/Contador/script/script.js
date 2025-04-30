const contadorElement = document.getElementById('contador');
const incrementarBotao = document.getElementById('incrementar');
const decrementarBotao = document.getElementById('decrementar');

let contador = 0;

incrementarBotao.addEventListener('click', () => {
    contador++;
    contadorElement.textContent = contador;
});

decrementarBotao.addEventListener('click', () => {
    contador--;
    contadorElement.textContent = contador;
});