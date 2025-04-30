function calcular(n1, n2){
    n1 = parseFloat(document.getElementById("n1").value);
    n2 = parseFloat(document.getElementById("n2").value);

    // Verifica se os valores são números válidos
    if (isNaN(n1) || isNaN(n2)) {
        document.getElementById("resultado").innerHTML = "Por favor, insira números válidos!";
        return;
    }

    const selector = document.getElementById("selector").value;
    let calculo;

    switch(selector){
        case '+':
            calculo = n1 + n2;
            document.getElementById("resultado").innerHTML = `O resultado da soma de ${n1} + ${n2} é = ${calculo}`;
            break;

        case '-':
            calculo = n1 - n2;
            document.getElementById("resultado").innerHTML = `O resultado da subtração de ${n1} - ${n2} é = ${calculo}`;
            break;

        case '*':
        calculo = n1 * n2;
        document.getElementById("resultado").innerHTML = `O resultado da subtração de ${n1} * ${n2} é = ${calculo}`;
        break;

        case '/':
            if (n2 === 0) {
                document.getElementById("resultado").innerHTML = "Divisão por zero não é permitida!";
            } else {
                calculo = Math.round(n1 / n2);
                if (Number.isNaN(calculo)) {
                    document.getElementById("resultado").innerHTML = "Insira um divisor válido!";
                } else {
                    document.getElementById("resultado").innerHTML = `O resultado da divisão de ${n1} / ${n2} é = ${calculo}`;
                }
            }
            break;

        default:
            document.getElementById("resultado").innerHTML = "Operação inválida!";

            
    }
}