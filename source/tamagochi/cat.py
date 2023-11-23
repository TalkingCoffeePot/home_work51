import random as rd

class Cat():
    age = 1
    hunger = 40
    happiness = 40
    sleep = False
    name = ''

    @staticmethod
    def random_encounter():
        if rd.randint(0, 100) < 33:
            return True
        else:
            return False

    def action_choose(self, action):
        match action:
            case 'feed':
                self.cat_feed()
            case 'play':
                self.cat_play()
            case 'sleep':
                self.cat_sleep()

    def cat_image(self):
        if self.happiness < 30:
            return "/static/img/low.jpg"
        if self.happiness >= 30 and self.happiness <= 70:
            return "/static/img/middle.jpg"
        if self.happiness > 70:
            return "/static/img/high.jpg"
        

    def cat_feed(self):
        if not self.sleep:
            
            self.happiness += 5
            if self.happiness > 100:
                self.happiness = 100
            elif self.happiness < 0:
                self.happiness = 0

            self.hunger += 15
            if self.hunger > 100:
                self.happiness -= 30
                self.hunger = 100
            if self.hunger < 0:
                self.hunger = 0
                
    def cat_play(self):
        if self.sleep:
            self.happiness -= 5
            self.sleep = False
        elif not self.sleep and not self.random_encounter():

            self.happiness += 15
            if self.happiness > 100:
                self.happiness = 100
            elif self.happiness < 0:
                self.happiness = 0

            self.hunger -= 10
            if self.hunger < 0:
                self.hunger = 0

        elif not self.sleep and self.random_encounter():
            self.happiness = 0

    def cat_sleep(self):
        self.sleep = True

