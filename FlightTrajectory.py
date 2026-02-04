import numpy as np



DRY_MASS = 1 #kg
FUEL_MASS = 9 #kg
BURN_TIME = 15 #sec
THRUST = 100 #N
AREA = 0.008 #m^2
DRAG_COEF = 0.3
#Launch angle 
T_STEP = 10 #sec
I_VELOCITY = 0 #m/s

def atmospheric_density(h):
    '''calculate the pressure of the atmosphere given the altitude
    all calculations from https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html'''
    #Troposphere
    if h < 11000:
        temp = 15.04 - 0.006649 * h
        press = 101.29 * ((temp + 273.1)/288.08)**5.256

    #Lower Stratosphere
    elif h < 25000:
        temp = -56.46
        press = 22.65 * np.exp(1.73 - 0.000157 * h)
    #Upper Stratosphere
    else:
        temp = -131.21 + 0.00299 * h
        press = 2.488 * ((temp + 273.1) / 216.6) ** -11.388

    dens = press/(0.2869*(temp + 273.1))
    return dens

def compute_forces(dens, v, secs):
    '''gets net force'''
    f_drag = DRAG_COEF * dens * v**2 / 2 * AREA
    f_grav = 9.81 * (FUEL_MASS + DRY_MASS)

    if secs < BURN_TIME:
        f_thrust = THRUST
    else:
        f_thrust = 0

    f_net = f_thrust - f_grav - f_drag

    return f_net

    
    
