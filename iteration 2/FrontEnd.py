import pygame
from pygame.locals import *


# Some global constants...
WHITE = 250,250,250
BLACK = 0,0,0


#Keyboard input and draw to screen

# The screen class that manages how things are drawn - including the main refresh. (called from each
# of the loops in the GameControl)
class Screen():
	# Initialise and transport data.
    def __init__(self, screenSize, name):
        self.screen = pygame.display.set_mode(screenSize)
        pygame.display.set_caption(name)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.text = ""
        self.textpos = 0
        self.options = []
        self.titleFont = pygame.font.SysFont('calibri', 50)
        self.optionFont = pygame.font.SysFont('calibri', 35)


    def whiteout(self):
        self.background.fill(WHITE)
        self.screen.blit(self.background, (0, 0))
        self.options = []
        pygame.display.flip()

    # So far we only need to refresh the text... later we'll have a general purpose update method.
    def refreshText(self):
        #refresh the screen - for temporary text. Will be using group update eventually
        # Clear the background
        self.background.fill(WHITE)
        
        # Not the best place for this calculation as mentioned in the lesson. But ok for now.
        # See if you can fix this... :)
        self.background.blit(self.text, self.textpos) # Draw Title
        for option in self.options:
            text, textpos = option
            self.background.blit(text, textpos) # Draw the Option

        #self.screen.fill(WHITE)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    # For the purposes of getting something working, a simple centre text method
    # We'll probably abandon this for something more sophisticated later
    def setTitleText(self, text):
        #font = pygame.font.SysFont('calibri', 50)
        #font = pygame.font.Font("Arial", 36)
        self.text = self.titleFont.render(text, 1, (10, 10, 10))
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.background.get_rect().centerx
        self.textpos.centery = self.background.get_rect().top + 50

    def setOptionText(self, options, current):
        
        font = pygame.font.SysFont('calibri', 35)
        position = 1
        self.options = []

        for option in options:
            if option == current:
                text = font.render(option, True, (250,10,10)) # If it's our selected option - make it red
            else:
                text = font.render(option, True, (10,10,10)) # Otherwise Black
            textpos = text.get_rect()
            textpos.centerx = self.background.get_rect().centerx
            textpos.centery = self.background.get_rect().top + 100 + (position * 50) # Spaces out the options
            position += 1
            tup = text, textpos
            self.options.append(tup)



        


# Our nice little config read/write function.
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
        #Try loading the config... 
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
            	# Lower case the line, so we don't get any nasty surprises
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
    # the clean config method help solve it
    def cleanConfigFile(self):
    	saveConfig()
            
            
    