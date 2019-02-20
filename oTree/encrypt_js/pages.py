from ._builtin import Page, WaitPage
from .models import Constants

class Task(Page):
    form_model = 'player'
    form_fields = ['performance', 'mistakes']
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period
    
    def vars_for_template(self):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90/Constants.letters_per_word
        return{'legend_list': legend_list,
               'task_list': task_list,
               'task_width': task_width}

class Results(Page):
    pass

page_sequence = [Task,
                 Results]
