from django.shortcuts import render
import openai
openai.api_key = "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"
        
# Create your views here.
def index(request):
    if request.method == 'POST':
        input = request.POST['input']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = input,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            ) 
        answer = response.choices[0].text  
        context = {
            'answer': answer,
            'input': input
        }
        return render(request,'index.html',context)
    return render(request,'index.html')