//Função somar//
function somar(){
    const num1 = Number(document.getElementById('num1').value)
    const num2 = Number(document.getElementById('num2').value)
   
    if (num1 != '' && num2 != ''){
         let soma = num1 + num2
        document.getElementById('result').innerHTML = 'Resultado: ' + soma
    }else{
        alert('Preencha os dois campos.')
    }
}

//Função subtrair
function subtrair(){
    const num1 = Number(document.getElementById('num1').value)
    const num2 = Number(document.getElementById('num2').value)
   
    if (num1 != '' && num2 != ''){
         let soma = num1 - num2
        document.getElementById('result').innerHTML = 'Resultado: ' + soma
    }else{
        alert('Preencha os dois campos.')
    }
}

//Função multiplicar//
function multiplicar(){
    const num1 = Number(document.getElementById('num1').value)
    const num2 = Number(document.getElementById('num2').value)
   
    if (num1 != '' && num2 != ''){
         let soma = num1 * num2
        document.getElementById('result').innerHTML = 'Resultado: ' + soma
    }else{
        alert('Preencha os dois campos.')
    }
}

//Função dividir//
function dividir(){
    const num1 = Number(document.getElementById('num1').value)
    const num2 = Number(document.getElementById('num2').value)
   
    if (num1 != '' && num2 != ''){
         let soma = num1 / num2
        document.getElementById('result').innerHTML = 'Resultado: ' + soma
    }else{
        alert('Preencha os dois campos.')
    }
}

//Função limpar//
function limpar(){
    document.getElementById('num1').value = ''
    document.getElementById('num2').value = ''
    document.getElementById('result').innerHTML = 'Resultado: '
}

//Função calcular//
function calcular(){
    const ap1 = Number(document.getElementById('ap1').value)
    const ap2 = Number(document.getElementById('ap2').value)
    const as = Number(document.getElementById('as').value)

    let nota = ap1 + ap2 + as

    document.getElementById('nota').innerHTML = 'Nota: ' + nota
    if(nota >= 6){
        alert('O aluno está aprovado')
    }
    else{
        alert('O aluno está reprovado')
    }
}
//Função para verificar ap1//
function verificaAp1(){
    const ap1 = Number(document.getElementById('ap1').value)
    if (ap1 < 0 || ap1 > 1.5){
        alert ('Nota inválida. Digite uma nota de 0 a 1.5.')
        document.getElementById('ap1').value = ''
        document.getElementById('ap1').focus()
    }
}

//Função para verificar ap2//
function verificaAp2(){
    const ap2 = Number(document.getElementById('ap2').value)
    if (ap2 < 0 || ap2 > 2.5){
        alert ('Nota inválida. Digite uma nota de 0 a 2.5.')
        document.getElementById('ap2').value = ''
        document.getElementById('ap2').focus()
    }
}

//Função para verificar As//
function verificaAs(){
    const as = Number(document.getElementById('as').value)
    if (as < 0 || as > 6){
        alert ('Nota inválida. Digite uma nota de 0 a 6.')
        document.getElementById('as').value = ''
        document.getElementById('as').focus()
    }
}