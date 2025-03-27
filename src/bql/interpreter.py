class BQLInterpreter:
    def __init__(self):
        self.registers = {}

    def execute(self, command):
        tokens = command.split()
        if not tokens:
            return
        
        action = tokens[0]

        if action == "CREATE":
            self.create_register(tokens[1], int(tokens[2]))
        elif action == "ENTANGLE":
            self.entangle(tokens[1], tokens[2])
        elif action == "APPLY_NOISE":
            self.apply_noise(tokens[1], float(tokens[2]))
        elif action == "DISTILL":
            self.distill(tokens[1])
        elif action == "SHOW":
            self.show(tokens[1])
        else:
            print("Unknown command")

    def create_register(self, name, levels):
        self.registers[name] = {"levels": levels, "state": [1] + [0] * (levels - 1)}
        print(f"Created bosonic register {name} with {levels} levels.")

    def entangle(self, reg1, reg2):
        if reg1 in self.registers and reg2 in self.registers:
            print(f"Entangled {reg1} and {reg2} using rotation-based encoding.")
        else:
            print("Register not found.")

    def apply_noise(self, reg, strength):
        if reg in self.registers:
            print(f"Applied noise with strength {strength} to {reg}.")
        else:
            print("Register not found.")

    def distill(self, reg):
        if reg in self.registers:
            print(f"Applied entanglement distillation on {reg}.")
        else:
            print("Register not found.")

    def show(self, reg):
        if reg in self.registers:
            print(f"State of {reg}: {self.registers[reg]}")
        else:
            print("Register not found.")

