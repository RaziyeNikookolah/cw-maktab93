from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def result(request):
    result_ = 0
    operator = request.GET['operator']
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    print(num1, num2, operator)
    if operator == "add":
        result_ = num1 + num2
    elif operator == "subtract":
        result_ = num1 - num2
    elif operator == "multiply":
        result_ = num1 * num2
    elif operator == "divide":
        if num2 != 0:
            result_ = num1 / num2
    return render(request, 'result.html', {"result": result_})
