import pygame
import os, sys
import Events.Manager   as EventManager
import Model.main       as model
import View.main        as view
import Controller.main  as controller

def main():

	pygame.init()
	ev_manager = EventManager.EventManager()
	gamemodel = model.GameEngine(ev_manager)
	Control = controller.Control(ev_manager, gamemodel)
	graphics = view.GraphicalView(ev_manager, gamemodel)

	gamemodel.run()
	pygame.quit()
	return 0



main()