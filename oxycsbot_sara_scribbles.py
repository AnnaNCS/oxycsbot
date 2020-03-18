#!/usr/bin/env python3
"""A simple chatbot that debates with the user about veganism)"""

import random # https://pynative.com/python-random-choice/
from chatbot import ChatBot

class OxyCSBot(ChatBot):

    STATES = [
        'waiting',
        # 'neutral_stance',
        'pro_vegan_stance',
        'anti_vegan_stance',
    ]

    TAGS = {
        # intent
        'veganism': 'veganism',
        'vegan': 'veganism',
        'vegetarian': 'veganism',
        'diet': 'veganism',

        # DETERMINE BOT STANCE BASED ON USER STANCE

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
        'eco-friendly': 'pro_vegan_stance',
        'sustainable': 'pro_vegan_stance',

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
        'unnatural': 'anti_vegan_stance',


        # GIVE ARGUMENT DEPENDING ON THE USER'S RESPONSE
        # ex. 'like burgers': 'arg_a4', ...

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
        # 'neutral',
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

    ALL_ARGS = {
        'arg_p1': 'arg_health',
        'arg_p2': 'arg_environment',
        'arg_p3': 'arg_poverty',
        'arg_p4': 'arg_animal_rights',
        'arg_a1': 'arg_agricultural_stress',
        'arg_a2': 'arg_circle_of_life',
        'arg_a3': 'arg_job_loss',
        'arg_a4': 'arg_yummy_meat',
    }

    FILLER_STATEMENTS = [
        'Yeah, I’m not buying it. Could you elaborate?',
        'Hmm, okay I see your point. Go on.',
    ]



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

        # Use tags and message to determine user stance, then define bot's stance as the opposite
        # If user is neutral/has no opinion, the bot will randomly choose between pro and con

        if 'veganism' in tags:
            for stance in self.STANCES:
                # If user is pro-vegan, bot takes anti-vegan stance
                if 'pro_vegan_stance' in tags:
                    self.stance = 'anti_vegan'

                    # Determine the first argument the bot will use, add to used_arguments

                    return self.go_to_state('anti_vegan_stance')

                # If user is anti-vegan, bot takes pro-vegan stance
                elif 'anti_vegan_stance' in tags:
                    self.stance = 'pro_vegan'

                    # Determine the first argument the bot will use, add to used_arguments

                    return self.go_to_state('pro_vegan_stance')

                # If user is neutral, bot chooses randomly between pro and anti vegan stances
                else:
                    # Choose stance randomly
                    # bot_stances = ['pro_vegan_stance', 'anti_vegan_stance']
                    # self.stance = random.choice(bot_stances)
                    self.stance = random.choice(STANCES)

                    # Or should bot ask more questions to determine user stance?
        elif 'thanks' in tags:
            return self.finish('thanks')
        else:
            return self.finish('confused')


    # ******************** GENERAL STATES (may not be necessary?) ********************

    # This would be the default 'waiting' state
    def wait_for_user_response(self, message, tags):
        response = "testing, send help"
        return response


    # def get_first_arg(self, stance):
    #         if stance == 'pro_vegan_stance':
    #             # choose from ARGS_PRO
    #         else
    #             # choose from ARGS_CON
    #     return argument

    # def get_next_arg(self, stance):
    #     return argument

    def get_neutral_statement(self):
        # Choose a neutral statement randomly
        response = "testing, send help"
        return response

    # def end_convo(self):
    #     return something


    # ******************** PRO-VEGAN STATES ********************

    def on_enter_pro_vegan_stance(self):
        response = "testing, send help"
        return response

    def respond_from_pro_vegan_stance(self, message, tags):

        # I think this is the equivalent of a "wait" state, it's just specific to the stance


        # # Get current argument
        # current_arg = random.choice(ARGS_PRO)

        # # Check against used arguments
        # while current_arg in self.used_arguments:
        #     current_arg = random.choice(ARGS_PRO)

        # if ARGS_PRO in used_arguments:

        # Add random neutral statement if used_arguments has 3 elements

        # If there are still arguments, go to wait_for_user_response state

        # If all arguments are used, end conversation

        response = "testing, send help"
        return response


    # ******************** ANTI-VEGAN STATES ********************

    def on_enter_anti_vegan_stance(self):
        response = "testing, send help"
        return response

    def respond_from_anti_vegan_stance(self, message, tags):
        response = "testing, send help"
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
