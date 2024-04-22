from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == 'GET':
        return render(request, "cadastro.html")
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            return redirect('/usuarios/cadastro')
        
        user = User.objects.filter(username = username)
        if user.exists():
            return redirect('/usuarios/cadastro')

        try:
            User.objects.create_user(
                username = username,
                password = confirmar_senha
            )
            return redirect('/usuarios/login')
        except:
            return redirect('/usuarios/cadastro')

        return HttpResponse('<h2>Deu certo</h2>')

