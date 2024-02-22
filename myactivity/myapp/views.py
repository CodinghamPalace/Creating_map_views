from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from django.http import HttpResponse

def vision(request):
    content = """
    <h1>UNIVERSITY VISION</h1>
    <p>
    In 2030, the Manuel S. Enverga University Foundation is a globally competitive university with high concentrations of talent, excellent teaching environment, rigorous program quality, sufficient resources, and a culture of collaboration.
    </p>
    """
    return HttpResponse(content)

def mission(request):
    content = """
    <h1>UNIVERSITY MISSION</h1>
    <p>
    The Manuel S. Enverga University Foundation is a private, non-stock, non-profit, non-sectarian educational foundation with a three-fold function – instruction, research and community service – offering responsive and alternative programs supportive of national development goals and standards of global excellence.
    </p>
    """
    return HttpResponse(content)

def objectives(request):
    content = """
    <h1>Objectives</h1>
    <p>
    The University Libraries recognize their roles as instruments of teaching, research and extension in the academe. The organization of all materials and resources, the facilities provided, selection, training, and management of the staff, are all geared toward the fulfillment of these roles.
    </p>
    <p>
    The general objective of the University Libraries System is to gather, organize and service a collection of library materials print and non-print, book and non-book in support of the University’s educational programs.
    </p>
    """
    return HttpResponse(content)