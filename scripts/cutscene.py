class Cutscene:
    def __init__(self, game, sequential_commands=[], independent_commands=[], function=None, args=[]):
        self.game = game
        self.sequential_commands = []
        self.independent_commands = []
        self.finished = False
        self.function = function
        self.args = args

        self.load_commands(sequential_commands, independent_commands)

    def load_commands(self, sequential_commands, independent_commands):
        for command in sequential_commands:
            object = Command(self.game, command['function'], command['args'], command['timer'])
            self.sequential_commands.append(object)

        for command in independent_commands:
            object = Command(self.game, command['function'], command['args'], command['timer'])
            self.independent_commands.append(object)

    def update(self):
        self.sequential_commands[0].update()
        if self.sequential_commands[0].finished:
            self.sequential_commands.pop(0)

        for command in self.independent_commands[:]:
            command.update()

            if command.finished:
                self.independent_commands.remove(command)

        if len(self.sequential_commands) == 0 and len(self.independent_commands) == 0:
            self.finished = True

            if self.function:
                print(self.function, self.args)
                self.function(*self.args)

class Command:
    def __init__(self, game, function, args, timer):
        self.game = game
        self.function = getattr(self.game, function)
        self.args = args
        self.timer = timer
        self.finished = False

    def update(self):
        self.function(*self.args)
        self.timer -= 1

        if self.timer <= 0:
            self.finished = True
