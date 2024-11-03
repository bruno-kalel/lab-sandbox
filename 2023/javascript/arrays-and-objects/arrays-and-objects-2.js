let linhas = parseInt(prompt('linhas'))
let colunas = parseInt(prompt('colunas'))

let matriz = []

for (let i = 0; i < linhas; i++)
{
    matriz[i] = []
    for (let j = 0; j < colunas; j++)
    {
        matriz[i][j] = 0
    }
}

console.log(matriz)