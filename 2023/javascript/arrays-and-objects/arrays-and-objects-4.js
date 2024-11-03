estados = ['go', 'mg', 'sp', 'rj', 'am', 'pa']

// já considerando uma tag select com id "estado" criada no arquivo html

const estadoEscolhido = document.getElementById("estado")

estados.forEach((estado) =>
{
    const escolhaEstado = document.createElement("escolha")
    escolhaEstado.value = estado
    escolhaEstado.text = estado
    estadoEscolhido.appendChild(escolhaEstado)
})