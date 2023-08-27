//Botão de adicionar a tarefa//
function adicionar() {
    const tarefa = document.getElementById("tarefa").value
    const li = document.createElement("li")
    li.textContent = tarefa
    //Tarefas pendentes
    const pendentes = document.getElementById("pendentes")
    pendentes.appendChild(li)

    //Botão de concluir a tarefa//
    const concluir = document.createElement('button');
    concluir.textContent = 'Concluir';
    concluir.type = 'button';
    concluir.style.marginLeft = "20px";
    concluir.addEventListener('click', function () {
        const tarefa = this.parentNode;     
        const concluidas = document.getElementById("concluidas");
        concluidas.appendChild(tarefa);
    });
    li.appendChild(concluir);

    //Botão para remover tarefas//
    const remover = document.createElement("button")
    remover.textContent = "Remover"
    remover.type = "button"
    remover.style.marginLeft = "20px"
    remover.addEventListener("click", function () { li.remove() })
    li.appendChild(remover)

    document.getElementById("tarefa").value = ''
    document.getElementById("tarefa").focus()
}

//Botão para mudar a cor de fundo//
function mudacor(){
    const body = document.querySelector("body")
    body.classList.toggle("fundo")
}