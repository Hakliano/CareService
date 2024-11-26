from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Partner, Review, Post, City, Region, Category
from .forms import PartnerForm, ReviewForm, UserRegisterForm
from django.contrib import messages
from django.db.models import Q


def index(request):
    partners = Partner.objects.all()
    return render(request, "index.html", {'partners': partners})


def partner_list(request):
    partners = Partner.objects.all()
    review_form = ReviewForm()
    return render(request, 'partner_list.html', {'partners': partners, 'review_form': review_form})


def rate_partner(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.partner = partner
            review.customer = request.user
            review.save()
            messages.success(request, 'Your review has been added successfully.')
            return redirect('partner_list')
    else:
        form = ReviewForm()
    return render(request, 'rate_partner.html', {'form': form, 'partner': partner})


def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New partner has been added successfully.')
            return redirect('partner_list')
    else:
        form = PartnerForm()
    return render(request, 'add_partner.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, {username}! You can now log in.')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def cards(request):
    return render(request, 'cards.html')


def get_cities_for_region(request):
    region_id = request.GET.get('region_id')
    cities = City.objects.filter(region_id=region_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)


def filter_partners(request):
    categories = Category.objects.all()
    regions = Region.objects.all()

    selected_category = request.GET.get('category')
    selected_region = request.GET.get('region')
    selected_city = request.GET.get('city')

    partners = Partner.objects.all()

    if selected_category:
        try:
            selected_category_obj = Category.objects.get(id=selected_category)
            partners = partners.filter(category=selected_category_obj)
        except Category.DoesNotExist:
            partners = partners.none()

    if selected_region:
        cities_in_region = City.objects.filter(region_id=selected_region)
        partners = partners.filter(city__in=cities_in_region)

    if selected_city:
        partners = partners.filter(city__id=selected_city)

    return render(request, 'reality.html', {
        'partners': partners,
        'categories': categories,
        'regions': regions,
        'selected_category': selected_category,
        'selected_region': selected_region,
        'selected_city': selected_city,
    })


def partner_detail(request, partner_id):
    """Detail konkrétního partnera."""
    partner = get_object_or_404(Partner, id=partner_id)
    return render(request, 'partner_detail.html', {'partner': partner})


def partners_by_category_and_city(request):
    """Filtrovaní partnerů podle kategorie a města."""
    category_id = request.GET.get('category')  # ID kategorie z URL
    city_id = request.GET.get('city')  # ID města z URL

    partners = Partner.objects.all()

    if category_id:
        partners = partners.filter(category_id=category_id)

    if city_id:
        partners = partners.filter(city_id=city_id)

    categories = Category.objects.all()
    cities = City.objects.all()

    return render(request, 'partner_list.html', {
        'partners': partners,
        'categories': categories,
        'cities': cities,
        'selected_category': category_id,
        'selected_city': city_id,
    })
