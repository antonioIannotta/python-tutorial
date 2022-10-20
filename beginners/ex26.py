import datetime


class SMS:

    def __init__(self, from_number, time_arrived, text, has_been_viewed=False):
        self.has_been_viewed = has_been_viewed
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text = text



class SmsStore:

    def __init__(self, message_list=None):
        if message_list is None:
            message_list = list()
        self.new_list = message_list

    def add_new_arrival(self, sms):
        self.new_list.append(sms)

    def message_count(self):
        return len(self.new_list)

    def get_message(self, message_index):
        message = self.new_list[message_index]
        return message.from_number + " " + message.time_arrived + " " + message.text


message1 = SMS("123", str(datetime.datetime.now()), "Ciao 1")
message2 = SMS("456", str(datetime.datetime.now()), "Ciao 2")
message3 = SMS("789", str(datetime.datetime.now()), "Ciao 3")

mailbox = SmsStore()
mailbox.add_new_arrival(message1)
mailbox.add_new_arrival(message2)
mailbox.add_new_arrival(message3)

print(mailbox.message_count())
for counter in range(mailbox.message_count()):
    print(mailbox.get_message(counter))


