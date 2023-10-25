# 导入所需的模块和类
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, UserQuiz
from accounts.models import UserProfile
from .forms import AnswerForm
from django.db.models import Q

# 定义视图函数
@login_required
def hello_view(request):
    return render(request, 'myapp/hello.html')  # 返回 hello.html 模板

@login_required
def quiz_already_answered(request, question_id=None):
    user = request.user

    # 查找下一个未回答的问题
    unanswered_questions = Question.objects.exclude(
        userquiz__user=user, userquiz__user_answer__isnull=False)
    next_question = unanswered_questions.first()

    if question_id:
        # 如果提供了 question_id 参数，重定向到 take_quiz 视图
        return redirect('take_quiz', question_id=question_id)

    if next_question:
        # 检查下一个问题的索引是否在未回答的问题范围内
        if next_question.id <= unanswered_questions.count():
            # 如果有下一个问题可用，重定向到下一个问题
            return redirect('take_quiz', question_id=next_question.pk)

    return render(request, 'quiz_app/quiz_already_answered.html')

@login_required
def take_quiz(request, question_id):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    question = Question.objects.get(pk=question_id)

    try:
        user_quiz = UserQuiz.objects.get(user=user, question=question)
    except UserQuiz.DoesNotExist:
        user_quiz = UserQuiz(user=user, question=question)

    form = AnswerForm()

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data['user_answer']
            if user_answer == question.correct_option:
                user_profile.cp += 1
                user_profile.save()

                user_quiz.user_answer = user_answer
                user_quiz.save()

                # 检查下一个未回答的问题
                unanswered_questions = Question.objects.exclude(
                    userquiz__user=user, userquiz__user_answer__isnull=False)
                next_question = unanswered_questions.first()

                if next_question:
                    # 重定向到下一个问题，并将question_id作为查询参数传递
                    return redirect('take_quiz', question_id=next_question.pk)
                else:
                    # 如果没有下一个问题，重定向到quiz_already_answered视图
                    return redirect('quiz_already_answered')

    return render(request, 'quiz_app/quiz_question.html', {
        'question': question,
        'form': form,
        'user_quiz': user_quiz
    })