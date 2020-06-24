import math

def atms_prop_calc(altitude):
    """State properties of 1976 US Standard Atmosphere model. 0 - 110km
    
    altitude  -- veritcal displacement in meters (m)  
    atms_prop -- P (Pa), T (K), rho (kg/m^3), geopotenial height (m) 
    """

    #Constants used in calculation
    pres_sealevel = 101315      #Pa
    temp_sealevel = 288.15      #K
    radius_earth = 6.371e6      #m
    gas_const_air = 287.053     #J/kg-k

    #Calculate geopotential height - remove gravity from atmosphere
    geopotenial_height = radius_earth*altitude / (radius_earth+altitude) / 1e3 #km

    #The general list shape
    atms_prop = [0, 0, 0, geopotenial_height * 1e3]

    #List containing ranges (km), 0 = sea level, 86 = von Karman, 110 for Stratos IV
    altitude_range = [0, 11, 20, 32, 47, 51, 71, 83, 91, 100, 110]

    #Check for right section of the atmosphere, apply appropriate rules of calculation
    if geopotenial_height >= altitude_range[0] and geopotenial_height < altitude_range[1]:
        atms_prop[1] = temp_sealevel - 6.5*geopotenial_height #K
        atms_prop[0] = pres_sealevel * (288.15 / (288.15 - 6.5*geopotenial_height)) ** (34.1632/-6.5) #Pa
        atms_prop[2] = atms_prop[0] / (atms_prop[1]*gas_const_air) #kg/m^3
        return atms_prop

    elif geopotenial_height >= altitude_range[1] and geopotenial_height < altitude_range[2]:
        atms_prop[1] =  216.65  #K
        atms_prop[0] =  22632.06 * math.exp(-34.1632 * (geopotenial_height - 11) / 216.65)#Pa
        atms_prop[2] =  atms_prop[0] / (atms_prop[1]*gas_const_air) #kg/m^3
        return atms_prop

    elif geopotenial_height >= altitude_range[2] and geopotenial_height < altitude_range[3]:
        atms_prop[1] =  196.65 + geopotenial_height #K
        atms_prop[0] =  5474.889 * (216.65 / (216.65 + (geopotenial_height - 20))) ** (34.1632) #Pa
        atms_prop[2] =  atms_prop[0] / (atms_prop[1]*gas_const_air) #kg/m^3
        return atms_prop

    elif geopotenial_height >= altitude_range[3] and geopotenial_height < altitude_range[4]:
        atms_prop[1] =  139.05 + 2.8*geopotenial_height #K
        atms_prop[0] =  868.0187  * (228.65 / (228.65 + 2.8 * (geopotenial_height - 32))) ** (34.1632/2.8) #Pa
        atms_prop[2] =  atms_prop[0] / (atms_prop[1]*gas_const_air) #kg/m^3
        return atms_prop

    elif geopotenial_height >= altitude_range[4] and geopotenial_height < altitude_range[5]:
        atms_prop[1] =  270.65 #K
        atms_prop[0] =  110.9063 * math.exp(-34.1632 * (geopotenial_height - 47) / 270.65) #Pa
        atms_prop[2] =  atms_prop[0] / (atms_prop[1]*gas_const_air) #kg/m^3
        return atms_prop

    elif geopotenial_height >= altitude_range[5] and geopotenial_height < altitude_range[6]:
        atms_prop[1] =  413.5 - 2.8 * geopotenial_height #K
        atms_prop[0] =  66.93887 * (270.65 / (270.65 - 2.8 * (geopotenial_height - 51))) ** (34.1632 / -2.8) #Pa
        atms_prop[2] =  atms_prop[0] / (atms_prop[1]*gas_const_air) #kg/m^3
        return atms_prop

    elif geopotenial_height >= altitude_range[6] and geopotenial_height < altitude_range[7]:
        atms_prop[1] =  356.65 - 2 * geopotenial_height #K
        atms_prop[0] =  3.956420 * (216.65 / (214.65 - 2 * (geopotenial_height - 71))) ** (34.1632 / -2) #Pa
        atms_prop[2] =  atms_prop[0] / (atms_prop[1]*gas_const_air) #kg/m^3
        return atms_prop
    
    elif geopotenial_height >= altitude_range[7] and geopotenial_height < altitude_range[8]:
        atms_prop[1] =  186.8673 #K
        atms_prop[0] =  math.exp(2.159582e-6*(geopotenial_height)**3 + -4.836957e-4*(geopotenial_height)**2 + -0.1425192*(geopotenial_height) + 13.47530) #Pa
        atms_prop[2] =  math.exp(-3.322622e-6*(geopotenial_height)**3 + 9.11146e-4*(geopotenial_height)**2 + -0.2609971*(geopotenial_height) + 5.944694) #kg/m^3
        return atms_prop

    elif geopotenial_height >= altitude_range[8] and geopotenial_height < altitude_range[9]:
        atms_prop[1] =  263.1905 - 76.3232 * math.sqrt(1 - ((geopotenial_height - 91)/(-19.9429)) ** 2) #K
        atms_prop[0] =  math.exp(3.304895e-5*(geopotenial_height)**3 + -0.00906273*(geopotenial_height)**2 + 0.6516698*(geopotenial_height) + -11.03037) #Pa
        atms_prop[2] =  math.exp(2.873405e-5*(geopotenial_height)**3 + -0.008492037*(geopotenial_height)**2 + 0.6541179*(geopotenial_height) -23.6201) #kg/m^3        
        return atms_prop

    elif geopotenial_height >= altitude_range[9] and geopotenial_height < altitude_range[10]:
        atms_prop[1] =  263.1905 - 76.3232 * math.sqrt(1 - ((geopotenial_height - 91)/(-19.9429)) ** 2) #K
        atms_prop[0] =  math.exp(6.693926e-5*(geopotenial_height)**3 + -0.01945388*(geopotenial_height)**2 + 1.719080*(geopotenial_height) + -47.7503) #Pa
        atms_prop[2] =  math.exp(-1.240774e-5**(geopotenial_height)**4 +0.00162063*(geopotenial_height)**3 +-0.8048342*(geopotenial_height)**2 + 55.55996*(geopotenial_height) + -1443.338) #kg/m^3        
        return atms_prop