from enum import Enum


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7


class StateMachine:
    state = State.A

    def loop(self):
        return self.update({
            State.A: [State.B, 0],
            State.B: [State.C, 2],
            State.C: [State.D, 3],
            State.E: [State.F, 6],
            State.F: [State.D, 9]
        })

    def race(self):
        return self.update({
            State.A: [State.C, 1],
            State.C: [State.E, 4],
            State.D: [State.E, 5],
            State.E: [State.B, 7],
            State.F: [State.G, 8]
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal


def main():
    return StateMachine()


o = main()
print(o.race(), o.loop(), o.race(), o.race(), o.loop(), o.race(), o.loop(), o.loop(), o.race(), o.loop(), o.race())