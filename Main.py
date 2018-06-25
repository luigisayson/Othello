import Menu 
from GUI import GUI

if __name__ =="__main__":
    dimensions = Menu.Menu().get_dimensions()
    GUI(dimensions[0], dimensions[1]).start()