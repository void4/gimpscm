from gimpscm import Context
from glob import glob
import os

g = None

for path in glob("images/*.png"):

    c = Context(path, os.path.join(os.path.dirname(path), "fastbatch", os.path.basename(path)))
    #print(dir(c))
    c.rect_select(10, 20, 500, 700, 2, 10, 10)
    c.gauss(150, 150, 0)

    if g is None:
        g = c
    else:
        # Chain Contexts by adding them
        g += c

g.execute()
