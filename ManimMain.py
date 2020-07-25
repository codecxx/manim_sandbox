import os

f = open('run_manim.bat','w' )
py_file_name = r'C:\FromLaptop\manim_sandbox\chenxiaoxiannb\Gaokao_Math.py'
classname = ''
pl = " -pl"
pm = " -pm"
str01 = 'python C:\FromLaptop\manim_sandbox\manim.py '+ py_file_name +' '+ classname + pm
f.write(str01)
f.close()
os.system('run_manim.bat')
