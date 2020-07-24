import os

for filename in os.listdir():
    for end in ['.aux', '.log', '.tex', '.svg', '.xdv']:
        if filename.endswith(end):
            os.remove(filename)
            # print(filename)
            break

os.chdir('Tex')
for filename in os.listdir():
    for end in ['.aux', '.log', '.tex', '.svg', '.xdv']:
        if filename.endswith(end):
            os.remove(filename)
            # print(filename)
            break
os.chdir('..')
if not os.listdir('Tex'):
    os.rmdir('Tex')