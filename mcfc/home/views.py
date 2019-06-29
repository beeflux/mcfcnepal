from django.shortcuts import render
from member.models import Members, AdminMember
# Create your views here.
def homepage(request):
    members = AdminMember.objects.all()[0:4]
    return render(request, 'home/base.html',{'active':'home','members':members})