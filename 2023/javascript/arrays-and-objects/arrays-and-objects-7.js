const politicos = []

function P(nome, cargo) // Político
{
    this.nome = nome;
    this.cargo = cargo;
}

const p1 = new P('nome1', 'cargo1')
politicos.push(p1)

const p2 = new P('nome2', 'cargo2')
politicos.push(p2)

const p3 = new P('nome3', 'cargo3')
politicos.push(p3)

function C(c1, c2) // caráter
{
    this.c1 = c1;
    this.c2 = c2;
}

p1.carater = new C('p1c1', 'p1c2')
p1.carater = new C('p2c1', 'p2c2')
p1.carater = new C('p3c1', 'p3c2')

for (let i = 0; i < politicos.length; i++)
{
    console.log(politicos[i].nome)
    console.log(politicos[i].cargo)
    console.log(politicos[i].carater)
}