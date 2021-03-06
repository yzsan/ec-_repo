from django.views.generic import TemplateView, ListView, DetailView
from .models import Product


class Home(TemplateView):
    template_name = 'mamazon/home.html'


class ProductListView(ListView):
    model = Product
    template_name = "mamazon/list.html"

    def get_queryset(self):
        queryset = Product.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            queryset = queryset.filter(name__contains=qs)
        # get_querysetのスニペットで表示された２行と return queryset
        # queryset = super(CLASS_NAME, self).get_queryset()
        # queryset = queryset # TODO
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = "mamazon/detail.html"
