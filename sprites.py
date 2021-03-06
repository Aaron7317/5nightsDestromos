from pygame import image

class Sprite:

  def __init__(self, imgLocation, visibilityStatus, layer):
    self.imgLocation = imgLocation
    self.visibilityStatus = visibilityStatus 
    self.layer = layer


class Room(Sprite):
  
  def __init__(self, imgLocation, visibilityStatus, layer, connections, active, foreground):
    super().__init__(imgLocation, visibilityStatus, layer)

    
class God(Sprite):
  
  def __init__(self, imgLocation, visibilityStatus, layer, currentRoom):
    super().__init__(imgLocation, visibilityStatus, layer)


# make a method that orders all objects based on their drawing layer