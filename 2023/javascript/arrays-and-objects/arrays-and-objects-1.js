function encontrarIndices(vetor, numero)
{
    let numeroEm = []

    for (let i = 0; i < vetor.length; i++)
    {
        if (vetor[i] === numero)
        {
            numeroEm.push(i)
        }
    }

    console.log(numeroEm)
}

const v = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
encontrarIndices(v, 2)