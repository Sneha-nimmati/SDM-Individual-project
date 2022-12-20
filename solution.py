from operator import ne

question_list = {
    1:"Welcome to the game! Think or a desian pattern and answer these following yes/no questions. Ready?",
    2:"Does it provide the object creation mechanism that enhance the flexibilities of the existing code?",
    3:"Is it responsible for how one class communicates with others",
    4:"Does it explain how to assemole objecis and classes ino a larger structure and simplifies the structure genuino the rolatinnshins?",
    5:"Does it ensure you have at most one instance of a class in your application?",
    6:"Does it provide a mechanism to the context to change its behavior?",
    7:"Does it attach additional behavior to an object dynamically at run-time?",
    8:"Is changing behavior built into its scheme?",
    9:"Does it allow a group of objects to be notified when some state changes?",
    10:"Is it Singleton Pattern?",
    11:"Is it Builder Pattern?",
    12:"Is it State Pattern?",
    13:"Is it Strategy Pattern?",
    14:"Is Observer Pattern?",
    15:"Is it Command Pattern?",
    16:"Is it Decorator Pattern?",
    17:"If Adapter Pattern?",
    18:"Woohoo! I quessed it! Try again?",
    19:"Oops! Something went wrong.Try again?",
    99:"Exit the game"
}
yes_patterns = [(0,1),(1,2),(2,5), (3,6), (4,7), (5,10), (6, 8),(7,16),(8,12),(9,14),(10,18),(11,18),(12,18),(13,18),(14,18),
                (15,18),(16,18),(17,18),(18,1),(19,1)]
no_patterns = [(1, 99),(2,3), (3,4), (4,19),(5, 11), (6, 9), (7, 17),(8,13),(9,15),(10,19),(11,19),(12,19),(13,19),(14,19),
                (15,19),(16,19),(17,19),(19, 99),(18,99)]

class DesignPatternGame():
    def __init__(self):
        self.next_question_index = 1
        self.previous_question_index = 0
        self.answer = "yes"
        self.yes_patterns = yes_patterns
        self.no_patterns = no_patterns

    def start(self):
        next_question_index = self.next_question_index
        previous_question_index = self.previous_question_index
        answer = self.answer
        while next_question_index != 99:
            if previous_question_index == 0:
                next_question,next_question_index = self.get_question(previous_question_index, answer)
                answer = input(next_question)
                previous_question = next_question
                previous_question_index = next_question_index
            else:
                previous_question_index = [i for i in question_list if question_list[i]==previous_question][0]
                next_question,next_question_index = self.get_question(previous_question_index, answer)
                if next_question_index == 99:
                    continue
                else:
                    answer = input(next_question)
                    previous_question = next_question
                    previous_question_index = next_question_index

    def get_question(self, pre_ques, pre_ans):
        if pre_ans.lower() == "yes":
            next_question, next_question_index= self.answerYes(pre_ques,  self.yes_patterns)
        else:
            next_question, next_question_index= self.answerNo(pre_ques,  self.no_patterns)
        return next_question,next_question_index

    def get_pattern(self, pre_ques, pattern_list):
        get_tuple = [i for i in pattern_list if i[0] == pre_ques]
        next_ques = question_list[get_tuple[0][1]]
        return next_ques, get_tuple[0][1]

    def answerYes(self, pre_ques, patterns):
        next_question, next_question_index= self.get_pattern(pre_ques,  patterns)
        return next_question,next_question_index

    def answerNo(self,pre_ques, patterns):
        next_question,next_question_index = self.get_pattern(pre_ques, patterns)
        return next_question,next_question_index



    
if __name__ == "__main__":
    design_pattern = DesignPatternGame()
    design_pattern.start()




            
            


    