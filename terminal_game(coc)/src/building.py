class building:
  def __init__(self, pos_x, pos_y, health, health_init):
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.health = health
    self.health_init = health_init

class Hut(building):
  def __init__(self, pos_x, pos_y, health, health_init):
    super().__init__(pos_x, pos_y, health, health_init)


class TownHall(building):
  def __init__(self, pos_x, pos_y, health, health_init):
    super().__init__(pos_x, pos_y, health, health_init)


class Cannon(building):
  def __init__(self, pos_x, pos_y, health, health_init, damage, range):
    super().__init__(pos_x, pos_y, health, health_init)
    self.damage = damage
    self.range = range

class WizardTower(building):
  def __init__(self, pos_x, pos_y, health, health_init, damage, range):
    super().__init__(pos_x, pos_y, health, health_init)
    self.damage = damage
    self.range = range
    self.target = 0