import google.generativeai as genai
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Suggestion
from decouple import config
from django.shortcuts import render, redirect
from urllib.parse import urlencode 
from django.views import View

genai.configure(api_key=config("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def index(request):
    return render(request, 'index.html')

class SuggestCareerView(View):
    def post(self, request):
        data = request.POST

        # Convert multi-select values to list
        skills = request.POST.getlist('skills')
        interests = request.POST.getlist('interests')
        goals = data['goals']

        prompt = f"""
        Suggest 3 careers for someone with:
        Skills: {skills}
        Interests: {interests}
        Goals: {goals}
        Give brief reasons too.
        """

        response = model.generate_content(prompt)
        result = response.text

        # Save to DB
        suggestion = Suggestion(
            name=data['name'],
            age=data['age'],
            skills=skills,
            interests=interests,
            goals=goals,
            suggested_careers=[],  # optional
            reasoning=result
        )
        suggestion.save()

        # Save result in session instead of query params
        request.session['suggestions'] = result
        return redirect('/career-results/')

# View for rendering the results page
def career_results(request):
    suggestions = request.session.get('suggestions', '')
    return render(request, 'career_results.html', {'suggestions': suggestions})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # For now, just show success message. You can log or save the data if needed.
        print("Contact form received:", name, email, message)

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')