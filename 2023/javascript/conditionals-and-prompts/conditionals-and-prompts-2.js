let qtd_provas = parseInt(prompt('qtd_notas'))
let notas = 0

for (let i = 0; i < qtd_provas; i++)
{
    notas += parseFloat(prompt('nota prova ' + (i+1)))
}

console.log('média: ', notas/qtd_provas)

if (notas/qtd_provas < 7)
{
    console.log('reprovado')
}
else
{
    console.log('aprovado')
}