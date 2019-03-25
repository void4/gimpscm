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
c.execute()

# If the command is too long, it may be necessary to store it in a script file and call that
# The first argument is the gimp scripts folder relative from the home directory
# The second argument specifies if it should be executed after it was written
c.file_execute(path=".gimp-2.8/scripts/tempbatch.scm", exe=True)

# To get more info about a method
help(c.rect_select)

```
