#PyGimpBatchGen

All methods are attached to a `Context` object.

Method prefixes (script_fu_, plug_in_, gimp_) are omitted.

run-mode, image and layer arguments are supplied automatically by the Context

Chain Contexts by adding them


See fastbatch.py for a usage example
```python
from gimpscm import Context

c = Context("infile.png", "outfile.png")

# To list all attached methods
print(dir(c))

# To get more info about a method
help(c.rect_select)

```
