from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Referer


def category(request):
    return render(request, 'ref_pages/category.html')


def support(request):
    contact_list = Referer.objects.all()
    paginator = Paginator(contact_list, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'ref_pages/index.html', {'contacts': contacts})
