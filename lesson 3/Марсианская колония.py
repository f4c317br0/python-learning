class Robot:
    def __init__(self, name, battery: int = 100):
        self.name = name
        self.battery = battery

    def status(self):
        return [self.name, self.battery, 'idle']

    def info(self):
        return f'Robot {self.name} ready for work'


class Miner(Robot):
    def __init__(self, name, battery: int = 100, resource: str = 'stone'):
        super().__init__(name, battery)
        self.resource = resource

    def mine(self):
        return f'{self.name} mined {self.resource}'

    def status(self):
        return [self.name, self.battery, 'mining', self.resource]


class Transporter(Robot):
    def __init__(self, name, battery: int = 100, cargo: int = 0):
        super().__init__(name, battery)
        self.cargo = cargo

    def transport(self):
        return f'{self.name} transported {self.cargo} kg'

    def status(self):
        return [self.name, self.battery, 'transporting', self.cargo]


class Builder(Robot):
    def __init__(self, name, battery: int = 100, material: str = 'brick'):
        super().__init__(name, battery)
        self.material = material

    def build(self):
        return f'{self.name} built a wall from {self.material}'

    def status(self):
        return [self.name, self.battery, 'building', self.material]


class MinerTransporter(Miner, Transporter):
    def __init__(self, name, battery: int = 100, resource: str = 'stone', cargo: int = 0):
        Robot.__init__(self, name, battery)  # явно, минуя MRO
        self.resource = resource
        self.cargo = cargo

    def work(self):
        return self.mine() + '\n' + self.transport()


class TransporterBuilder(Transporter, Builder):
    def __init__(self, name, battery: int = 100, cargo: int = 0, material: str = 'brick'):
        Robot.__init__(self, name, battery)
        self.cargo = cargo
        self.material = material

    def work(self):
        return self.transport() + '\n' + self.build()


class SuperRobot(Builder, MinerTransporter):
    def __init__(self, name, battery: int = 100, resource: str = 'stone',
                 cargo: int = 0, material: str = 'brick'):
        Robot.__init__(self, name, battery)
        self.resource = resource
        self.cargo = cargo
        self.material = material

    def work(self):
        return self.mine() + '\n' + self.transport() + '\n' + self.build()
