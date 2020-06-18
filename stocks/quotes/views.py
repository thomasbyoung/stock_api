from django.shortcuts import render

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        try:
            api = json.loads(api_request.content)
        except Exception as e: 
            api = "Error..."
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Please enter a ticker."})

def about(request):
    return render(request, 'about.html', {})