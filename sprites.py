class Sprite:

  def __init__(self, imgLocation, visibilityStatus):
    self.imgLocation = imgLocation
    self.visibilityStatus = visibilityStatus 


class Background(Sprite):
  
  def __init__(self, imgLocation, visibilityStatus):
    super().__init__(imgLocation, visibilityStatus)
    self.layer = 0

    
class God(Sprite):
  
  def __init__(self, imgLocation, visibilityStatus, currentRoom):
    super().__init__(imgLocation, visibilityStatus)
    self.layer = 1
