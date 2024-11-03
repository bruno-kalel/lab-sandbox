function gerar(v) // valor
{
    const s = [0, 1]; // sequência

    for (let i = 2; i < v; i++)
    {
        const p = s[i - 1] + s[i -2] // próximo
        s.push(p)
    }

    return s
}

const n = gerar(50) // números
console.log(n)
