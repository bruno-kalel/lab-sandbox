function conceder_aumento(valor)
{
    console.log('sal_original: ' + valor);

    let percentualAumento = 0;
    let valorAumento = 0;

    if (valor <= 1280)
    {
        percentualAumento = 20;
    }
    else if (valor <= 2540)
    {
        percentualAumento = 15;
    }
    else if (valor <= 4160)
    {
        percentualAumento = 10;
    }
    else
    {
        percentualAumento = 5;
    }

    valorAumento = (valor * percentualAumento) / 100;
    valor += valorAumento;

    console.log('per_aplicado: ' + percentualAumento);
    console.log('val_aumento: ' + valorAumento);
    console.log('sal_reajustado: ' + valor);
}

conceder_aumento(parseFloat(prompt('sal_original')));
