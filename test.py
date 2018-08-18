from subprocess import call
import sys

call(['git','checkout', '-b', sys.argv[1]])
call(['git','add','.'])
call(['git','commit', '-m', '"justcheck"'])
call(['git','push', 'origin', sys.argv[1]])
call(['git','checkout','master'])

