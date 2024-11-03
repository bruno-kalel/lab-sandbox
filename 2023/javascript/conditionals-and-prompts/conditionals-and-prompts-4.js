let pos_inicial = parseInt(prompt('pos_inicial'))
let pos_final = parseInt(prompt('pos_final'))
let dis_passo = parseInt(prompt('dis_passo'))
let dis_total = pos_final-pos_inicial
let passos = 0

// tbm poderia ser let dis_total = parseInt(prompt('pos_final')) - parseInt(prompt('pos_inicial'))

while (dis_total > 0)
{
    dis_total -= dis_passo
    dis_passo++
    passos++
}

console.log('dê ' + passos + ' passos para chegar ao destino')