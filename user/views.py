from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST  # Ensures the view only responds to POST requests
def register_user(request):
    username = request.POST.get("uname")
    password = request.POST.get("pword")
    
    # Log data for debugging
    print("Username:", username)
    print("Password:", password)
    
    # Respond with a simple JSON message to confirm connection
    return JsonResponse({"success": True, "message": "Data received successfully!"})

def login_user(request):
    username = request.POST.get("uname")
    password = request.POST.get("pword")
    
    # Log data for debugging
    print("Username:", username)
    print("Password:", password)
    
    # Respond with a simple JSON message to confirm connection
    return JsonResponse({"success": True, "message": "Data received successfully!"})