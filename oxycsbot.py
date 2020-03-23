#!/usr/bin/env python3
"""A simple chatbot that debates with the user about veganism"""

import random  # https://pynative.com/python-random-choice/
from chatbot import ChatBot


class OxyCSBot(ChatBot):

    STATES = [
        'waiting',
        'pro_vegan_stance',
        'anti_vegan_stance',
    ]

    TAGS = {
        # vegan topic
        'veganism': 'veganism',
        'vegan': 'veganism',
        'vegetarian': 'veganism',
        'non-animal products': 'veganism',
        'diet': 'veganism',
        'food': 'veganism',

        # pro-vegan
        'pro': 'pro_vegan_stance',
        'animal cruelty': 'pro_vegan_stance',
        'animal rights': 'pro_vegan_stance',
        'healthy': 'pro_vegan_stance',
        'better for you': 'pro_vegan_stance',
        'poverty': 'pro_vegan_stance',
        'alleviate': 'pro_vegan_stance',
        'global warming': 'pro_vegan_stance',
        'environmentalism': 'pro_vegan_stance',
        'environmental': 'pro_vegan_stance',
        'save the environment': 'pro_vegan_stance',
        'eco-friendly': 'pro_vegan_stance',
        'eco friendly': 'pro_vegan_stance',
        'eco food': 'pro_vegan_stance',
        'eco': 'pro_vegan_stance',
        'sustainable': 'pro_vegan_stance',
        'ethics': 'pro_vegan_stance',
        'ethical': 'pro_vegan_stance',
        'unethical': 'pro_vegan_stance',

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
        'against nature': 'anti_vegan_stance',

        # Next phase: convert above tags to referencing specific arguments
        # ex. 'like burgers': 'arg_a4', ...

        # generic
        'thanks': 'thanks',
        'thank you': 'thanks',
        'okay': 'success',
        'bye': 'success',
        'not really': 'failure',
        'never': 'failure',
        'probably no': 'failure',
        'might': 'success',
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

        # greetings
        'hi': 'hello',
        'hello': 'hello',
        'sup': 'hello',
        'hallo': 'hello',
        'hey': 'hello',

        'reset': 'reset', # added for testing purposes only
    }

    STANCES = [
        'pro_vegan',
        'anti_vegan',
    ]

    # bot has pro-vegan stance
    ARGS_PRO = {
        'arg_health': "Being vegan is very good for your health",
        'arg_environment': "Veganism impacts the environment a lot",
        'arg_poverty': "A transition to veganism could alleviate poverty.",
        'arg_animal_rights': "Aren't you against animal cruelty?",
    }

    # bot has anti-vegan stance
    ARGS_CON = {
        'arg_agricultural_stress': "Do you know how much land is required to grow the crops needed for a vegan lifestyle? Way more than we're using now!",
        'arg_circle_of_life': "Well, I believe that there is a natural circle of life.",
        'arg_job_loss': "Have you ever thought about how many people will lose their jobs if everyone became vegan?",
        'arg_meat_taste': "Don't you like the taste of the meat? Would you ever be able to give it up?",
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

    # ******************** WAITING STATE FUNCTIONS ********************

    def respond_from_waiting(self, message, tags):
        """Decide what state to go to from the "waiting" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """

        if 'pro_vegan_stance' in tags or 'anti_vegan_stance' in tags or 'veganism' in tags:
            # Use tags and message to determine user stance, then define bot's stance as the opposite
            # If user is neutral/has no opinion, the bot will randomly choose between pro and con
            if self.stance is None:

                # If user is pro-vegan, bot takes anti-vegan stance
                if 'pro_vegan_stance' in tags:
                    self.stance = 'anti_vegan'
                    return "Ugh, I don't understand how people can do the veganism thing. Why do you believe in it?"

                # If user is anti-vegan, bot takes pro-vegan stance
                elif 'anti_vegan_stance' in tags:
                    self.stance = 'pro_vegan'
                    return "Wait, you don't believe in veganism? Why not?"

                # If user is neutral, bot chooses randomly between pro and anti vegan stances
                elif 'veganism' in tags:
                    # return self.finish('neutral')
                    self.stance = random.choice(STANCES)

                    if self.stance == 'pro_vegan':
                        return "Wait, you don't believe in veganism? Why not?"
                    else:
                        return "Ugh, I don't understand how people can do the veganism thing. Why do you believe in it?"
                else:
                    return self.finish('neutral')

            # If bot already has a stance, return to the response state for that stance
            else:
                if self.stance == 'anti_vegan':
                    return self.go_to_state('anti_vegan_stance')
                else:
                    return self.go_to_state('pro_vegan_stance')

        # For testing purposes only
        elif 'reset' in tags:
            self.stance = None
            self.used_arguments = []
            return "Stance and used arguments cleared."
        elif 'hello' in tags:
            return self.finish('hello')

        # If user message is unrelated to veganism, choose appropriate response for bot
        elif 'thanks' in tags:
            return self.finish('thanks')
        else:
            return self.finish('confused')

    # ******************** PRO-VEGAN STATES ********************

    def on_enter_pro_vegan_stance(self):
        # return "entered pro vegan stance"
        first_arg = ARGS_PRO['arg_health']
        return first_arg
        # if self.stance == None:
        # if len(self.used_arguments) == 0:
        #     return "Wait, you don't believe in veganism? Why not?"
        # else:
        #     return "I have a stance" # self.go_to_state('pro_vegan_stance')

    def respond_from_pro_vegan_stance(self, message, tags):
        # return "in pro vegan response state"
        return ARGS_PRO['arg_health']
        current_arg = random.choice(ARGS_PRO.keys())
        self.used_arguments.append(argument)
        # return self.go_to_state('pro_vegan_stance')
        return current_arg

        # # If there are still unused arguments, go back to pro_vegan_stance state
        # if len(self.used_arguments < 4):
        #     current_arg = random.choice(x for x in ARGS_PRO if x not in self.used_arguments)
        #     self.used_arguments.append(argument)
        #     return self.go_to_state('pro_vegan_stance')

        # # If all arguments are used, end conversation
        # else:
        #     return self.finish('success')

    # ******************** ANTI-VEGAN STATES ********************

    def on_enter_anti_vegan_stance(self):
        return "entered anti vegan stance"
        # response = "Ugh, I don't understand how people can do the veganism thing. Why do you believe in it?"
        # return response

    def respond_from_anti_vegan_stance(self, message, tags):
        # return "in anti vegan response state"
        return ARGS_CON['arg_meat_taste']
        current_arg = random.choice(ARGS_CON.keys())
        self.used_arguments.append(argument)
        # return self.go_to_state('anti_vegan_stance')
        return current_arg

    # ******************** FINISH STATES ********************
    # Send a message then go to the default state (waiting)
    def finish_neutral(self):
        return "Tell me something about your diet. What do you think of veganism?"

    def finish_confused(self):
        return "You've lost me. Could you clarify that?"

    def finish_thanks(self):
        return "You're welcome! It was nice talking to you!"

    def finish_hello(self):
        return "Hello to you too! :)"

    def finish_success(self):
        return "Great, I am glad you can see my side of the argument."

    def finish_fail(self):
        return "You make some good points. I have to say I think you are right about this."


if __name__ == '__main__':
    OxyCSBot().chat()
