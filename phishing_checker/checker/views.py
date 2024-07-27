

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import get_phishing_status

@csrf_exempt
def check_url(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data.get('url', '')
        result = get_phishing_status(url)
        # Convert result to a Python int
        return JsonResponse({'result': int(result)})
    return JsonResponse({'error': 'Invalid request'}, status=400)
