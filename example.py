#!/usr/bin/env python3

import sys
sys.dont_write_bytecode = True
from importmodule import importmodule

a = importmodule("a.py")
print(a.value)

b = importmodule("directory/b.py")
b.funct()

c = importmodule("directory/folder/c.py")
( c.Cls() ).method()
