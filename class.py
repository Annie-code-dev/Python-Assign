class Anime :
    def __init__(self, title, character): #constructor
        self.title = title
        self.character = character
    def Act(self):
        return f"I love {self.title} and my best character is {self.character}"
anime1 = Anime("Attack On Title","Mikasa")
anime2 = Anime("Arcane","VI")

print (anime1.Act())
print (anime2.Act())


    
class Panda:
    def speak(self):
        return "Bleat!"

class Koala:
    def speak(self):
        return "growl!"

# Polymorphism in action
for animal in [Panda(), Koala()]:
    print(animal.speak())