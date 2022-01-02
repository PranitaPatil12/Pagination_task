from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import InstituteModelForm
from .models import Institute
from django.views import View
from django.core.paginator import Paginator




class AddInstituteView(View):
    def get(self,request):
        form = InstituteModelForm()
        template_name = 'InstituteApp/addinstitute.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request):
        form = InstituteModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("show_list")
        template_name = 'InstituteApp/addinstitute.html'
        context = {'form': form}
        return render(request, template_name, context)

class InstituteListView(View):
    def get(self,request):
        institute_list = Institute.objects.all()
        paginator = Paginator(institute_list, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        template_name = 'InstituteApp/show_institute.html'
        context = {'page_obj':page_obj}
        return render(request, template_name, context)

class UpdateView(View):
    def get(self,request,i):
        inst = Institute.objects.get(id=i)
        form = InstituteModelForm(instance=inst)
        template_name = 'InstituteApp/addinstitute.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request,i):
        inst= Institute.objects.get(id=i)
        form = InstituteModelForm(request.POST,instance=inst)
        if form.is_valid():
            form.save()
            return redirect("details")
        template_name = 'InstituteApp/addinstitute.html'
        context = {'form': form}
        return render(request, template_name, context)

class DeleteView(View):

    def post(self,request,i):
        inst = Institute.objects.get(id=i)
        inst.delete()
        return redirect("show_list")
