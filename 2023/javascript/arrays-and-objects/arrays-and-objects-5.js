let matriz = []

for (let i = 0; i < 5; i++)
{
    matriz[i] = []
    for (let j = 0; j < 2; j++)
    {
        let user_input
        if (j % 2 === 0)
        {
            user_input = prompt('dia da semana')
        }
        else
        {
            user_input = prompt('compromisso')
        }
        matriz[i][j] = user_input
    }
}

console.log(matriz)