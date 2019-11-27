from django.db import models
from django.utils import timezone
import datetime



class Event(models.Model):
    event = models.CharField(max_length=100)
    date_of_event = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.event

    
class Question(models.Model):

    question_text = models.CharField(max_length=100)
    type_of_question = models.CharField(max_length=100)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    if Question.type_of_question == "choice":
        choice_text = models.CharField(max_length=100)

        def __str__(self):
            return self.choice_text

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    if Question.type_of_question ==  "text":
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        answer_text = models.CharField(max_length=100)

    elif Question.type_of_question == "choice":
        answer_text = models.ForeignKey(Choice, related_name='', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text




    
