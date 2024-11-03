function calcular(valor, cupom)
{
    switch (cupom)
    {
        case 'menos10':
            return valor*10/100
        case 'menos20':
            return valor*20/100
        default:
            console.log('cupom inválido :(')
    }
}

console.log('desconto da compra:', calcular(200, 'menos20'))