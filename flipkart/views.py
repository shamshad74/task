import datetime
import time
from django import forms
from django.utils import timezone
from .models import Product,Category
from django.http import JsonResponse
from django.views import generic

class IndexView(generic.Listview):
    template_name='flipkart/index.html'
    context_object_name='product_list'

    def get_queryset(self):
        return Product.objects.all()
    


def scrape_product(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("span", {"class": "_35KyD6"}).text
    description = soup.find("div", {"class": "_3WHvuP"}).text
    price = float(soup.find("div", {"class": "_30jeq3U"}).text[1:].replace(',', ''))

    try:
        size = soup.find("div", {"class": "_2kHMtA"}).text
    except:
        size = None

    try:
        mobile_number = soup.find("div", {"class": "_3m3Yyu"}).text
    except:
        mobile_number = None

    product, created = Product.objects.update_or_create(url=url, defaults={'title': title, 'description': description, 'price': price, 'size': size, 'mobile_number': mobile_number, 'scraped_at': timezone.now()})
    return product

def scrape_view(request):
    url = request.GET.get('url')
    product = Product.objects.filter(url=url).first()
    if product is None or (timezone.now() - product.scraped_at).days >= 7:
        product = scrape_product(url)
    else:
        time.sleep(1)
        scrape_product(url)
    return render(request, 'scraped_data.html', {'product': product})

class CategoryForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="All Categories", required=False)

def list_view(request):
    form = CategoryForm(request.GET or None)
    if form.is_valid():
        category = form.cleaned_data['category']
        products = Product.objects.filter(category=category) if category else Product.objects.all()
    else:
        products = Product.objects.none()

    return render(request, 'list.html', {'form': form, 'products': products})


class URLForm(forms.Form):
    url = forms.URLField()

def fetch_view(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': form.errors})
    else:
        form = URLForm()
        return render(request, 'fetch.html', {'form': form})
