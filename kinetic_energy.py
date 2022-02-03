# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def calculate_kinetic_energy(mass, distance, time):
    massVal = mass.value
    massUnit = mass.unit
    distanceUnit = distance.unit
    distanceValue = distance.value

    if distanceUnit != 'km':
        if distanceUnit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit
            in_km = distanceValue * 9.461e12
            distanceValue = in_km
            distanceUnit = 'km'
        else:
            print ("unit is Unknown")
            return
    speed = distanceValue/time # [km per sec]
    if massUnit != 'kg':
        if massUnit == "solar-mass":
            # convert from solar mass to kg
            value = massVal * 1.98892e30 # [kg]
            massVal = value
            massUnit = 'kg'
        else:
            print ("unit is Unknown")
            return

    return 0.5 * massVal * speed ** 2

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))
