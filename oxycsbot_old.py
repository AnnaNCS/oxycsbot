#!/usr/bin/env python3
"""A simple chatbot that directs students to office hours of CS professors."""

from chatbot import ChatBot


class OxyCSBot(ChatBot):
    """A simple chatbot that directs students to office hours of CS professors."""
    # Can Sara make edits? Please say it is so

    STATES = [
        'asking_question',
        'vegan',
        'non-vegan',
        'no-opinion',
        'unrecognized_state',
    ]

    TAGS = {
        # intent
        'veganism': 'vegan',
        'non-animal products': 'vegan',
        'diet': 'vegan',
        'food': 'vegan',
        'eco food': 'vegan',
        'eco-friendly': 'vegan',
        'enviromental' : 'vegan',
        'sustainable' : 'vegan',

        # the answere to the vegan question
        'I am vegan' : 'sucess',
        'might' : 'sucess',
        'possibly': 'sucess',
        'maybe': 'sucess',
        'yes': 'sucess',
        'yeah': 'sucess',
        'yep': 'sucess',
        'of course': 'sucess',
        'why not': 'sucess',
        'could be': 'sucess',
        'I am not vegan' : 'failure',
        'not really' : 'failure',
        'never' : 'failure',
        'probably no' : 'failure',
        'no' : 'failure',
        'nope' : 'failure',


        # argument
        'ethics': '',
        'ethical': '',
        '': '',
        'li': 'justin',
        'jeff': 'jeff',
        'miller': 'jeff',
        'celia': 'celia',
        'hsing-hau': 'hsing-hau',
        'umit': 'umit',
        'yalcinalp': 'umit',

        # generic
        'thanks':'thank you',
        'have a great day': 'have a great day',
        'have a great day': 'success',
        'okay': 'success',
        'I agree' : 'success',
        'bye': 'success',
        'I am not sure' : 'failure',
        'I do not agree' : 'failure',
        'yes': 'yes',
        'yep': 'yes',
        'no': 'no',
        'nope': 'no',
    }

    def __init__(self):
        """Initialize the OxyCSBot.

        The `professor` member variable stores whether the target professor has
        been identified.
        """
        super().__init__(default_state='asking_question')
        //self.professor = None

    def get_responese(self, tag):
        """Find the office hours of a professor.

        Arguments:
            professor (str): The professor of interest.

        Returns:
            str: The office hours of that professor.
        """
        office_hours = {
            'celia': 'unknown',
            'hsing-hau': 'MW 3:30-4:30pm; F 11:45am-12:45pm',
            'jeff': 'W 4-5pm; Th 12:50-1:50pm; F 4-5pm',
            'justin': 'T 3-4pm; W 2-3pm; F 4-5pm',
            'kathryn': 'MF 4-5:30pm',
            'umit': 'M 3-5pm; W 10am-noon, 3-5pm',
        }
        return office_hours[professor]

    def get_office(self, professor):
        """Find the office of a professor.

        Arguments:
            professor (str): The professor of interest.

        Returns:
            str: The office of that professor.
        """
        office = {
            'celia': 'Swan 232',
            'hsing-hau': 'Swan 302',
            'jeff': 'Fowler 321',
            'justin': 'Swan B102',
            'kathryn': 'Swan B101',
            'umit': 'Swan 226',
        }
        return office[professor]

    # "waiting" state functions

    def respond_from_waiting(self, message, tags):
        """Decide what state to go to from the "waiting" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        self.professor = None
        if 'office-hours' in tags:
            for professor in self.PROFESSORS:
                if professor in tags:
                    self.professor = professor
                    return self.go_to_state('specific_faculty')
            return self.go_to_state('unknown_faculty')
        elif 'thanks' in tags:
            return self.finish('thanks')
        else:
            return self.finish('confused')

    # "specific_faculty" state functions

    def on_enter_specific_faculty(self):
        """Send a message when entering the "specific_faculty" state."""
        response = '\n'.join([
            f"{self.professor.capitalize()}'s office hours are {self.get_office_hours(self.professor)}",
            'Do you know where their office is?',
        ])
        return response

    def respond_from_specific_faculty(self, message, tags):
        """Decide what state to go to from the "specific_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        if 'yes' in tags:
            return self.finish('success')
        else:
            return self.finish('location')

    # "unknown_faculty" state functions

    def on_enter_unknown_faculty(self):
        """Send a message when entering the "unknown_faculty" state."""
        return "Who's office hours are you looking for?"

    def respond_from_unknown_faculty(self, message, tags):
        """Decide what state to go to from the "unknown_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        for professor in self.PROFESSORS:
            if professor in tags:
                self.professor = professor
                return self.go_to_state('specific_faculty')
        return self.go_to_state('unrecognized_faculty')

    # "unrecognized_faculty" state functions

    def on_enter_unrecognized_faculty(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        return ' '.join([
            "I'm not sure I understand - are you looking for",
            "Celia, Hsing-hau, Jeff, Justin, Kathryn, or Umit?",
        ])

    def respond_from_unrecognized_faculty(self, message, tags):
        """Decide what state to go to from the "unrecognized_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        for professor in self.PROFESSORS:
            if professor in tags:
                self.professor = professor
                return self.go_to_state('specific_faculty')
        return self.finish('fail')

    # "finish" functions

    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm just a simple bot that can't understand much. You can ask me about office hours though!"

    def finish_location(self):
        """Send a message and go to the default state."""
        return f"{self.professor.capitalize()}'s office is in {self.get_office(self.professor)}"

    def finish_success(self):
        """Send a message and go to the default state."""
        return 'Great, let me know if you need anything else!'

    def finish_fail(self):
        """Send a message and go to the default state."""
        return "I've tried my best but I still don't understand. Maybe try asking other students?"

    def finish_thanks(self):
        """Send a message and go to the default state."""
        return "You're welcome!"


if __name__ == '__main__':
    OxyCSBot().chat()
