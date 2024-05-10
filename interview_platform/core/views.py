from django.shortcuts import render, redirect
from .form import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .interview_bot import InterviewBot
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST

# Home page view
def home_view(request):
    return render(request, 'core/home.html')

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have been logged in successfully.')
            return redirect('interview')  # Consider if redirect should be to a different page
        else:
            messages.error(request, 'Login failed. Please try again.')
    form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def interview_get_view(request):
    if 'new_interview' in request.GET:
        request.session['chat_history'] = []
        request.session.modified = True

    return render(request, 'core/interview.html') 

# API View for the interview bot
@login_required
@require_POST  # Ensure that this view only accepts POST requests

def interview_api_view(request):
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    bot = InterviewBot()
    bot.chat_history = request.session['chat_history']

    user_input = request.POST.get('user_input', '')
    if user_input:
        print("Chat History Before Response:", request.session['chat_history'])

        response = bot.get_response(user_input)
        request.session['chat_history'].append({'role': 'user', 'content': user_input})
        request.session['chat_history'].append({'role': 'system', 'content': response})
        request.session.modified = True  

        # Debugging: Log the response
        #print("Bot Response:", response)

        #response = bot.get_response(user_input)
        #request.session['chat_history'] = bot.chat_history
        #request.session.modified = True 

        # Debugging: Log the updated chat history
        # print("Chat History After Response:", request.session['chat_history'])


        return JsonResponse({'response': response})

    return JsonResponse({'response': "No input received"}, status=400)