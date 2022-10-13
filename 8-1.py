class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathing')

    def move(self):
        print('moving')

    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        # print('eating leaves')
        self.eat_food()

    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()

    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

    def left_Foot_Forward(self):
        print('left foot forward')
    
    def left_Foot_Back(self):
        print('left foot back')
    
    def right_Foot_Forward(self):
        print('right foot forward')
    
    def right_Foot_Back(self):
        print('right foot back')

    def dance(self):
        self.left_Foot_Forward()
        self.left_Foot_Back()
        self.right_Foot_Forward()
        self.right_Foot_Back()
        self.left_Foot_Back()
        self.right_Foot_Back()
        self.right_Foot_Forward()
        self.left_Foot_Forward()

reginald = Giraffes()

harold = Giraffes()

reginald.dance()