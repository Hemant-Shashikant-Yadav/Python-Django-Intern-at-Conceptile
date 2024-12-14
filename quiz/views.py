from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Question, QuizSession

def dashboard(request):
    total_questions = Question.objects.count()
    context = {
        'total_questions': total_questions
    }
    return render(request, 'quiz/dashboard.html', context)


@require_http_methods(["POST"])
def start_quiz(request):
    try:
        num_questions = int(request.POST.get('num_questions', 10))
        
        total_available = Question.objects.count()
        if num_questions <= 0 or num_questions > total_available:
            messages.error(request, f"Please select a number between 1 and {total_available}.")
            return redirect('dashboard')

        quiz_session = QuizSession.generate_quiz(num_questions=num_questions)

        return redirect('quiz_question', session_id=quiz_session.id)

    except ValueError:
        messages.error(request, "Invalid input for number of questions.")
        return redirect('dashboard')


def quiz_question(request, session_id):
    try:
        quiz_session = QuizSession.objects.get(id=session_id)

        question = quiz_session.get_next_question()
        question_numbers = list(range(1, quiz_session.total_questions + 1))

        if not question:
            return redirect('quiz_summary', session_id=session_id)

        total_questions = len(quiz_session.selected_question_ids)
        context = {
            'question': question,
            'session_id': session_id,
            'total_questions': total_questions,
            'current_question_number': quiz_session.total_questions + 1,  # Correct current question number
            'question_numbers': question_numbers,
        }
        return render(request, 'quiz/question.html', context)

    except QuizSession.DoesNotExist:
        messages.error(request, "Invalid quiz session!")
        return redirect('dashboard')


@require_http_methods(["POST"])
def submit_answer(request, session_id):
    try:
        quiz_session = QuizSession.objects.get(id=session_id)

        total_questions = len(quiz_session.selected_question_ids)
        if quiz_session.total_questions >= total_questions:
            messages.info(request, f"You have already answered all {total_questions} questions.")
            return redirect('quiz_summary', session_id=session_id)

        question_id = request.POST.get('question_id')
        user_answer = request.POST.get('answer')

        if not question_id or not user_answer:
            messages.error(request, "Invalid submission!")
            return redirect('quiz_question', session_id=session_id)

        question = Question.objects.get(id=question_id)

        if question.id not in quiz_session.selected_question_ids[:quiz_session.total_questions]:
            quiz_session.total_questions += 1

        if question.correct_answer == user_answer:
            quiz_session.correct_answers += 1
            messages.success(request, "Correct answer!")
        else:
            quiz_session.incorrect_answers += 1
            messages.warning(request, f"Incorrect answer! Correct answer was: {question.correct_answer}")

        quiz_session.save()

        return redirect('quiz_question', session_id=session_id)

    except (QuizSession.DoesNotExist, Question.DoesNotExist):
        messages.error(request, "Invalid quiz session or question!")
        return redirect('dashboard')


def quiz_summary(request, session_id):
    try:
        quiz_session = QuizSession.objects.get(id=session_id)
        
        total_questions = len(quiz_session.selected_question_ids)
        correct_answers = quiz_session.correct_answers

        if total_questions > 0:
            score_percentage = (correct_answers / total_questions) * 100
        else:
            score_percentage = 0
        
        context = {
            'session': quiz_session,
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'incorrect_answers': quiz_session.incorrect_answers,
            'score_percentage': round(score_percentage, 2),
        }
        
        return render(request, 'quiz/summary.html', context)
    
    except QuizSession.DoesNotExist:
        messages.error(request, "Invalid quiz session!")
        return redirect('dashboard')

