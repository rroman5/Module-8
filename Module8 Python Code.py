class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses

player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)
print("There are three tasks you can choose")
print("1. Task1 - Climb a mountain")
print("2. Task2 - Cook a meal ")
print("3. Task3 - Write a book ")
option = input("Please enter one of the following options (1-3)")

if option == '1':
    task = ['rope', 'coat', 'first aid kit']
    not_allowed_state = 'slow'
    print("You will need Coat and first aid kit, cannot have", not_allowed_state)
if option == '2':
    task = ['pan', 'groceries']
    cannot_size = 'small'
    print ("Cannot have small")
if option == '3':
    task = ['pen', 'paper', 'idea',]
    confusion = 'confusion'
    print("Cannot have confusions")


