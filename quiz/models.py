from django.db import models
import uuid
import random

class Question(models.Model):
    text = models.TextField(help_text="Question text")
    option_a = models.CharField(max_length=200, help_text="First option")
    option_b = models.CharField(max_length=200, help_text="Second option")
    option_c = models.CharField(max_length=200, help_text="Third option")
    option_d = models.CharField(max_length=200, help_text="Fourth option")
    
    ANSWER_CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D')
    ]
    
    correct_answer = models.CharField(
        max_length=1, 
        choices=ANSWER_CHOICES, 
        help_text="Correct answer option"
    )
    
    def __str__(self):
        return self.text[:50]

class QuizSession(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    selected_question_ids = models.JSONField(default=list)
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def generate_quiz(cls, num_questions=10):
        all_question_ids = list(Question.objects.values_list('id', flat=True))

        selected_ids = random.sample(all_question_ids, min(num_questions, len(all_question_ids)))

        quiz_session = cls.objects.create(
            selected_question_ids=selected_ids
        )
        return quiz_session
    
    def get_current_question(self):
      
        if not self.selected_question_ids:
            return None
        
        questions = Question.objects.filter(id__in=self.selected_question_ids)
        return questions.first()
    
    def get_next_question(self):
      
        answered_ids = self.selected_question_ids[:self.total_questions] 
        remaining_questions = [q_id for q_id in self.selected_question_ids if q_id not in answered_ids]
        
        if not remaining_questions:
            return None  
        
        next_question_id = remaining_questions[0]  
        return Question.objects.get(id=next_question_id)

    def __str__(self):
        return f"Quiz Session {self.id}"