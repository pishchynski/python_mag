
class Action:
    def __init__(self,
                 priority=0,
                 period=None,
                 exact=None,
                 critical=False,
                 exec_limit=None):
        self.priority = priority
        self.period = period
        self.exact = exact
        self.critical = critical
        self.exec_limit = exec_limit

    def check_limit(self):
        return (not self.exec_limit) or self.exec_limit > 0

    def execute(self):
        self.do_action()
        if self.exec_limit:
            self.exec_limit -= 1

    def do_action(self):
        pass
