import inspect
import pkgutil


class Collector:
    def __init__(self, packages):
        self.actions = []

        for importer, mod_name, ispkg in pkgutil.walk_packages(packages):
            loaded_module = importer.find_module(mod_name).load_module(mod_name)

            for obj_name, obj in inspect.getmembers(loaded_module):
                if inspect.isclass(obj) and not obj_name.startswith('Action'):
                    self.actions.append(obj())

        self.actions.sort(key=lambda x: x.priority, reverse=True)

    def execute(self, event_index):
        for action in self.actions:
            executed = False

            if action.always or (action.period == 1):
                try:
                    if not action.execute():
                        # print 'Action index = {}'.format(event_index)
                        executed = True
                except Exception as e:
                    # print ('Exception raised!')
                    if action.critical:
                        raise e

            if not executed and action.period and event_index and not (event_index % action.period):
                try:
                    if not action.execute():
                        # print 'Action index = {}'.format(event_index)
                        executed = True
                except Exception as e:
                    # print ('Exception raised!')
                    if action.critical:
                        raise e

            if not executed and action.exact == event_index:
                try:
                    if not action.execute():
                        # print 'Action index = {}'.format(event_index)
                        executed = True
                except Exception as e:
                    # print ('Exception raised!')
                    if action.critical:
                        raise e



