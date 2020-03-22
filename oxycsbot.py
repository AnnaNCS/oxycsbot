#!/usr/bin/env python3
"""A simple chatbot that debates with the user about veganism"""

import random # https://pynative.com/python-random-choice/
from chatbot import ChatBot

class OxyCSBot(ChatBot):

    STATES = [
        'waiting',
        'pro_vegan_stance',
        'anti_vegan_stance',
    ]

    TAGS = {
        # intent
        'veganism': 'veganism',
        'vegan': 'veganism',
        'vegetarian': 'veganism',
        'non-animal products': 'veganism',
        'diet': 'veganism',
        'food': 'veganism',

        # DETERMINE BOT STANCE BASED ON USER STANCE

        # pro-vegan
        'pro': 'pro_vegan_stance',
        'animal cruelty': 'pro_vegan_stance', # maybe instead of stance do the specific argument instead?
        'healthy': 'pro_vegan_stance',
        'better for you': 'pro_vegan_stance',
        'poverty': 'pro_vegan_stance',
        'alleviate': 'pro_vegan_stance',
        'global warming': 'pro_vegan_stance',
        'environmentalism': 'pro_vegan_stance',
        'environmental': 'pro_vegan_stance',
        'save the environment': 'pro_vegan_stance',
        'eco-friendly': 'pro_vegan_stance',
        'sustainable': 'pro_vegan_stance',
        'ethics': 'pro_vegan_stance',
        'ethical': 'pro_vegan_stance',
        'unethical': 'pro_vegan_stance',
        'eco food': 'pro_vegan_stance',

        # anti-vegan
        'con': 'anti_vegan_stance',
        'anti': 'anti_vegan_stance',
        'i like meat': 'anti_vegan_stance',
        'job loss': 'anti_vegan_stance',
        'loss of jobs': 'anti_vegan_stance',
        'unemployment': 'anti_vegan_stance',
        'circle of life': 'anti_vegan_stance',
        'soil erosion': 'anti_vegan_stance',
        'agricultural stress': 'anti_vegan_stance',
        'omnivore': 'anti_vegan_stance',
        'unnatural': 'anti_vegan_stance',
        'meat is yummy': 'anti_vegan_stance',
        'burgers': 'anti_vegan_stance',
        'steak': 'anti_vegan_stance',
        'ribs': 'anti_vegan_stance',
        'barbecue': 'anti_vegan_stance',
        'bbq': 'anti_vegan_stance',
        'against nature' : 'anti_vegan_stance',

        # neutral tags?

        # GIVE ARGUMENT DEPENDING ON THE USER'S RESPONSE
        # ex. 'like burgers': 'arg_a4', ...

        # generic
        'thanks': 'thanks',
        'thank you': 'thanks',
        'okay': 'success',
        'bye': 'success',
        'yes': 'yes',
        'yeah' : 'yes',
        'yep': 'yes',
        'yeah': 'success',
        # 'no': 'no',
        # 'nope': 'no',
        'not really': 'failure',
        'never': 'failure',
        'probably no': 'failure',
        'might' : 'success',
        'possibly': 'success',
        'maybe': 'success',
        'of course': 'success',
        'why not': 'success',
        'could be': 'success',
        'have a great day': 'success',
        'I agree': 'success',
        'I am not sure': 'failure',
        'I do not agree': 'failure',
        'I am vegan': 'success',
        'I am not vegan': 'failure',
    }

    STANCES = [
        'pro_vegan',
        'anti_vegan',
    ]

    # bot has pro-vegan stance
    ARGS_PRO = {
         'arg_health': "Being vegan is very good for your health",
         'arg_environment': "Veganism impacts the environment a lot",
         'arg_poverty': "Have to write something here",
         'arg_animal_rights': "Aren't you against animal cruelty?",
    }

    # bot has anti-vegan stance
    ARGS_CON = {
        'arg_agricultural_stress': "Help me out here" ,
        'arg_circle_of_life': "Well, I believe that there is a natural circle of life.",
        'arg_job_loss': "Have you ever thought about how many people will loose their jobs?",
        'arg_meat_taste': "Don't you know the taste of the meat? Would you ever be able to give it up?",
    }

    """
    ALL_ARGS = {
        'arg_p1': 'arg_health',
        'arg_p2': 'arg_environment',
        'arg_p3': 'arg_poverty',
        'arg_p4': 'arg_animal_rights',
        'arg_a1': 'arg_agricultural_stress',
        'arg_a2': 'arg_circle_of_life',
        'arg_a3': 'arg_job_loss',
        'arg_a4': 'arg_meat_taste',
    }


    FILLER_STATEMENTS = [
        'Yeah, I’m not buying it. Could you elaborate?',
        'Hmm, okay I see your point. Go on.',
    ]
    """

    def __init__(self):
        """Initialize the OxyCSBot."""

        super().__init__(default_state='waiting')
        self.stance = None # bot's stance is determined by user stance
        self.used_arguments = [] # keeps track of which arguments have been used to avoid repetition

    """
    def get_args_pro(self, args_pro):
        Pick a pro argument.

        Arguments:

        Returns:
            str: The argument.

        args_con = {
            'arg_health' : "Being vegan is very good for your health",
            'arg_environment' : "Veganism impacts the environemtn a lot",
            'arg_poverty' : "Have to write something here",
            'arg_animal_rights' : "Aren't you against the animal cruelty?",
        }
        return args_con, "What is your opinion"?
    """

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

        if 'veganism' in tags or 'anti_vegan_stance' in tags or 'pro_vegan_stance' in tags: #we might wanna delete this part, as it is unnecessary, the conversation is already about veganism
            for stance in self.STANCES:
                # If user is pro-vegan, bot takes anti-vegan stance
                if 'pro_vegan_stance' in tags:
                    self.stance = 'anti_vegan'
                    # print("is in pro vegan stance")
                    return self.go_to_state('anti_vegan_stance')

                    # Determine the first argument the bot will use, add to used_arguments
                    #
                    #return self.go_to_state('anti_vegan_stance')

                # If user is anti-vegan, bot takes pro-vegan stance
                elif 'anti_vegan_stance' in tags:
                    self.stance = 'pro_vegan'
                    # print("is in anti vegan stance")
                    return self.go_to_state('pro_vegan_stance')

                # If user is neutral, bot chooses randomly between pro and anti vegan stances
                else:
                    # Choose stance randomly
                    self.stance = random.choice(STANCES)

                    if self.stance == 'pro_vegan':
                        return self.go_to_state('pro_vegan_stance')
                    else:
                        return self.go_to_state('anti_vegan_stance')

        elif 'thanks' in tags:
            return self.finish('thanks')
        else:
            return self.finish('confused')


    # ******************** GENERAL STATES (may not be necessary?) ********************

    # This would be the default 'waiting' state
    #def wait_for_user_response(self, message, tags):
        #response = "testing, send help"
        #return response


    # def get_first_arg(self, stance):
    #         if stance == 'pro_vegan_stance':
    #             # choose from ARGS_PRO
    #         else
    #             # choose from ARGS_CON
    #     return argument

    # def get_next_arg(self, stance):
    #     return argument

    #def get_neutral_statement(self):
        # Choose a neutral statement randomly
        #response = "testing, send help"
        #return response

    # def end_convo(self):
    #     return something


    # ******************** PRO-VEGAN STATES ********************

    def on_enter_pro_vegan_stance(self):
        # response = '\n'.join([
        #     random.choice(list(ARGS_PRO.keys())),
        #     'What do you think?',
        # ])
        #current_arg = random.choice(ARGS_PRO)
        #test = "in on_enter_pro_vegan_stance"
        return "yeses"
        #print(random.choice(ARGS_PRO))
        #

    def respond_from_pro_vegan_stance(self, message, tags):

        # I think this is the equivalent of a "wait" state, it's just specific to the stance
        # Get current argument
        #current_arg = random.choice(ARGS_PRO)

        # Check against used arguments
        #while current_arg in self.used_arguments:
        # current_arg = random.choice(ARGS_PRO)

        #if ARGS_PRO in used_arguments:

        # Add random neutral statement if used_arguments has 3 elements

        # If there are still arguments, go to wait_for_user_response state

        # If all arguments are used, end conversation

        test = "in respond_from_pro_vegan_stance"
        return test


    # ******************** ANTI-VEGAN STATES ********************

    def on_enter_anti_vegan_stance(self):
        # response = '\n'.join([
        #     random.choice(list(ARGS_CON.keys())),
        #     'What do you think?',
        # ])
        response = "in on_enter_anti_vegan_stance"
        return response

    def respond_from_anti_vegan_stance(self, message, tags):
        response = "in respond_from_anti_vegan_stance"
        # response = '\n'.join([
        #     random.choice(list(ARGS_CON.keys())),
        #     'What do you think?',
        # ])
        return response



    # ******************** FINISH STATES ********************
    # Send a message then go to the default state (waiting)
    def finish_confused(self):
        return "Tell me something about your diet. What do you think of veganism?"

    def finish_thanks(self):
        return "You're welcome! It was nice talking to you!"


    def finish_success(self):
        return 'Great, I am glad you can see my side of the argument.'

    def finish_fail(self):
        return "You make some good points. I have to say I think you are right about this."



if __name__ == '__main__':
    OxyCSBot().chat()
