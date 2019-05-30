class Planet():
    """
    This object represents a planet
    _________________________________________________
    Attributes:
    name, mass, aphelion, perihelion, semi_major_axis
    _________________________________________________
    """
    def __init__(self,
                 name=None,
                 mass=None,
                 aphelion = None,
                 perihelion = None,
                 semi_major_axis = None):
        self.name = name
        self.mass = mass
        self.aphelion = aphelion
        self.perihelion = perihelion
        self.semi_major_axis = semi_major_axis
        
