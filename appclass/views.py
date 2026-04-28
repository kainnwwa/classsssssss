from django.shortcuts import render
from django.views import View

class MyFormView(View):
    def get(self, request):
        return render(request, 'main.html')
    
    def post(self, request):
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operation = request.POST.get('operation')
        
        result = None
        error = None
        
        if num1 and num2 and operation:
            try:
                a = float(num1)
                b = float(num2)
                
                if operation == '+':
                    result = a + b
                elif operation == '-':
                    result = a - b
                elif operation == '*':
                    result = a * b
                elif operation == '/':
                    if b == 0:
                        error = 'На ноль делить нельзя!'
                    else:
                        result = a / b
                else:
                    error = 'Неверное действие'
                    
            except ValueError:
                error = 'Введите числа!'
        else:
            error = 'Заполните все поля'
        
        return render(request, 'main.html', {'result': result, 'error': error})