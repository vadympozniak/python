"""TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
if the channel N or 'name' exists in the list, or "No" - in the other case.

The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above."""


CHANNELS = ['BBC / #1 / [0]', 'Discovery / #2 / [1]', 'TV1000 / #3 / [2]']


class TVController:
    my_channel = 0

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        TVController.my_channel = 0
        return self.channels[TVController.my_channel]

    def last_channel(self):
        TVController.my_channel = -1
        return self.channels[TVController.my_channel]

    def turn_channel(self, number):
        try:
            if int(number) > len(self.channels):
                print('Channel not found')
            else:
                TVController.my_channel = int(number) - 1
                return self.channels[TVController.my_channel]
        except ValueError:
            print('Enter the number.')

    def next_channel(self):
        TVController.my_channel += 1
        if TVController.my_channel == len(self.channels):
            TVController.my_channel = 0
        return self.channels[TVController.my_channel]

    def previous_channel(self):
        TVController.my_channel -= 1
        if TVController.my_channel == len(self.channels) * (-1) - 1:
            TVController.my_channel = -1
        return self.channels[TVController.my_channel]

    def current_channel(self):
        return self.channels[TVController.my_channel]

    def is_exist(self, question_channel):
        question_channel = str(question_channel)
        if question_channel.isdigit():
            if int(question_channel) > len(self.channels):
                return 'No'
            else:
                return 'Yes'
        else:
            if question_channel not in self.channels:
                return 'No'
            else:
                return 'Yes'


controller = TVController(CHANNELS)

if __name__ == '__main__':
    print(f'Channels: {controller.channels}')
    print(f'First channel: {controller.first_channel()}')
    print(f'Last channel: {controller.last_channel()}')
    print(f"Turn channel: {controller.turn_channel('3')}")
    print(f'Next channel: {controller.next_channel()}')
    print(f'Previous channel: {controller.previous_channel()}')
    print(f'Current channel: {controller.current_channel()}')
    print(f"Channel is exist(num) {controller.is_exist('4')}")
    print(f"Channel is exist (name): {controller.is_exist('BBC / #1 / [0]')}")