from screens.main_menu import MainMenu
from tools import Controler

menu = MainMenu()

controller = Controler(menu)
controller.control()
