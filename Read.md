Overview (what can i do with this?)

This program is for simulating the heat flux of a solid stuff or any stuff....
It can be used for any material if user update some information of new material and make a form by an equation.
User may calculate any flux if they modify the formula in the mainmodule containg the physical engine.

You can adjust specific heat conductivity capacity and density to material u made in the program. (or another physical character u need.)

Basic materials are iron and copper. User can use the information of those two material. And User can add another information needed for simulation by the UI, or just typing in the program.

The information of the metarial is from wickipedia of google.


Physical Idea of the Program.
The main idea is to split the solid into blocks like lego and calculate the flux between the blocks.

Calcuating mechanism is defined as a method in the 'RObject' class which is the solid object consisting of the blocks.

The 'block' object is the unit object of the solid like a lego block, each block in the solid has it's own index.

So 'block' should has indices (a set of index in 3 dimension) and the solid stuff, 'RObject' has a set of indices.
User can make any object by equation of the obejct in 3D rectangular coordinate.
  **(I'm making the circular and spherical coordinate system too.)

The copper stick and the iron stick sample object is also in the main module, so user can just try making it by command line with python :
  from mainmodule import *
  a = ironstick();

The sample object is just like a experiment metarial, which i used in the 'general physics experiment class' at my school.
I'm in the dept. of physics in University of Seoul.

Setting up the environment

program language : python
required module : numpy, vpython, tkinter

There is a 'setup.sh' shell script for setting up your environment of the computer to run the program. User just need to run the shell script by : ./setup.sh, and then user is ready to run the program. (If you can't run it, try : chmod 755 setup.sh) The shell script is for linux os since I'm developing the program with Ubuntu. I don't recommend this program for window user because is very annoying to use vpython with window. 윈도우 극혐...
But there are many easy way to run the linux os in the window so user would be better to run the program in that way.

Development progress situation

<List of functions I want to add to the program.>
- multi-process (most important, since the process is too slow now...)
- fantastic UI (making the program so easy to use that even my nine-years-old sister can try running it. not important at all)
- equation editor (if user had learnt the 'differential and integral calculus' and never gived up, it will be simple to set the equation of the form u want. Even if the form is very complex user can just split it into some easy forms and join them together. But in that way, some problem of the indices can be caused. So it would be better to find a way to convert the form to equation, by 3d camera or somthing.)

<UI>
- user can choose the environment either 'open' or 'close'.
- there are two example simulations 
      setting one end of the metal stick at 100℃ and one end of the metal stick, 0℃  and  other part is 20℃ .
- actually the UI is not working properly...
