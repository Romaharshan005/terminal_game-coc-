class Troops:
  def __init__(self, pos_x, pos_y, health, health_init, damage, spawn):
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.health = health
    self.health_init = health_init
    self.damage = damage
    self.spawn = spawn

class Barbarian(Troops):
  def __init__(self, pos_x, pos_y, health, health_init, damage, spawn):
    super().__init__(pos_x, pos_y, health, health_init, damage, spawn)
    self.target = 0

class Archers(Troops):
  def __init__(self, pos_x, pos_y, health, health_init, damage, spawn, range):
    super().__init__(pos_x, pos_y, health, health_init, damage, spawn)
    self.range = range
    self.target = 0

class Balloons(Troops):
  def __init__(self, pos_x, pos_y, health, health_init, damage, spawn):
    super().__init__(pos_x, pos_y, health, health_init, damage, spawn)
    self.target = 0