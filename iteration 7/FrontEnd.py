import pygame
from pygame.locals import *
import Launcher


# Some global constants...
WHITE = 250,250,250
BLACK = 0,0,0


#Keyboard input and draw to screen

# screen class that manages how things are drawn - including the main refresh. (called from each
# of the loops in the GameControl)
class Screen():
	# Initialise what is needed and transport data.
    def __init__(self, screenSize, name, font = 'calibri'):
        self.screen = pygame.display.set_mode(screenSize)
        pygame.display.set_caption(name)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.text = ""
        self.promptText = ()
        self.titleText = ()
        #self.textpos = 0
        self.options = []
        self.titleFont = pygame.font.SysFont(font, 50)
        self.optionFont = pygame.font.SysFont(font, 35)
        self.promptFont = pygame.font.SysFont(font, 18)


    def whiteout(self):
        self.background.fill(WHITE)
        self.screen.blit(self.background, (0, 0))
        self.options = []
        pygame.display.flip()

    def refreshMenu(self, page, withConfigs = False, configs = []):

        self.setTitleText(page.title)
        self.setOptionText(page, withConfigs, configs)
        self.setPromptText(page.prompt)
        self.refreshText()



    # refresh the text
    def refreshText(self):
        
        self.background.fill(WHITE)
        
        self.background.blit(self.titleText[0], self.titleText[1]) # Draw Title
        self.background.blit(self.promptText[0], self.promptText[1])
        for option in self.options:
            text, textpos = option
            self.background.blit(text, textpos) # Draw the Option

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def setTitleText(self, text):
        text = self.titleFont.render(text, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        textpos.centery = self.background.get_rect().top + 50
        self.titleText = text, textpos



    def setPromptText(self, text):
        text = self.promptFont.render(text, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        textpos.centery = self.background.get_rect().bottom - 50
        self.promptText = text, textpos

    def getConfigOption(self,name, configs):
        if name == "Time":
            return str(configs.time)
        elif name == "Rounds":
            return str(configs.rounds)
        elif name == "Sound Volume":
            return str(configs.sound)
        elif name == "Music Volume":
            return str(configs.music)

    def setOptionText(self, page, withConfigs, configs):
        font = self.optionFont
        position = 1
        self.options = []
        
        options = page.connectedPages
        
        for option in options:
            name = option.name
            if withConfigs:
                name = option.name + " .......... " + self.getConfigOption(option.name, configs)

            text = font.render(name, True, (option.colour))
            fHeight = font.size(name)[1]
            textpos = text.get_rect()
            
            textpos.centerx = self.background.get_rect().centerx
            textpos.centery = self.background.get_rect().top + 100 + (position * fHeight * 2) # Spaces out the options
            position += 1
            tup = text, textpos
            self.options.append(tup)




# config read/write function.
class OptionConfigs:
	# Initialise some defaults... but then read in from file.
    def __init__(self, file = 'config.txt'):
        #initialise with defaults before reading in config
        self.time = 3
        self.rounds = 1
        self.sound = 3
        self.music = 3
        self.keysP1 = ["blank"]*7
        self.keysP2 = ["blank"]*7
        self.file = file
        #Try loading the config
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
            	# Lower case the line, so avoid errors
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
                if line.find('keysP1=') != -1:
                    keys = line.strip('keysP1=').split('/')
                    keys.remove('\n')
                    self.keysP1 = keys
                if line.find('keysP2=') != -1:
                    keys = line.strip('keysP2=').split('/')
                    keys.remove('\n')
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
                txtfile.write(i+'/')
            txtfile.write('\nkeysP2=')
            for i in self.keysP2:
                txtfile.write(i+'/')
            txtfile.write('\n')
    
    # Sometimes the config file can get corrupted by it being opened...
    # this clean config function helps it
    def cleanConfigFile(self):
    	self.saveConfig()


if __name__ == "__main__":          
    #op = OptionConfigs()
    #op.cleanConfigFile()
    Launcher.main()

