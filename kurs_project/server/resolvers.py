from functools import reduce
from settings import INSTALLING_APPS

def get_sever_actions():
    applications = reduce(
        lambda  value, item: value+[__import__(f'{item}.routes')],
         INSTALLING_APPS,
         []
    )
    routes = reduce(
        lambda value, item: value + [getattr(item, 'routes', None)],
        applications,
        []
    )
    return reduce(
        lambda value, item: value + getattr(item, 'actionmapping', None),
        routes,
        []
    )
def resolver (action):
    actionmapping = {
        item.get('action'):item.get('controlers')
        for item in get_sever_actions()
        if item
    }
    return actionmapping.get(action)
