class Tasks():
  def __init__(self):
    pass

  def selectPen(self, penNumber: str):
    print('Selecting pen ' + penNumber)

  def itemDown(self, item: str):
    print('Putting ' + item + ' down')

  def itemUp(self, item: str):
    print('Putting ' + item + ' up')

  def draw(self, direction: str, length: str, unit: str):
    print('Drawing ' + length + unit + ' to ' + direction)

def internalInterpret():
  Tasks().selectPen('2')
  Tasks().itemDown('pen')
  Tasks().draw('west', '2', 'cm')
  Tasks().draw('north', '1', 'cm')
  Tasks().draw('east', '2', 'cm')
  Tasks().draw('south', '1', 'cm')
  Tasks().itemUp('pen')