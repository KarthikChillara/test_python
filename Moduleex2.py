from Moduleex import someperson
import platform
import sys,os,glob
sys.path.append(os.getcwd())
# import Moduleex
# Moduleex.funct1("Karthik") #Modulename.functionname
# FirstName = Moduleex.someperson["FirstName"]
# print(FirstName)

# import Moduleex as mx
#
# mx.funct1("Karthik")
# FirstName = mx.someperson["FirstName"]
# print(FirstName)
#import Moduleex


# Moduleex.funct1(5)
print(someperson["FirstName"])

name = platform.system()
print(name)
