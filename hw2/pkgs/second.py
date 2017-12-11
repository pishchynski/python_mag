from action import Action


class SecondAction(Action):
    def __init__(self):
        super(SecondAction, self).__init__(priority=5,
                                           period=None,
                                           exact=8,
                                           critical=False)

    def do_action(self):
        print "SecondAction says 'Hello, World!'"
        raise Exception("SecondAction raised exception :(")
