from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('srikirti', 'Ms.', 21, 4.5)

friend_one = Spy('prachi', 'Ms.', 4.6, 20)
friend_two = Spy('priti', 'Ms.', 4.7, 21)
friend_three = Spy('krishn', 'Dr.', 4.95,27)
friend_four = Spy('ritu', 'Ms.', 4.8,25)



friends = [friend_one, friend_two, friend_three, friend_four]

