class State:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Transition:
    def __init__(self, from_state, input_symbol, to_state):
        self.from_state = from_state
        self.input_symbol = input_symbol
        self.to_state = to_state 
