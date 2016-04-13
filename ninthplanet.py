# A bit of code to investigate the supposed ninth planet
#
# Just out of curiosity!
#
#######################################################

import numpy as np
import math
# do I even need numpy for this?
# apparently yes I do
# Okay then.

#######################################################
# How bright would the postulated new plant look?
#Let's start with the worst-case scenario - dark and distant

# Since the planet would orbit in the Kuiper belt, this is presumably what it is
# That is, a KBO of unusual size
# So let's assume it has a similar composition and albedo to Pluto
# this can allow a guesstimate of the radius for Planet 9 From Outer Spaaaaace!
# define what quantities we know

grav_const = 6.672 * (10. ** -11.)
# Newton's constant of gravitation

pi = 3.141592654

r_orbit = 1200.
#orbital radius supposedly ranges between 200 and 2800 AU
# change value as needed

m_obj = 10.
# mass is supposedly 10 Earth masses

L_sun = 3.85 * (10. ** 26.)
# Solar luminosity in Watts

AU_m = 1.496 * (10. ** 11.)
# 1 AU in metres

m_earth = 5.972 * (10. ** 24.)
# mass of the Earth in kilograms

albedo_pluto = 0.4
# ranges from 0.49 to 0.66

pluto_density = 1880.0
# density in kilograms per cubic metre

# SI Units ###############################
# Get everything into sensible units #####

r_orb_m = r_orbit * AU_m
m_obj_kg = m_obj * m_earth

#########################################
# Flux = Luminosity / 4 * pi * radius_orbit^2

flux_at_9th_pl = L_sun / (4. * pi * r_orb_m * r_orb_m)
print flux_at_9th_pl

check_flux = L_sun / (4. * pi * AU_m * AU_m)
#print check_flux
# good - computation emits correct value for Earth

######################################
# Radius, g, escape velocity
# assume same average density as Pluto
# density = mass / volume => mass/density = volume

volume_obj = m_obj_kg / pluto_density

print volume_obj

#check_vol = m_obj_kg / volume_obj
#
#print check_vol - this is fine
# Now need to turn volume into a radius
# vol_sphere = 4/3 * pi * r^3, re-arrange as needed

r_obj = (volume_obj / ((4.0/3.0) * pi)) ** (1.0/3.0)

print r_obj, 'or in Earth=1:', (r_obj/6371000.)
# Three Earth radii - it would be big!

surface_grav = (grav_const * m_obj_kg) / (r_obj ** 2.)
print surface_grav, 'or in Earth = 1:', (surface_grav/9.80)
# Surprisingly, it would have close to a 1 G surface gravity

escape_vel = ((2. * grav_const * m_obj_kg) / r_obj) ** (0.5)
print escape_vel
# and a 20 km/s escape velocity? Impressive.
# that's heading toward the territory where you can hold onto H/He
# so how exactly is this thing NOT a gas giant's core?

#####################################
# Reflecting area
#
# How much sunlight can this object reflect?
# remember, reflecting area IS NOT 4 pi r^2.
# Rather, it's the circular cross-section of the object that faces the Sun
# because spherical objects will reflect some light away from the viewer
# and also the light itself is travelling radially out from the Sun
# Geometry - it's a pain.

refl_area = pi * r_obj * r_obj

reflected_light = albedo_pluto * refl_area * flux_at_9th_pl

dist_to_earth = (r_orbit - 1.0) * AU_m
# keep things simple - assume both planets are at opposition
# it makes up to 2 AU of distance, but with a 200-2800 AU orbit, that isn't
# so significant

flux_to_Earth = reflected_light / (4. * pi * dist_to_earth * dist_to_earth)
print flux_to_Earth

# Yeah, not a lot of flux.

mag_sun = -26.74

mag_planet = mag_sun + ((-2.5) * np.log10(flux_to_Earth/check_flux))
print mag_planet

# Worst-case magnitude - 28.6
# Best case - 17.2 mag
# Intermediate case - 25.9
# Would be detectable close to perihelion, basically hopeless when it's anywhere else
