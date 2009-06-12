from chouwa.decorators import jinjaglobal, jinjafilter

import markdown2

@jinjafilter
def markdown(value):
    return markdown2.markdown(value)
