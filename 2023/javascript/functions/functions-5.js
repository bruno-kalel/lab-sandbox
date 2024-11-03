function calcular(xa, ya, xb, yb) {
    return Math.sqrt(Math.pow(xb - xa, 2) + Math.pow(yb - ya, 2));
}

console.log(calcular(1, 1, 5, 4));