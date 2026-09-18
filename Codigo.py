
    down()
    goto(end.x, end.y)


def square(start, end):
    """Dibuja un cuadrado."""
    up()
    goto(start.x, start.y)
    setheading(0)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Primer clic: centro. Segundo clic: define el radio."""
    radius = abs(end - start)

    up()
    goto(start.x, start.y - radius)
    setheading(0)
    down()
    begin_fill()
    turtle.circle(radius)
    end_fill()


def rectangle(start, end):
    """Pendiente: dibujar un rectángulo."""
    pass


def triangle(start, end):
    """Pendiente: dibujar un triángulo."""
    pass


def tap(x, y):
    """Guarda el primer punto o dibuja la figura."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Guarda un valor en el estado."""
    state[key] = value


state = {'start': None, 'shape': line}

setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

# Deshacer el último paso de turtle.
onkey(undo, 'u')

# Colores: usa Mayús + la letra.
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')

# Figuras: usa letras minúsculas.
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()
