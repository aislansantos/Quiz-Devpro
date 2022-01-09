from django.shortcuts import render, redirect

# Create your views here.
from quiz.base.forms import AlunoForm
from quiz.base.models import Pergunta, Aluno


def home(request):  # como funciona a requisução/request ?
    if request.method == "POST":
        #usuario ja existe
        email = request.POST['email']
        try:
            aluno = Aluno.objects.get(email=email)
        except Aluno.DoesNotExist:
            #usuario não existe
            formulario = AlunoForm(request.POST)
            if formulario.is_valid():
                aluno = formulario.save()
                return redirect('/perguntas/1')
            else:
                contexto = {'formulario': formulario}
                return render(request, 'base/home.html', contexto)
        else:
            request.session['aluno_id'] = aluno.id
            return redirect('/perguntas/1')
    return render(request, 'base/home.html')


def classificacao(request):
    return render(request, 'base/classificacao.html')


def perguntas(request, indice):
    try:
        aluno_id = request.session['aluno_id']
    except KeyError:
        return redirect('/')
    else:
        pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
        context = {'indice_da_questao': indice, 'pergunta': pergunta} #o que é o contexto ?
        return render(request, 'base/game.html', context=context)
