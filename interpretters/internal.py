class Tasks():
  def __init__(self):
    pass

  def select_pen(self, pen_number: str):
    print('Selecting pen ' + pen_number)

  def item_down(self, item: str):
    print('Putting ' + item + ' down')

  def item_up(self, item: str):
    print('Putting ' + item + ' up')

  def draw(self, direction: str, length: str, unit: str):
    print('Drawing ' + length + unit + ' to ' + direction)

def internal_interpret():
  Tasks().select_pen('2')
  Tasks().item_down('pen')
  Tasks().draw('west', '2', 'cm')
  Tasks().draw('north', '1', 'cm')
  Tasks().draw('east', '2', 'cm')
  Tasks().draw('south', '1', 'cm')
  Tasks().item_up('pen')