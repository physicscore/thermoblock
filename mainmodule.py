from numpy import *
from visual import *
from pickle import *
from materials import * #include pickle
from equation import *
from visual.graph import *
			#default material is copper
			#contains materials array

print 'Materiallist', materiallist


class Temperature: # this class is for set some temperatures used through the all classes and functions

    def __init__(self):
        self.__Tmax__ = 100
        self.__Tmin__ = 0
        self.__Tofroom__ = 20.0
        self.__setTRange__()

    def setTmax(self,MaxTemperature):
        self.__Tmax__ = MaxTemperature
        # Tmax is defined at the main module and initialized as 100 celsius degrees
        self.__setTRange__()

    def setTmin(self,MinimumTemperature):
        self.__Tmin__ = MinimumTemperature
        # Tmin is defined at the main module and initialized as 0 celsius degrees
        self.__setTRange__()

    def __setTRange__(self):
        self.__TRange__ = self.__Tmax__ - self.__Tmin__

    def setTofroom(self,roomtemperature):
        self.__Tofroom__ = roomtemperature

    def getTmax(self):
        return self.__Tmax__

    def getTmin(self):
        return self.__Tmin__

    def getTRange(self):
        return self.__TRange__

    def getTofroom(self):
        return self.__Tofroom__

    def __repr__(self):
        information = "The maximum temperature is " + str(self.__Tmax__) + "C\n"
        information = information + "The minimum temperature is " + str(self.__Tmin__) + "C\n"
        information = information + "The Range of temperature is " + str(self.__TRange__) + "C\n"
        information = information + "The temperature of room is " + str(self.__Tofroom__) + "C\n"
        return information

##############################
temperature = Temperature()
##############################


#load the colorspectrum.pck file 
#anyone can chage the color information.
#this RGB information in array list is used to assign color for specific temperature.
f = open('colorspectrum.pck','r')
RGB = load(f)
f.close()



#This function is just for some situation that type of indices should be list.
#Since the ndarray.put or ndarray.itemset doesn't use list for indices.
def Indexis(nddata,indices,*value): 
    # return value of indices from array(or list or tuple) if there isn't any value.
    if len(value) == 0:
        pass
    # put value to data of indices if there is given value.
    elif len(value) == 1 :
        for i in value:
            nddata[indices[0]][indices[1]][indices[2]] = i
        pass
    else:
        print "Please enter only 1 value."
        pass
    return nddata[indices[0]][indices[1]][indices[2]]

def up(data,indices,m):
    indices = list(indices) # tuple doesn't support assignment.
    indices[m] = indices[m] + 1 # plus 1 at axis m.
    indices = tuple(indices) # list doesn't fit for variable of ndarray.item().
    try:
        if data.item(indices) is not None: # No problem!
            pass
        else: #None item was put in thermoblock[outofsystem]
            indices = 'outofsystem'
            pass
    except IndexError: #out of system.
        indices = 'outofsystem'
    return indices 

def down(data,indices,m):
    indices = list(indices) # tuple doesn't support assignment.
    if (indices[m]!=0): # we never need negative indices.
        indices[m] = indices[m] - 1 # minus 1 for axis m.
        indices = tuple(indices) # for item, put function indices should be tuple.
        try: # error hadling.
            if data.item(indices) is not None: # No problem!
                pass
            else: # out of indexset
                indices = 'outofsystem'
        except IndexError:
            indices = 'outofsystem'
    elif (indices[m]==0): #end of array(system).
        indices = 'outofsystem'
    else: pass
    return indices

###mono lego block class for build an object.###
#Thermo Block Class
#Each block has it's material[3], length[3],temperature T

class block:
    def setPosition(self,pos):
        self.pos = pos

    def getPosition(self):
        return self.pos

    def setVolume(self):
        self.volume = self.dx[0] * self.dx[1] * self.dx[2]

    def getVolume(self):
        return self.volume

    def setMaterial(self,material):
        self.material = material

    def getMaterial(self):
        return self.material

    def setArea(self):
        self.area = [1,1,1]
        for i in range(3):
            self.area[i]=self.volume/self.dx[i]

    def getArea(self,*m):
        area=[]
        if len(m) == 1:
            for i in m:
                return self.area[i]
        elif len(m) == 2:
            for i in m:
                area.append(area[i])
            return area
        else:
            return self.area

    def setdx(self,dx):
        self.dx = dx
        self.setVolume()
        self.setArea()

    def getdx(self,dx):
        return self.dx

    def setTemperature(self,T):
        self.T = T
        self.setColor()

    def getTemperature(self):
        return self.T

    def setColor(self):
        i = int((self.T-temperature.getTmin())*430/temperature.getTRange())
        if self.T>=temperature.getTmax():
            self.color = (1,1,1)
        elif self.T<=temperature.getTmin():
            self.color = (0,0,0)
        else:
            self.color = RGB[i]
        self.paintColor()

    def paintColor(self):
        self.block.color = self.color

    def getColor(self):
        return self.color

    def makeblock(self,pos,dx):
        self.block = box(pos=pos,length=dx[0],height=dx[1],width=dx[2])
#       w.axis = pos  #for spherical coordinate
    def setIndices(self,indices):
        self.indices = indices

    def getIndices(self):
        return self.indices

    def setPosition(self,objectpos):
        self.pos = []
        for m in range(3):
            self.pos.append(self.indices[m]*self.dx[m]+objectpos[m])

    def __init__(self,indices,dx,**keywords):
        self.setIndices(indices)
        self.setdx(dx)
        self.setMaterial(keywords.get('Material',copper))
        self.setPosition(keywords.get('objectpos',[0,0,0])) #automatically set from dx and indices
        self.makeblock(self.pos,self.dx) # visualize the block.
        self.setTemperature(keywords.get('Temperature',temperature.getTofroom())) # settemperature must be after makeblock()
        self.setColor() # automatically set from temperature.
        self.paintColor() # visualize the temperature of the block.

    def __repr__(self):
        self.block_info = "<Information of the block>" + '\n'
        self.block_info = self.block_info + 'Indices of block : ' + str(self.indices) + '\n'
        self.material_info = 'Material information : ' + '\n'
        for m in range(4):
            self.material_info = self.material_info + '    ' + str(constant[m]) + ' : ' + str(self.material[m]) + '\n'
        self.block_info = self.block_info + self.material_info
        self.block_info = self.block_info + 'Length[cm] : ' + str(self.dx[0]) + '\n'
        self.block_info = self.block_info + 'Width[cm] : ' + str(self.dx[1]) + '\n'
        self.block_info = self.block_info + 'Height[cm] : ' + str(self.dx[2]) + '\n'
        self.block_info = self.block_info + 'Temperature[`C] : ' + str(self.T) + '\n'
        self.block_info = self.block_info + 'Position : ' + str(self.pos) + '\n'
        return self.block_info


class Indexset:
    def __init__(self,*args,**keywords):
        if len(args)==0:
            self.setEquation(keywords.get('equation',eqStick))
            self.setVariables(keywords.get('variables',{'Length':10.0,'Width':1.0,'Height':0.3}))
            self.setMaxPos(keywords.get('MaxPos',[20.0,20.0,20.0])) # I'm makin a method for calculate the maximum position of the system.
            self.setPosition(keywords.get('position',[0,0,0]))
            self.setdx(keywords.get('dx',[0.5,1.0,0.3]))
            pass
        elif len(args)==5:
            #args = (equation,variables,MaxPos,position,dx)
            self.setEquation(args[0])
	    self.setVariables(args[1])
	    self.setMaxPos(args[2])
	    self.setPosition(args[3])
	    self.setdx(args[4])
            pass
        else:
            print "wrong arguments. put arguments like (equation,variables,MaxPos,position,dx) or like (equation = eqStick)"
        self.__setWholespace__()
        self.__setIndexset__()

    def setEquation(self,equation):
        self.equation = equation
    def getEquation(self):
        return self.equation

    def setVariables(self,variables):
        self.variables = variables
    def getVariables(self):
        return self.variables

    def setMaxPos(self,MaxPos):
        self.MaxPos = MaxPos
    def getMaxPos(self,MaxPos):
        return self.MaxPos

    def setPosition(self,position):
        self.pos = position
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
    def getPosition(self):
        return self.pos

    def setdx(self,dx):
        self.dx = dx
    def getdx(self):
        return self.dx


    def __setWholespace__(self): # the number of block for each axis.
        self.wholespace = []
        for m in range(3):
            self.wholespace.append(int(rint(self.MaxPos[m]/self.dx[m])))
    def getWholespace(self):
        return self.wholespace

    def __setIndexset__(self):
        self.indexset = []
        for i in range(self.wholespace[0]):
            for j in range(self.wholespace[1]):
                for k in range(self.wholespace[2]):
                    self.variables.update({'x':self.dx[0]*i,'y':self.dx[1]*j,'z':self.dx[2]*k})
                    if (self.equation(self.variables)== True):
                        self.indexset.append((i,j,k))
                        pass
        self.indexset = set(self.indexset)
    def setIndexset(self,indexset):
        self.indexset = indexset
    def getIndexset(self):
        return self.indexset

    def getMaxIndex(self):
        maxindex = []
        indexset = array(list(self.indexset)).swapaxes(0,1)
        for m in range(3):
            maxindex.append(max(indexset[m]))
        return maxindex
        
    def getMinIndex(self):
        minindex = []
        indexset = array(list(self.indexset)).swapaxes(0,1)
        for m in range(3):
            minindex.append(min(indexset[m]))
        return minindex

class RObject(Indexset):
    def __init__(self,**keywords):
        Indexset.__init__(self,keywords.get('equation',eqStick),keywords.get('variables',{'Length':10.0,'Width':1.0,'Height':0.3}),keywords.get('MaxPos',[20.0,20.0,20.0]),keywords.get('position',[0,0,0]),keywords.get('dx',[0.5,1.0,0.3]))
        self.setMaterial(keywords.get('material',copper))
        self.setState(keywords.get('state','isolated'))
        self.setIndexRange()
        self.setOpacity(keywords.get('opacity',1))
        self.setTemperature(keywords.get('temperature',temperature.getTofroom()))
        self.setCoefficient()
        self.pileblocks()

    def setMaterial(self,material):
        self.material = material
    def getMaterial(self):
        return self.material

    def setState(self,state):
        self.state = state
    def getState(self):
        return self.state

    def setIndexRange(self):
        self.indexrange = self.getMaxIndex()
    def getIndexRange(self):
        return self.indexrange

    def setOpacity(self,opacity):
        self.opacity = opacity
    def getOpacity(self):
        return self.opacity

    def setTemperature(self,temper):
        self.temperature = temper
    def getTemperature(self):
        return self.temperature
   
    def setBlockTemperature(self,indices,temper):
        self.getThermoblock().item(indices).setTemperature(temper)

    def setCoefficient(self):
        # coeffiecient is capacity * density / conductivity
        material = self.getMaterial()
        self.coefficient = material[2]*material[3]/material[1]
    def getCoefficient(self):
        return self.coefficient

    def pileblocks(self):
        indexsize = array(self.getIndexRange()) + array([1,1,1])

        indexset = self.getIndexset()
        self.thermoblock = []
        for i in range(indexsize[0]):
            for j in range(indexsize[1]):
                for k in range(indexsize[2]):
                    indices = (i,j,k)
                    if indices in indexset:
                        self.thermoblock.append(block(indices,self.getdx(),objectpos=self.getPosition(),Material=self.getMaterial()))
                        pass
                    elif indices not in indexset:
                        self.thermoblock.append(None)
                        pass
                    else: pass
        self.thermoblock = array(self.thermoblock).reshape(indexsize)
        for indices in self.getIndexset():
            self.thermoblock.item(indices).block.opacity = self.getOpacity()
 
    def getThermoblock(self):
        return self.thermoblock

class Simulation:
    def __init__(self,*Objects,**keywords):
        for m in range(len(Objects)):
            self.setObjectList(Objects[m])
        self.setMaximumIndex()
        self.prepareTemperatureArray()
        self.setdx()
        self.setdTMax(keywords.get('dTMax',1))
        self.setdt()
        self.setRunning(False)


########### start stop methods. #################
    def setRunning(self,running):
        self.running = running
    def getRunning(self):
        return self.running
#################################################

############## object list methods. ###############
    def setObjectList(self,Object,*objectname): 
        if len(objectname)==0: # if the user never put the name of the object
            try:
                if Object not in self.objectlist.values():
                    objectname = 'object_'+str(len(self.objectlist))
                    self.objectlist.update({objectname:Object})
                    pass
                else : pass
            except AttributeError: # if the object is the first one
                self.objectlist = {}
                objectname = 'object_0'
                self.setObjectList(Object,objectname)
                pass
            pass
        elif len(objectname)==1: # if the user put the name of the object
            try:
                if objectname[0] not in self.objectlist.keys():
                    self.objectlist.update({objectname[0]:Object})
                elif objectname[0] in self.objectlist.keys():
                    obname = objectname[0] + '_'
                    self.setObjectList(Object,obname)
            except AttributeError: # if the object is the first one
                self.objectlist = {objectname[0]:Object}
            pass
        else : print "Put one object at once"
        self.setWholeIndexset()

    def getObjectList(self):
        return self.objectlist

    def setObjectName(self,oldname,newname):
        newlist={newname:self.getObjectList().pop(oldname)}
        self.getObjectList().update(newlist)
    def getObjectName(self):
        return self.getObjectList().keys()
    def getAllObject(self):
        return self.getObjectList().values()

    def getObjectByName(self,name):
        return self.getObjectList().get(name)
#####################################################

########### indexset methods ########################

    def setWholeIndexset(self):
        self.wholeindexset = set([])
        for name in self.getObjectName():
            self.wholeindexset = self.wholeindexset.union(self.getObjectByName(name).getIndexset())

    def getWholeIndexset(self):
        return self.wholeindexset

    def setMaximumIndex(self):
        indexset = array(list(self.getWholeIndexset())).swapaxes(0,1)
        self.MaximumIndex = []
        for m in range(3):
            self.MaximumIndex.append(max(indexset[m]))
    def getMaximumIndex(self):
        return self.MaximumIndex

    def selectIndices(self,indices):
        self.getSelectedIndexset().add(indices)

    def setSelectedIndexset(self,indexset):
        self.selectedindexset = indexset
    def getSelectedIndexset(self):
        return self.selectedindexset

    def setSelectedIndexsetList(self,indexset,temper): #dictionary {temperature:indexset}
        if temper not in self.selectedindexlist.keys():
            self.selectedindexlist = self.selectedindexlist.update({temper:indexset})
        else:
            indexset = self.selectedindexlist.pop(temper) + indexset
            self.selectedindexlist.update({temper:indexset})
    def getSelectedIndexsetList(self):
        return self.selectedindexlist

#######################################################

##############temperature methods #####################

    def prepareTemperatureArray(self):
        self.Tn = []
        indexsize = array(self.getMaximumIndex()) + array([1,1,1])
        for i in range(indexsize[0]):
            for j in range(indexsize[1]):
                for k in range(indexsize[2]):
                    self.Tn.append(None)
        self.Tn = array(list(self.Tn)).reshape(indexsize)
        for name in self.getObjectName():
            Object = self.getObjectByName(name)
            temp = Object.getTemperature()
            for indices in Object.getIndexset():
                self.Tn.itemset(indices,temp)
        self.Tc = self.Tn
    def setTn(self,Tc):
        self.Tn = Tc
    def getTn(self):
        return self.Tn
    def setTc(self,Tc):
        self.Tc = Tc
    def getTc(self):
        return self.Tc

    def setdTMax(self,dTMax):
        self.dTMax = dTMax # the maximum change of the temperature during the simulation
    def getdTMax(self):
        return self.dTMax

    def setTemperature(self,indexset,temper):
        for indices in indexset:
            self.getTn().itemset(indices,temper)
        self.paint()

    def fixTemperature(self):
        for temper in self.getSelectedIndexsetList().keys():
            for indices in self.getSelectedIndexsetList.get(temper):
                self.getTn().itemset(indices,temper)

    def paint(self):
        # paint
        for name in self.getObjectName():
            thisobject = self.getObjectByName(name)
            for indices in thisobject.getIndexset():
                temper = self.getTn().item(indices)
                thisobject.setBlockTemperature(indices,temper)
	# done

#########################################


############ length methods ######################
    def setdx(self):
        self.dx = self.getAllObject()[0].getdx()
        for m in range(len(self.getAllObject())):
            Object = self.getAllObject()[m]
            if self.dx != Object.getdx():
                print "'dx' of all objects must be same..."
            else: pass
        self.setVolume()
        self.setArea()
    def getdx(self):
        return self.dx

    def setVolume(self):
        dx = self.getdx()
        self.volume = dx[0]*dx[1]*dx[2]
    def getVolume(self):
        return self.volume
    def setArea(self):
        self.area = []
        for m in range(3):
            self.area.append(self.getVolume()/self.getdx()[m])
    def getArea(self):
        return self.area

###################################################

            
############ time methods ##########################
    def setdt(self):
        coefficient = []
        for name in self.getObjectName():
            Object = self.getObjectByName(name)
            coefficient.append(Object.getCoefficient())
        mincoefficient = min(coefficient)
        mindL = min(self.getdx())/2
        volumeovermaxarea = min(self.getdx())
        self.dt = mincoefficient * volumeovermaxarea * mindL * self.getdTMax()/ temperature.getTRange()
    def getdt(self):
        return self.dt
#############################################

############ physics methods ####################
    def dQ(self,indices_0,indices_1,m,material):
        temp = self.getTn().item(indices_0)
        if type(indices_1)==tuple: # if neighbor block exists.
            dTperdL = (self.getTn().item(indices_1)-temp)/(self.dx[m]/2)
            pass
        elif indices_1 == 'outofsystem': # if neighbor block doesn't exists..
            dTperdL = 0
        else : print "can't calculate heat flux. something wrong with indexing"

        k = material[1]
        area = self.getArea()[m]

        return k*area*dTperdL*self.getdt()

    def dT(self,Q,material):
        capacity = material[2]
        density = material[3]
        deltaT = Q/(capacity*density*self.getVolume())
        return deltaT

    def UpdateTemperature(self):
        self.deltaT = []
        self.flux = []
        
        for indices in self.getWholeIndexset():
            indices = tuple(indices)
            deltaQ = [0,0,0]
            for Object in self.getAllObject():
                if indices in Object.getIndexset():
                    material = Object.getMaterial()
                else: pass
            for m in range(3):
                ind = up(self.getTn(),indices,m)
                deltaQ[m] = deltaQ[m] + self.dQ(indices,ind,m,material)
                ind = down(self.getTn(),indices,m)
                deltaQ[m] = deltaQ[m] + self.dQ(indices,ind,m,material)
                
            Q = (deltaQ[0]+deltaQ[1]+deltaQ[2])/6
            self.flux.append(Q)
            self.deltaT.append(self.dT(Q,material))
            result = self.getTn().item(indices) + self.dT(Q,material)
            self.getTc().itemset(indices,result)
        self.setTn(self.getTc()) # now the temperature is updated
        self.paint()
################################################

########## quick simulation ####################
    def demoSimulation(self,*T):
        if len(T)==2:
            Th = max(T)
            Tl = min(T)
        else:
            Th = 90
            Tl = 10
        time = 0
        endofsystem = set([])
        for indices in self.getWholeIndexset():
            if (indices[0]==0):
                endofsystem.add(indices)
            pass
        leftendofstick = tuple(self.getObjectList().get('object_0').getMinIndex())
        leftendofstick = set([leftendofstick])
        rightendofstick = tuple(self.getObjectList().get('object_0').getMaxIndex())
        rightendofstick = set([rightendofstick])
        self.setRunning(True)
        while True:
            if self.getRunning():
                self.setTemperature(leftendofstick,Th)
                self.setTemperature(rightendofstick,Tl)
                self.UpdateTemperature()
                time = time + self.getdt()
                print str(time) + ' seconds'
            else :
                rate(1)
##################################################




class Stick(RObject):
    def __init__(self,**keywords):
        self.length=keywords.get('Length',keywords.get('length',6.5))
        self.width=keywords.get('Width',keywords.get('width',1.0))
        self.height=keywords.get('Heigth',keywords.get('height',0.3))
        self.depth = keywords.get('depth',0)
        self.position=keywords.get('position',[self.depth,self.depth,self.depth])
        self.dx = keywords.get('dx',[0.5,1.0,0.3])
        self.material = keywords.get('material',copper)
        self.variables = {'Length':self.length,'Width':self.width,'Height':self.height,'position':self.position}
        RObject.__init__(self,dx=self.dx,material=self.material,equation = eqStick,variables = self.variables)
        

class WrappingStickAirBlock(RObject):
    def __init__(self,**keywords):
        self.innerobject = keywords.get('InnerObject')
        self.depth = self.innerobject.depth
        self.olength = keywords.get('outerlength',self.innerobject.length+self.depth*2)
        self.owidth = keywords.get('outerwidth',self.innerobject.width+self.depth*2)
        self.oheight = keywords.get('outerheight',self.innerobject.height+self.depth*2)
        self.dx = self.innerobject.dx
        self.material = air
        self.variables = {'Length':self.olength,'Width':self.owidth,'Height':self.oheight}
        RObject.__init__(self,dx=self.dx,material=self.material,equation = eqStick,variables = self.variables,opacity = 0.025)
        indexset = self.getIndexset() - self.innerobject.getIndexset()
        self.setIndexset(indexset)
        self.pileblocks()


