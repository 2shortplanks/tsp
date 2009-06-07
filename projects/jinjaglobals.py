from chouwa.decorators import jinjaglobal, jinjafilter

@jinjafilter
def add_five(value):
    return value + 5

@jinjaglobal
def answer():
    return 42