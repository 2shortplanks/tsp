from chouwa.decorators import jinjaglobal, jinjafilter

@jinjaglobal
def asset_path():
    return "/static/v1/"