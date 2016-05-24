from Tkinter import *
from tkMessageBox import *
from pickle import *

# materiallist = empty((10,6),dtype = object)

constantindex = {'name':0,'conductivity[cal/(cm*s)]':1,'capacity[cal/(g*K)]':2,'density[g/(cm^3)]':3,'number':4}
constant = {}
for key in constantindex.keys():
    constant.update({constantindex[key]:key})


copper = ['copper',9578.0,9.24e-2,8.96,29,'']
iron = ['iron',1920.0,1.07e-1,7.86,26,'']
air = ['air',1,0.240,1.239e-3,'','']
materiallist = [copper,iron]


def UploadMaterials():
    f = open('materiallist.pck','r')
    materiallist = load(f)
    f.close()
    return materiallist

def UpdateFile(filename,arrayname):
    f = open(filename,'w')
    dump(arrayname,f)
    f.close()

def UpdateMaterial(**constant):
    try:
        UploadMaterials()
        pass
    except IOError:
        pass

    if 'name' in constant.keys():
        materiallist.append(range(len(constant.keys())))
        for key in constant.keys():
            materiallist[len(materiallist)-1][constantindex[key]] = constant[key]
        pass
    else:
        pass
    UpdateFile('materiallist.pck',materiallist)


def DeleteMaterial(name):
    for i in range(len(materiallist)-1):
        if name in materiallist[i]:
            materiallist.remove(materiallist[i])
        else:
            continue
    UpdateFile('materiallist.pck',materiallist)

class EditMaterials(Frame):
    def __init__(self,*master):
        Frame.__init__(self,master[0])
        self.master.title("Edit Material")
        self.pack()
        self.Entries()
        self.createWidgets()

    def Entries(self):
        self.addmaterialframe = LabelFrame(self.master,text = "Add Material")
        self.addmaterialframe.pack()

        l0 = Label(self.addmaterialframe,text = "Name")
        l0.pack()
        self.Name = Entry(self.addmaterialframe)
        self.Name.pack()

        l1 = Label(self.addmaterialframe,text = "Conductivity[cal/(m^2*s)]")
        l1.pack()
        self.conductivity = Entry(self.addmaterialframe)
        self.conductivity.pack()

        l2 = Label(self.addmaterialframe,text = "Density[g/cm^3]")
        l2.pack()
        self.density = Entry(self.addmaterialframe)
        self.density.pack()

        l3 = Label(self.addmaterialframe,text = "Capacity[cal/(K*g)]")
        l3.pack()
        self.capacity = Entry(self.addmaterialframe)
        self.capacity.pack()

        self.deleteframe = LabelFrame(self.master, text = "Delete Material")
        self.deleteframe.pack()

        l = Label(self.deleteframe,text = "Name")
        l.pack()
        self.dname = Entry(self.deleteframe)
        self.dname.pack()
        

    def createWidgets(self):
        self.ShowButton = Button(self.master,text = 'Show all Materials',command = self.ShowAllMaterials)
        self.ShowButton.pack(side='top')
        self.AddButton = Button(self.addmaterialframe,text = 'Add',command = self.Addmaterial)
        self.AddButton.pack(side='bottom')
        self.DeleteButton = Button(self.deleteframe,text = 'Delete',command = self.Deletematerial)
        self.DeleteButton.pack(side='bottom')

    def ShowAllMaterials(self):
        f = open("materiallist.pck",'r')
        temp = load(f)
        f.close()
        s = ""
        for i in range(len(temp)):
            s = s + str(temp[i][0]) + "\n"
        showinfo("Material list",s)

    def Addmaterial(self):
        try:
            UpdateMaterial(name = str(self.Name.get()),conductivity = self.conductivity.get(),density = self.density.get(), capacity = self.capacity.get())
        except AttributeError:
            showerror("Attribute Error", "Plz fill all constants information for the material")
            
        showinfo("", "Material information was saved at materiallist.pck")

    def Deletematerial(self):
        name = str(self.dname.get())
        DeleteMaterial(name)
        s = self.dname.get() + " was removed"
        showinfo("", s)
         

