from Tkinter import *
import tkMessageBox
from mainmodule import * 

root = Tk()
root.title("Thermolego")

class DemoSimulation(Frame):
    def __init__(self,*master):
        Frame.__init__(self,master[0])
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.menubar = Menu(self.master)

        self.simulationmenu = Menu(self.menubar,tearoff=0,title="MetalSticks")
        	

	self.simulationmenu.add_command(label="IronStick",command=self.demosimulation_ironstick)
        self.simulationmenu.add_command(label="CopperStick",command=self.demosimulation_copperstick)

        self.menubar.add_cascade(label="MetalSticks",menu=self.simulationmenu)

        self.master.config(menu=self.menubar)

    def demosimulation_ironstick(self):
        a = Stick(material = iron)
        b = Simulation(a)
        b.demoSimulation()
    def demosimulation_copperstick(self):
        a = Stick(material = copper)
        b = Simulation(a)
        b.demoSimulation()

class MainApplication(Frame):
    def __init__(self, master=root):
        Frame.__init__(self, master)   
        self.pack()                       
        self.createMenus()
        self.MaterialList()
        self.StateList()
        self.r1.select()
        self.createWidgets()
        self.fillparameters()

    def simulate(self):
        Th = float(self.Th.get())
        Tl = float(self.Tl.get())
        self.simulation.demoSimulation(Th,Tl)
        
    def makeObject(self):
        dx = [float(self.dx[0].get()) , float(self.dx[1].get()) , float(self.dx[2].get())]
        #MaxPos = [float(self.MaxPos[0].get()) , float(self.MaxPos[1].get()) , float(self.MaxPos[2].get())]
 #       equation = self.equation.get()
        material = materiallist[self.material_list.curselection()[0]]
        state = self.state.get()
        length = float(self.Length.get())
        width = float(self.Width.get())
        height = float(self.Height.get())
        print state
        try: 
            depth = int(self.depth.get())
        except AttributeError:
            depth = 0
            pass

        if state == 'open':
            self.stick = Stick(dx=dx,material=material,depth=depth,length = length,width = width, height = height)
            self.airblock = WrappingStickAirBlock(InnerObject = self.stick)
            self.simulation = Simulation(self.stick,self.airblock)
        else:
            self.stick = Stick(dx=dx,material=material,length = length,width = width, height = height)
            self.simulation = Simulation(self.stick)
        self.simulate()        


    def ShowInfo(self):
        title = "Information of " + self.Name.get()
        labelframe = LabelFrame(self.master,text = title)
        labelframe.pack()

        information = StringVar()
        label = Message(labelframe,textvariable = information)
        s = "Material : " + self.simulation.material[0] + "\n"
        s = s + "Conductivity : " + str(self.simulation.material[1]) + "\n"
        s = s + "Capacity : " + str(self.simulation.material[2]) + "\n"
        s = s + "Length : " + str(self.simulation.L) + "\n"
        information.set(s)
        label.pack()

    def fillparameters(self):
        labelframe = LabelFrame(self.master,text="Let's Fill the parameters")
        labelframe.pack()

#        l0 = Label(labelframe,text = "Name")
#        l0.pack()
#        self.Name = Entry(labelframe)
#        self.Name.pack()

        self.dx = []
        l1 = Label(labelframe,text = "dx")
        l1.pack()
        self.dx.append(Entry(labelframe,width = 5))
        self.dx[0].pack()
        self.dx[0].insert(0,'0.5')
        self.dx.append(Entry(labelframe,width = 5))
        self.dx[1].pack()
        self.dx[1].insert(0,'1.0')
        self.dx.append(Entry(labelframe,width = 5))
        self.dx[2].pack()
        self.dx[2].insert(0,'0.3')

        l2 = Label(labelframe,text = 'Length')
        l2.pack()
        self.Length = (Entry(labelframe,width=5))
        self.Length.pack()
        self.Length.insert(0,'10')

        l2 = Label(labelframe,text = 'Width')
        l2.pack()
        self.Width = (Entry(labelframe,width=5))
        self.Width.pack()
        self.Width.insert(0,'1')

        l2 = Label(labelframe,text = 'Height')
        l2.pack()
        self.Height = (Entry(labelframe,width=5))
        self.Height.pack()
        self.Height.insert(0,'0.3')
#        self.MaxPos = []
#        l2 = Label(labelframe,text = "MaxPos")
#        l2.pack()
#        self.MaxPos.append(Entry(labelframe,width = 5))
#        self.MaxPos[0].pack()
#        self.MaxPos.append(Entry(labelframe,width = 5))
#        self.MaxPos[1].pack()
#        self.MaxPos.append(Entry(labelframe,width = 5))
#        self.MaxPos[2].pack()

#        l3 = Label(labelframe,text = "Equation")
#        l3.pack()
#        self.equation = Entry(labelframe)
#        self.equation.pack()

        l4 = Label(labelframe,text = "Th")
        l4.pack()
        self.Th = Entry(labelframe)
        self.Th.pack()
        self.Th.insert(0,90)

        l5 = Label(labelframe,text = "Tl")
        l5.pack()
        self.Tl = Entry(labelframe)
        self.Tl.pack()
        self.Tl.insert(0,0)


    def EditMaterials(self):
        tempapp = Tk()
        a = EditMaterials(tempapp)
        tempapp.mainloop()

    def createMenus(self):
        self.menubar = Menu(root)

        self.editmenu = Menu(self.menubar,tearoff=0,title="Edit")
        self.editmenu.add_command(label="Material",command=self.EditMaterials)

        self.simulationmenu = Menu(self.menubar,tearoff=0,title="Simulation")
        self.simulationmenu.add_command(label="Demo",command=self.DemoSimulation)

        self.menubar.add_cascade(label="Edit",menu=self.editmenu)
        self.menubar.add_cascade(label="Simulation",menu=self.simulationmenu)

        self.master.config(menu=self.menubar)

    def DemoSimulation(self):
        demosimulation = Tk()
        demosimulation.title("Demo Simulations")
        a = Frame(demosimulation,width = 200)
        a.pack()
        b = DemoSimulation(demosimulation)
        demosimulation.mainloop()
        
    def MaterialList(self):
        labelframe = LabelFrame(self.master,text="Material List")
        labelframe.pack()
        width = 0
        for material in materiallist:
            width = max(width,len(material[0]))
        self.material_list = Listbox(labelframe,height=len(materiallist),width=width)
        for material in materiallist:
            self.material_list.insert(END,material[0])
        self.material_list.pack(padx=0,pady=0)
#        self.scrollbar.config(command=self.material_list.yview)

    def StateList(self):
        self.state = StringVar()
        labelframe = LabelFrame(self.master,text = "State List")
        labelframe.pack()
        self.r1 = Radiobutton(labelframe,text = "isolated",variable = self.state,value='isolated')
        self.r1.pack()
        self.r2 = Radiobutton(labelframe,text = "open",variable = self.state,value='open',command=self.airDepth)
        self.r2.pack()

    def airDepth(self):
        try:
            self.depth.cget('text')
        except AttributeError:
            labelframe=LabelFrame(self.master,text="air depth")
            labelframe.pack()
            self.depth = Spinbox(labelframe,from_=0,to=10)
            self.depth.pack()
        

    def Fixedornot(self):
        self.c1 = Checkbutton(self.master,text = "fixed",onvalue = 1,offvalue = 0, height = 1, width = 10)
        self.c1.pack()

    def setRunning(self):
        if self.startstopButton.cget('text') == 'Start':
            self.startstopButton.config(text= 'Stop')
            self.simulation.setRunning(True)
        else:
            self.startstopButton.config(text = 'Start')
            self.simulationsetRunning(False)

    def createWidgets(self):
        self.submitButton = Button(self, text='Start',command=self.makeObject)
#        self.startstopButton = Button(self, text='Start',command=self.setRunning)
        self.submitButton.pack(side='bottom')
#        self.startstopButton.pack(side='bottom')





app = MainApplication()


root.mainloop() 
