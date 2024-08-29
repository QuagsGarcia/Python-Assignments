# Import random module to select random questions
import random
#Defines a class named UserSurvey
class UserSurvey:
    #Initialize the class with a set of questions and responses, and an empty set to track user input
    def __init__(self):
        self.questions_and_answers = {
        # defines a set of questions with initial answers set to None
            "What's your name?": None,
            "How old are you?": None,
            "Where are you from?": None,
            "Do you have any hobbies? ": None,
            "How do you like to spend your free time?": None,
            "What kind of music are you into?": None,
            "Do you have any pets? ": None,
            "Who is one of your favorite celebrity role models?": None,
            "What is your dream job?": None,
            "If you could travel anywhere in the world, where would you go?": None,
            "What skill would you like to master? ": None,
            "What do you like to learn about?": None,
            "What has been the highlight of this past week?": None,
            "What has been the highlight of your year? ": None,
            "Have you read any intriguing books lately?": None,
            "What’s your current favorite TV show/movie?": None,
            "Do you have any nicknames?": None,
            "Where did you grow up?": None,
            "What is your favorite food?": None,
            "What is your favorite sport?": None,
            "What is something you’ve always wanted to learn?": None,
            "If you could trade places with anyone for a week, who would it be?": None,
            "What fictional character do you most relate to?": None,
            "What do you daydream about?": None,
        }
        self.asked_questions = set()
    # Method to start the survey
    def start_survey(self):
        # Displays a welcome message
        print("Welcome to the aiChatbot! Type '/responses' to see your answers at any time.")
        # Loop until all the questions are answered
        while self.questions_and_answers:
            # Get a random unanswered question
            question = self.get_random_question()
            if question == None:
                break
            # Add the question to the set of asked questions
            self.asked_questions.add(question)
            #prompt the user for an answer to the current question
            answer = input(f"{question} ")
            # checks to see if the user wants to see responses
            if answer == "/responses":
                # displays the users responses
                user_survey.display_results()
                # prompts the user for an answer to the current question again
                answer = input("\n\nAgain, " + f"{question} ")
                self.questions_and_answers[question] = answer
            else:
                # Update the answer for the current question in the dictionary
                self.questions_and_answers[question] = answer
        # display message when all the questions have been answered
        print("\nI have no more questions. Type '/responses' to see your answers.")
    # Method to get a random unanswered question
    def get_random_question(self):
        # Calculates the set difference to find remaining unanswered questions
        remaining_questions = list(set(self.questions_and_answers.keys()) - self.asked_questions)
        # checks to see if there are remaining questions
        if remaining_questions:
            # returns a randomly selected question from the remaining ones
            return random.choice(remaining_questions)
        # returns none if there are no remaining questions
        return None
    # Method to display the users responses
    def display_results(self):
        # Displays a message and iterate over quiestions and answers to print them
        print("\nHere are your responses:")
        for question, answer in self.questions_and_answers.items():
            print(f"{question}: {answer}")
# entry point of the program
if __name__ == "__main__":
    # create an instance of the UserSurvey class
    user_survey = UserSurvey()
    # starts the survey
    user_survey.start_survey()
    # continue to handle user input until the user types the command to see responses
    while True:
        command = input("You: ")
        if command.lower() == "/responses":
            user_survey.display_results()
            command = input("\n\nYou: ")
        else:
            print("Unknown command. Type '/responses' to see your answers.")