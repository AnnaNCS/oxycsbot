#!/usr/bin/env python3
"""A simple chatbot that directs students to office hours of CS professors."""

from chatbot import ChatBot

class OxyCSBot(ChatBot):

    STATES = [
        'waiting',
        'neutral_stance',
        'pro_vegan_stance',
        'anti_vegan_stance',
    ]

    TAGS = {
        # intent
        'veganism': 'veganism',
        'vegan': 'veganism',
        'vegetarian': 'veganism',
        'diet': 'veganism',

        # pro-vegan
        'pro': 'pro_vegan_stance',
        'animal cruelty': 'pro_vegan_stance',
        'healthy': 'pro_vegan_stance',
        'better for you': 'pro_vegan_stance',
        'poverty': 'pro_vegan_stance',
        'alleviate': 'pro_vegan_stance',
        'global warming': 'pro_vegan_stance',
        'environmentalism': 'pro_vegan_stance',
        'save the environment': 'pro_vegan_stance',

        # anti-vegan
        'con': 'anti_vegan_stance',
        'anti': 'anti_vegan_stance',
        'meat is yummy': 'anti_vegan_stance',
        'job loss': 'anti_vegan_stance',
        'loss of jobs': 'anti_vegan_stance',
        'circle of life': 'anti_vegan_stance',
        'soil erosion': 'anti_vegan_stance',
        'agricultural stress': 'anti_vegan_stance',
        'omnivore': 'anti_vegan_stance',

        # generic
        'thanks': 'thanks',
        'okay': 'success',
        'bye': 'success',
        'yes': 'yes',
        'yep': 'yes',
        'no': 'no',
        'nope': 'no',
    }

    STANCES = [
        'pro_vegan',
        'anti_vegan',
        'neutral',
    ]

    # bot has pro-vegan stance
    ARGS_PRO = [
        'arg_health',
        'arg_environment',
        'arg_poverty',
        'arg_animal_rights',
    ]

    # bot has anti-vegan stance
    ARGS_CON = [
        'arg_agricultural_stress',
        'arg_circle_of_life',
        'arg_job_loss',
        'arg_yummy_meat',
    ]

    FILLER_STATEMENTS = [
        'Yeah, I’m not buying it. Could you elaborate?',
        'Hmm, okay I see your point. Go on.',
    ]

    # USED_ARGS = [
    #     'arg_health',
    #     'arg_environment',
    #     'arg_poverty',
    #     'arg_animal_rights',
    #     'arg_agricultural_stress',
    #     'arg_circle_of_life',
    #     'arg_job_loss',
    #     'arg_yummy_meat',
    # ]

    def __init__(self):
        """Initialize the OxyCSBot."""

        super().__init__(default_state='waiting')
        self.stance = None # bot's stance is determined by user stance
        self.used_arguments = [] # keeps track of which arguments have been used to avoid repetition

    # "waiting" state functions

    def respond_from_waiting(self, message, tags):
        """Decide what state to go to from the "waiting" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        self.stance = None
        self.used_arguments = []

        # Use tags and message to determine user stance - bot's stance will be the opposite, or if user is neutral the bot will randomly choose a stance

        if 'veganism' in tags:
            for stance in self.STANCES:
                # If user is pro-vegan, bot takes anti-vegan stance
                if 'pro_vegan_stance' in tags:
                    self.stance = 'anti_vegan'
                    return self.go_to_state('anti_vegan_stance')

                # If user is anti-vegan, bot takes pro-vegan stance
                elif 'anti_vegan_stance' in tags:
                    self.stance = 'pro_vegan'
                    return self.go_to_state('pro_vegan_stance')

                # If user is neutral, bot chooses randomly between pro and anti vegan stances
                else:
                    # Choose stance randomly
                    # Or should bot ask more questions to determine user stance?
        elif 'thanks' in tags:
            return self.finish('thanks')
        else:
            return self.finish('confused')


    # ******************** GENERAL STATES (may not be necessary?) ********************

    def get_next_arg(self, stance):
        return argument

    def get_neutral_statement(self):
        return statement

    def end_convo(self):
        return something


    # ******************** PRO-VEGAN STATES ********************

    def on_enter_pro_vegan_stance(self):
        # Choose one of the arguments for that stance, add to list of used arguments
        # On second or third argument add random neutral statement?
        return response

    def respond_from_pro_vegan_stance(self, message, tags):
        return response


    # ******************** ANTI-VEGAN STATES ********************

    def on_enter_anti_vegan_stance(self):
        return response

    def respond_from_anti_vegan_stance(self, message, tags):
        return response



    # ******************** FINISH STATES ********************
    # Send a message then go to the default state (waiting)

    def finish_confused(self):
        return "You've lost me, sorry. Guess I need to go brush up on my veganism knowledge!"

    def finish_success(self):
        return 'Great, I am glad you can see my side of the argument.'

    def finish_fail(self):
        return "You make some good points. I have to say I think you are right about this."

    def finish_thanks(self):
        return "You're welcome! It was nice talking to you!"

if __name__ == '__main__':
    OxyCSBot().chat()
