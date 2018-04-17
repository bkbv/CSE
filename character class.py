class Character(object):
    def __init__(self, name, health, description, talk):
        # Things a Character has
        self.name = name
        self.health = health
        self.description = description
        self.talk = talk

    def talk(self):
        print("hello")

    def (self):
        print("")

    def Character_description(self):
        if self.description:
            print("Tall, Long hair, Brown eyes")