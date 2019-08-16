from functools import reduce
from settings import INSTALLING_APPS

def get_sever_actions():
    applications = reduce(
        lambda  value, item: value+[__import__(f'{item}.routes')],
         INSTALLING_APPS,
         []
    )
    routes = reduce(
        lambda value, items: value + [getattr(item, 'routes', None)],
        applications,
        []
    )
    return reduce(
        lambda value, items: value + getattr(item, 'actionmapping', None),
        rotes,
        []
    )
