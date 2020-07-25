from manimlib.imports import *

class MyExam(Scene):
    def construct(self):
        basel = TextMobject(
            '''\\begin{flushleft}1. 已知集合 $A=\\{1,2,3,4,5\\}, B=\\{(x, y) \\mid x \\in A, y \\in A, x-y \\in A\\},$ 则 $B$
             中所含元素的个数为\\end{flushleft}''',
            r"\begin{tasks}(2)\task $3$\task $6$\task $8$\task $10$\end{tasks}"
        ).set_width(10).to_edge(UL)
        self.play(
            Write(basel),
        )
        self.wait()