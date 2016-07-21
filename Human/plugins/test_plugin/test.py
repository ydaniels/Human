import plugins

if __name__ == '__main__':

    # create a plugin manager
    plugin_manager = plugins.PluginManager('./plugins')

    # load all plugin modules
    for plugin in plugin_manager.get_available_plugins():
        plugin_manager.load_plugin(plugin)

    # executes action_hello(hook_params) in ./plugins/*/__init__.py (if loaded)
    plugin_manager.execute_action_hook('hello', {'name': 'bob'})

    # executes filter_hello(hook_params) in ./plugins/*/__init__.py (if loaded)
    result = plugin_manager.execute_filter_hook('hello', {'name': 'bob'})
    print result

    # load all plugin modules
    for plugin in plugin_manager.get_loaded_plugins():
        plugin_manager.unload_plugin(plugin)
