let lista_num = []

for (let i = 0; i < 3; i++)
{
    lista_num.push(parseInt(prompt('num ' + (i+1))))
}

console.log(lista_num.sort())