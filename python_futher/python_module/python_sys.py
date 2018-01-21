# Python package 'sys'
import sys

print(sys.winver)
print(sys.version)
print(sys.path)
print(sys.maxsize)
print(sys.modules)
print(sys.hash_info)
print(sys.float_info)
print(sys.int_info)
print(sys.byteorder)
print(sys.thread_info)
print(sys.copyright)
print(sys.platform)

# stream
sys.stdout.write('standard output stream...\n')
sys.stdout.flush()
print("Input(ctrl+d exit input):")
ss = sys.stdin.read()
print('U input:',ss)

# use the built-in dir function to list the identifiers that a module defines.
print(dir(sys))
