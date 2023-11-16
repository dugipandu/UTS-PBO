class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        return "Sparrow can fly."

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly."

def let_bird_fly(bird):
    print(bird.fly())

sparrow = Sparrow()
penguin = Penguin()

let_bird_fly(sparrow)
let_bird_fly(penguin)
