#(gimp-procedural-db-dump filename)
#(gimp-procedural-db-dump "procdump.txt")

from .lisp_parser import parse
import json
import os

PATH = os.path.join(os.path.dirname(__file__), "procdump.txt")
with open(PATH) as f:
	procs = "("+ f.read() + ")"

tree = parse(procs)

class Context:

	def makefunc(self, reg):

		name = reg[1]
		desc = " ".join(reg[2])
		help = " ".join(reg[3])
		auth = reg[4]
		auth2 = reg[5]
		date = reg[6]
		typ = reg[7]

		args = reg[8]
		rets = reg[9]

		def inner(*liveargs, **optargs):
			#if len(liveargs) != len(args):
			#	print("WARNING: ", liveargs, args)
			modargs = []


			trueindex = 0
			for i, arg in enumerate(args):
				argn = arg[0]
				if argn == "run-mode":
					modargs.append(self.RUNMODE)

				elif argn == "image":
					modargs.append("image")

				elif argn == "drawable":
					modargs.append("drawable")
				else:
					livearg = liveargs[trueindex]
					modargs.append(str(livearg) if not isinstance(livearg, str) else '"%s"' % livearg)
					trueindex += 1

			text = "(" + name + " " + " ".join(modargs) + ")"

			if not optargs.get("test", False):
				self.l.append(text)

			return text

		inner.__doc__ = "\n".join([str(l) for l in reg[1:8]])
		inner.__doc__ += "\nArgs:\n" + json.dumps(args, sort_keys=True, indent=4)
		inner.__doc__ += "\nRets:\n" + json.dumps(rets, sort_keys=True, indent=4)

		#TODO inner.__str__ = inner.__doc__

		return inner

	def __init__(self, path, outpath=None, interactive=False):
		self.tail = []
		self.l = []
		self.path = path
		self.outpath = path if outpath is None else outpath

		self.RUNMODE = "0" if interactive else "1"#"RUN-INTERACTIVE" if interactive else "RUN_NONINTERACTIVE"

		for reg in tree:
			setattr(self, reg[1].replace("-", "_").replace("script_fu_", "").replace("plug_in_", "").replace("gimp_", ""), self.makefunc(reg))

	def __call__(self, x):
		if isinstance(x, list):
			self.l += x
		else:
			self.l.append(str(x))

	def __str__(self):
		header = """(let* (
    (image (car (gimp-file-load RUN-NONINTERACTIVE inname inname)))
    (drawable (car (gimp-image-get-active-layer image))))\n""".replace("inname", '"%s"' % self.path)

		footer = """\n(gimp-file-save RUN-NONINTERACTIVE image drawable outname outname)
(gimp-image-delete image))""".replace("outname", '"%s"' % self.outpath)
		if len(self.l) > 0:
			ownstuff = header + "\n".join(self.l) + footer
		else:
			ownstuff = ""
		return ownstuff + "\n".join([str(t) for t in self.tail if not t is self])

	def execute(self, showcmd=False, warning=False):
		cmd = """gimp -i -b '{batchscript}' -b '(gimp-quit 0)'""".format(batchscript=str(self))
		if not warning:
			cmd += " 2> /dev/null"

		if showcmd:
			print(cmd)

		os.system(cmd)
	
	def file_execute(self, path=".gimp-2.8/scripts/tempbatch.scm", exe=True):
		
		with open(os.path.join(os.path.expanduser("~"), path), "w+") as scm:
			scm.write("(define (tempbatch)\n" + str(self) + "\n)")
		
		if exe:
			os.system("gimp -i -b '(tempbatch)' -b '(gimp-quit 0)'")

	def __add__(self, other):
		#ideally, many images in one batch, chain Contexts
		self.tail.append(other)
		return self


if __name__ == "__main__":

	c = Context("5.jpg", "_5.jpg")
	#print(dir(c))
	c.rect_select(10, 20, 500, 700, 2, 10, 10)
	c.gauss(150, 150, 0)

	b = Context("4.jpg", "_4.jpg")
	b.rect_select(10, 20, 500, 700, 2, 10, 10)
	b.gauss(150, 150, 0)

	c += b
	c.execute()

	#c.rect_select("5.jpg", 1, 2, 3, 4, "REPLACE", 1, 1, test=True)
	#print(c)
