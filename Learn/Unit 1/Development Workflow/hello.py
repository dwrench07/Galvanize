"""
The ideal workflow is to write a little bit of code,
then ensure that the code is doing what you expect by inspecting some output,
or playing with it in an interactive environment.
Plus, having a tight feedback loop is more fun.
"""


# Step 1: Writing the script. Use the Terminal to open hello.py
def hello_world():
    print "hello, cruel world!"


def add_em_up(a, b, c):
    return a + b + c


def power_up(b, e):
    return b ** e


if __name__ == "__main__":
    hello_world()
    a = 22
    b = 33
    print add_em_up(3, 4, 5)
