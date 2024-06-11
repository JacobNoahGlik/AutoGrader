import ai
from update_token import set_environ
from securepassing import safe_logger as get_token


class Auto_Grader_AI:
    def __init__(self, rubric: str):
        self.rubric: str = rubric
        self._combiner = Auto_Grader_AI.combiner

    def override_combiner(self, combiner) -> None:
        self._combiner = combiner

    def grade(
        self,
        prompt: str,
        max_new_tokens: int = 250
    ) -> str:
        set_environ(get_token())
        return ai.response(self._combiner(prompt, self.rubric))

    @staticmethod
    def combiner(prompt: str, rubric: str, prefix: str = 'You are a grader who\'s job is to grade applications using the following rubric (labeled *RUBRIC*) to grade the following submission (labeled *SUBMISSION*)\n') -> str:
        tripple_quote = '"""'
        return f'{prefix}\n' \
               f'*RUBRIC*\n{tripple_quote}\n{prompt}\n{tripple_quote}\n\n'\
               f'*SUBMISSION*\n{tripple_quote}\n{rubric}\n{tripple_quote}'