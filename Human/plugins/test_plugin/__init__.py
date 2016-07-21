__author__ = 'root'


def action_hello(hook_params):
    print 'hello %s' % hook_params['name']


def filter_hello(hook_params):
    return {'name': '%s johnson' % hook_params['name']}
