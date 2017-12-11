
class Action(object):
    def __init__(self,
                 priority=0,
                 period=None,
                 always=False,
                 exact=None,
                 critical=False,
                 exec_limit=None):
        self.priority = priority
        self.period = period
        self.always = always
        self.exact = exact
        self.critical = critical
        self.exec_limit = exec_limit

    def check_limit(self):
        return (not self.exec_limit) or self.exec_limit > 0

    def execute(self, force=False):
        if force or self.check_limit():
            self.do_action()
            if self.exec_limit:
                self.exec_limit -= 1
            return 0

        return 1

    def do_action(self):
        pass
