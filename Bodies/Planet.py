class Planet():
    """
    This object represents a planet
    _________________________________________________
    Attributes:
    name, mass, aphelion, perihelion, semi_major_axis,
    eccentricity, orbital_period, synodic_peroid
    _________________________________________________
    """
    def __init__(self,
                 name=None,
                 mass=None,
                 aphelion = None,
                 perihelion = None,
                 semi_major_axis = None,
                 eccentricity = None,
                 orbital_period = None,
                 synodic_peroid = None
                ):
        
        self.name = name
        self.mass = mass
        self.aphelion = aphelion
        self.perihelion = perihelion
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        self.orbital_period = orbital_period
        self.synodic_peroid = synodic_peroid
        
