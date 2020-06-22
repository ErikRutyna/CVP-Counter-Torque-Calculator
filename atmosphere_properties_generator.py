import math

def atmospheric_properties_generator(altitude):
    """State properties of 1976 US Standard Atmosphere model. 0 - 100km
    
    altitude  -- veritcal displacement in meters (m)
    atms_prop -- P (Pa), T (K), rho (kg/m^3), geopotenial height (m) 
    """

    #Constants used in calculation
    pres_sealevel = 101315      #Pa
    temp_sealevel = 288.15      #K
    radius_earth = 6.371e6      #m
    gas_const_air = 287.053     #J/kg-k

    #Calculate geopotential height - remove gravity from atmosphere
    geopotenial_height = radius_earth*altitude / (radius_earth+altitude) #m

    atms_prop = [0, 0, 0, altitude]

    #Check for right section of the atmosphere, apply appropriate rules of calculation
    if altitude >= 0 & altitude < 11e3 
        atms_prop[1] = temp_sealevel - 6.5*geopotenial_height #K
        atms_prop[0] = pres_sealevel * (temp_sealevel/atms_prop[1]) ^ (-34.1632/-6.5) #Pa
        atms_prop[2] = atms_prop[0] / (atms_prop[1]*gas_const_air) #kg/m^3

        return atms_prop
    elif altitude >= 11e3 & altitude < 20e3
 
        return atms_prop
    elif altitude >= 20e3 & altitude < 32e3

        return atms_prop
    elif altitude >= 32e3 & altitude < 47e3

        return atms_prop
    elif altitude >= 47e3 & altitude < 51e3

        return atms_prop
    elif altitude >= 51e3 & altitude < 71e3

        return atms_prop
    elif altitude >= 71e3 & altitude < 85e3

        return atms_prop
    