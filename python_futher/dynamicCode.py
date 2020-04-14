for i in range(5):
   exec('var{} = {}'.format(i, i))
   exec('print(var{},end=\' \')'.format(i))

print()

for i in range(5):
   exec('%s%d = %d' %('var',i, i))
   exec('print(%s%d,end=\' \')' %('var',i))