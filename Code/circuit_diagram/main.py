import schemdraw
from schemdraw.elements import Line, Battery, MeterA, MeterV, Lamp

ROOT_PATH = "./Code/circuit_diagram/"

with schemdraw.Drawing(file=f"{ROOT_PATH}parallel.svg", show=False) as d:
    Line().right(1)
    d.push()
    Line().up(0.75)
    Battery().right(2)
    Line().down(0.75)
    d.pop()
    Line().down(0.75)
    Battery().right(2)
    Line().up(0.75)
    Line().right(1)

    Line().up(2)
    d.push()
    MeterA().left(2)
    Lamp().left(2)

    d.pop()
    Line().up(2)
    MeterV().left(4)
    Line().to(d.elements[0].start)

with schemdraw.Drawing(file=f"{ROOT_PATH}series.svg", show=False) as d:
    Line().right(1)
    Battery().right(1)
    Battery().right(1)
    Line().right(1)

    Line().up(2)
    d.push()
    MeterA().left(2)
    Lamp().left(2)

    d.pop()
    Line().up(2)
    MeterV().left(4)
    Line().to(d.elements[0].start)
