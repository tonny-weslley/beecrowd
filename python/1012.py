a, b, c = map(float, input().split())
pi = 3.14159

triangulo = (a * c) / 2
circulo = pi * c ** 2
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

print(
    'TRIANGULO: {:.3f}\n'
    'CIRCULO: {:.3f}\n'
    'TRAPEZIO: {:.3f}\n'
    'QUADRADO: {:.3f}\n'
    'RETANGULO: {:.3f}'
    .format(triangulo, circulo, trapezio, quadrado, retangulo)
)
