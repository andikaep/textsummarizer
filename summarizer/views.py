from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import pipeline
import json

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@csrf_exempt
def index(request):
    return render(request, 'summarizer/index.html')

@csrf_exempt
def summarize(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            text = data.get("text", "")
            if not text:
                return JsonResponse({"error": "No text provided"}, status=400)

            summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
            return JsonResponse({"summary": summary[0]['summary_text']})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except KeyError:
            return JsonResponse({"error": "Missing 'text' key"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)
