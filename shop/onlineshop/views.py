from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from .models import Product

from cart.forms import CartAddProductForm


class MainPage(ListView):
    model = Product
    template_name = "main_page.html"
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(available=True)


class ProductsByCategory(ListView):
    model = Product
    template_name = "main_page.html"

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True)


class ViewProduct(FormMixin, DetailView):
    model = Product
    form_class = CartAddProductForm
    template_name = "view_product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super(ViewProduct, self).get_context_data(**kwargs)
        context["form"] = CartAddProductForm(initial={'post': self.object})
        return context

    def quantity(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ViewProduct, self).form_valid(form)

