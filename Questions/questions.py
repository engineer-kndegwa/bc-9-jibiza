class QuestionStructure(object):
    '''The QuestionStructure Will be imported
    from the Questions package and used to model the question Structure
    '''

    def __init__(self, q_text, answer, options):
        self.q_text = q_text
        self.answer = answer
        self.options = options

    def check_answer(self, answer_provided):
        """Checks whether the answer provided by the user matches
        the one set to is_true"""
        if not answer_provided or len(answer_provided) == 0:
            return 'You haven\'t answered the question'
        a = self.answer.upper()  # actual answer to a
        b = self.answer_provided.upper()  # provided answer to b
        if str(a) == str(b):
            return True
        else:
            return False

    def combine_string(self):
        '''Set How the Question and answer looks when output'''
        q_text_string = self.q_text + '\n'
        for key, letter in enumerate(self.options):
            q_text_string += str(letter).strip() + '==>' + \
                self.options[str(letter)] + '\n'
        return q_text_string
