import pygame
from pygame.locals import *

#Keyboard input and draw to screen


# screen class that manages how things are drawn - including the main refresh. (called from each
# of the loops in the GameControl)
class Screen():
	# Initialise and transporting data.
    def __init__(self, screenSize, name):
        self.white = 250,250,250
        self.black = 0,0,0
        self.screen = pygame.display.set_mode(screenSize)
        pygame.display.set_caption(name)
        self.background = pygame.Surface(self.screen.get_size()).convert()

    # just need to refresh the text for this iteration
    def refreshText(self, text):
        #refresh the screen - for temporary text. Will be using group update eventually
        # Clear the background
        self.background.fill(self.white)

        self.centreText(text)

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    # For the purposes of getting something working, a simple centre text method
    # We'll probably abandon this for something more sophisticated later
    def centreText(self, text):
        font = pygame.font.Font(None, 36)
        text = font.render(text, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        textpos.centery = self.background.get_rect().centery


        self.background.blit(text, textpos)


# config read/write function.
class OptionConfigs:
	# Initialise some defaults... but then read in from file.
    def __init__(self, file = 'config.txt'):
        #initialise with defaults before reading in config
        self.time = 3
        self.rounds = 1
        self.sound = 3
        self.music = 3
        self.keysP1 = [32]*7
        self.keysP2 = [32]*7
        self.file = file
        #loading the config
        try:
            self.loadConfig()
        except:
            print('Error: check {} exists'.format(self.file))

    # Load in the config
    def loadConfig(self):
    	# Open the file
        with open(self.file, encoding='utf-8') as txtfile:
            # go through each line
            for line in txtfile:
            	# Lower case the line to avoid errors
                line.lower()
                # a result of -1 means it wasn't found
                if line.find('time=') != -1:
                    self.time = int(line.strip('time='))
                if line.find('rounds=') != -1:
                    self.rounds = int(line.strip('rounds='))
                if line.find('video=') != -1:
                    self.video = int(int(line.strip('video=')))
                if line.find('sound=') != -1:
                    self.sound = int(line.strip('sound='))
                if line.find('music=') != -1:
                    self.music = int(line.strip('music='))
                #We'll iterate over the keys to add them
                if line.find('keysP1=') != -1:
                    keys = line.strip('keysP1=').split('/')
                    keys.remove('\n')
                    for i in range(len(keys)):
                        keys[i]=int(keys[i])
                    self.keysP1 = keys
                if line.find('keysP2=') != -1:
                    keys = line.strip('keysP2=').split('/')
                    keys.remove('\n')
                    for i in range(len(keys)):
                        keys[i]=int(keys[i])
                    self.keysP2 = keys

    # Save the config in the format that works
    def saveConfig(self):
        with open(self.file, mode='w', encoding='utf-8') as txtfile:
            txtfile.write('time='+str(self.time)+'\n')
            txtfile.write('rounds='+str(self.rounds)+'\n')
            txtfile.write('sound='+str(self.sound)+'\n')
            txtfile.write('music='+str(self.music)+'\n')
            txtfile.write('keysP1=')
            for i in self.keysP1:
                txtfile.write(str(i)+'/')
            txtfile.write('\nkeysP2=')
            for i in self.keysP2:
                txtfile.write(str(i)+'/')
            txtfile.write('\n')
    
    # Sometimes the config file can get currupted by it being opened...
    # This clean config method solves helps solve it
       def cleanConfigFile(self):
    	saveConfig()
            
            
    