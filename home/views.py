from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def home(request):
    return render(request, "index.html")


import os
import openai

openai.api_key = "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"


def chatapi(request):
    if request.method == "POST":
        prompt = request.POST["prompt"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        print(response)
        return JsonResponse(response)
    else:
        return HttpResponse(" Bad request !!")
