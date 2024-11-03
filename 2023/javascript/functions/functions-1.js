function calcular(pre_original, per_desconto, qua_adquirida)
{
    return (pre_original - ((pre_original * per_desconto)/100)) * qua_adquirida
}

console.log(calcular(50, 10, 2))