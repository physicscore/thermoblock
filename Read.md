this program is for simulate the heat flux of solid stuff.
You can adjust specific heat conductivity capacity and density to material u made in the program. (or another physical character u need.)
the basic materials are iron and copper. the parameter information of the metarial is from wickipedia of google.
the main idea is to split the solid into blocks like lego and calculate the flux between the blocks.
calcuate mechanism is defined as a method in the 'RObject' class which is the solid object consist of the blocks.
the 'block' object is the unit object of the solid like a lego block, each block in the solid has it's own index.
so 'block' should has indices (a set of index in 3 dimension) and the solid stuff, 'RObject' has a set of indices.
u can make any object by equation of the obejct in 3D rectangular coordinate.
  (I'm making the circular and spherical coordinate system.)

the copper stick and iron stick sample object is also in the main module, so u can just try making it by command line in python : 
  from mainmodule import *
  a = ironstick();

the sample object is just like a experiment metarial which i used in the 'general physics experiment class' at my school.
I'm in the dept. of physics in University of Seoul.

program language : python
required module : numpy, vpython, tkinter
