import os


def importmodule(moduleName):

	if not os.path.isfile(moduleName): 
		raise FileNotFoundError(moduleName)

	name = os.path.basename(moduleName)
	name = name.replace(".py","")

	path = os.path.dirname(moduleName)
	path = path.replace("/",".")

	if path == "":
		imported = __import__(name)
		return imported

	imported = __import__(path,fromlist = [name])
	return eval("imported." + name)
