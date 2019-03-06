# PyGimpBatchGen

See fastbatch.py for a more complex usage example

```python
from gimpscm import Context

# All methods are attached to a `Context` object.
c = Context("infile.png", "outfile.png")

# To list all attached methods
print(dir(c))

# Add a method invocation to the Context
# Method prefixes (script_fu_, plug_in_, gimp_) are omitted.
# run-mode, image and layer arguments are supplied automatically by the Context
c.rect_select(10, 20, 500, 700, 2, 10, 10)

# Execute the Context, opens Gimp in batch mode
g.execute()

# To get more info about a method
help(c.rect_select)

```
