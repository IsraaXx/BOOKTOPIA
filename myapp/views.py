from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import BookDetails , BorrowedBook
from django.http import JsonResponse
from .forms import bookform
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.templatetags.static import static

from .models import register3
from django.contrib.auth import authenticate, login
from .models import *


# Create your views here.

borrowed_dict = {}

def home(request):
    return HttpResponse("Hello")


def book_list(request):
    books = BookDetails.objects.all()
    user_type = request.session.get('type')  # Get user type from session
    if user_type:
       return render(request, 'book_list.html', {'books': books,'user_type': user_type})


def book_detail(request, book_id):
    book = get_object_or_404(BookDetails, pk=book_id)
    user_type = request.session.get('type')  # Get user type from session
    if user_type:
       return render(request, 'book_detail.html', {'book': book,'user_type': user_type})


def home_page(request):
    user_type = request.session.get('type')  # Get user type from session
    print(user_type)
    book = BookDetails.objects.all()
    books = BookDetails.objects.order_by('-no_of_borrow')
    for x in books :
        print(x.title)
    if user_type:
        return render(request, 'Home-page.html', {'book' : book , 'books' : books ,'user_type' : user_type})


def scientific_books(request):
    scientific_books = BookDetails.objects.filter(category='Scientific')
    user_type = request.session.get('type')  # Get user type from session
    if user_type:
       return render(request, 'Scientific-books.html', {'scientific_books': scientific_books,'user_type': user_type})


def personal_development_books(request):
    personal_development_books = BookDetails.objects.filter(category='Personal Development')
    user_type = request.session.get('type')  # Get user type from session
    if user_type:
       return render(request, 'Personal_development.html', {'personal_development_books': personal_development_books,'user_type': user_type})


def historic_books(request):
    historic_books = BookDetails.objects.filter(category='Historic')
    user_type = request.session.get('type')  # Get user type from session
    if user_type:
      return render(request, 'Historic-Books.html', {'historic_books': historic_books,'user_type': user_type})


def children_books(request):
    children_books = BookDetails.objects.filter(category='Children')
    user_type = request.session.get('type')  # Get user type from session
    if user_type:
       return render(request, 'Children-Books.html', {'children_books': children_books,'user_type': user_type})


def detective_books(request):
    detective_books = BookDetails.objects.filter(category='Detective')
    user_type = request.session.get('type')  # Get user type from session
    if user_type:
      return render(request, 'Detective-Books.html', {'detective_books': detective_books,'user_type': user_type})

def Programming_books(request):
    Programming_books = BookDetails.objects.filter(category='Programming')
    user_type = request.session.get('type')  # Get user type from session
    if user_type:
      return render(request, 'Programming-Books.html', {'Programming_books': Programming_books,'user_type': user_type})
  
def about_us(request):
    user_type = request.session.get('type')  # Get user type from session
    if user_type:
       return render(request, 'about-us.html',{'user_type': user_type})


def contact_us(request):
    user_type = request.session.get('type')  # Get user type from session
    if user_type:
        return render(request, 'contact-us.html',{'user_type': user_type})


def search_books(request):
    if request.method == 'GET':
        query = request.GET.get('search', '')
        books = BookDetails.objects.filter(title__icontains=query) | BookDetails.objects.filter(
            author__icontains=query) | BookDetails.objects.filter(category__icontains=query)
        books_data = [{
            'name': book.title,
            'author': book.author,
            'category': book.category,
            'image': book.image_url.url,
            'page': reverse('book_detail', args=[book.id])
        } for book in books]
        return JsonResponse(books_data, safe=False)


def register(request):
    # Only proceed if this is a POST request
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        type = request.POST.get('type')
        # Check if any of the required fields are missing
        if not all([username, email, password, password2, type]):
            return HttpResponse('All fields are required.', status=400)
        # Check if passwords match
        if password != password2:
            return HttpResponse('Passwords do not match.', status=400)
        try:
            data = register3(username=username, email=email, password=password, password2=password2, type=type)
            data.save()
            return redirect('login')
        except Exception as e:
            return HttpResponse('An error occurred: {e}', status=500)

    # If it's not a POST request, just render the registration page
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if both username and password are provided
        if not username or not password:
            messages.error(request, 'Both username and password are required.')
            return redirect('login')
        # Try to retrieve the user from the register3 table
        try:
            registered_user = register3.objects.get(username=username)
            if password == registered_user.password:
                request.session['user_id'] = registered_user.id
                request.session['name'] = registered_user.username
                request.session['email'] = registered_user.email
                request.session['type'] = registered_user.type
                if registered_user.type == 'user':
                    return redirect('userProfile')
                if registered_user.type == 'admin':
                    return redirect('adminProfile')
            else:
                # If the password is incorrect, return an error
                messages.error(request, 'Your username or password is incorrect.')
                return redirect('login')
        except register3.DoesNotExist:
            # If the user does not exist in register3 table, return an error
            messages.error(request, 'User does not exist in the register.')
            return redirect('login')
    # If it's not a POST request, just render the login page
    return render(request, 'Login.html')


def userProfile(request):
    name = request.session.get('name')
    email = request.session.get('email')
    return render(request, 'userProfile.html', {'name': name, 'email': email})


def adminProfile(request):
    name = request.session.get('name')
    email = request.session.get('email')
    return render(request, 'Admin-Profile.html', {'name': name, 'email': email})


def myprof(request):
     name = request.session.get('name')
     email = request.session.get('email')
     type = request.session.get('type')
     if type == "user":
         return render(request, 'userProfile.html', {'name': name, 'email': email})
     elif type == "admin":
         return render(request, 'Admin-Profile.html', {'name': name, 'email': email})


def addbook(request):
    submitted = False
    if request.method == "POST":
        form = bookform(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books?submitted=True')
    else:
        form = bookform
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add-book.html', {'form': form, 'submitted': submitted})


def adminlist(request, book_id):
    book = BookDetails.objects.get(pk=book_id)
    return render(request, 'adminlist.html', {'books': book})


def editbook(request):
    books = BookDetails.objects.all()
    return render(request, 'adminlist.html', {'books': books})


def update_book(request, book_id):
    book = BookDetails.objects.get(pk=book_id)
    form = bookform(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')

    return render(request, 'update_book.html', {'books': book, 'form': form})


def Deletebook(request):
    books = BookDetails.objects.all()
    return render(request, 'deletebook.html', {'books': books})


def Delete_event(request, book_id):
    try:
        book = BookDetails.objects.get(pk=book_id)
        book.delete()
        return redirect('book_list')
    except BookDetails.DoesNotExist:
        return HttpResponse("Book does not exist")

def DELETE(request, book_id):
    try:
        book = BookDetails.objects.get(pk=book_id)
        book.delete()
        return JsonResponse({'status': 'success', 'message': f'Book "{book.title}" is deleted'})
    except BookDetails.DoesNotExist:
        return JsonResponse({'status': 'success', 'message': f'Book "{book.title}" is not existed'})


def your_django_view(request, book_id):
    try:
        book = get_object_or_404(BookDetails, id=book_id)
        user_id = request.session.get('user_id')
        userID = get_object_or_404(register3, id = user_id)
        if book_id not in borrowed_dict :
          borrowed_dict[book_id] = set()
        borrowed_dict[book_id].add(user_id)
        book.no_of_borrow = len(borrowed_dict[book_id])
        book.save()
        if book.available:
            book.available = False
            book.btn = 'Unavailable'
            book.save()
            borrowbook = BorrowedBook(book=book , user = userID)
            borrowbook.save()
            return JsonResponse({'status': 'success', 'message': f'Book "{book.title}" is now unavailable'})
        else:
            return JsonResponse({'status': 'error', 'message': f'Book "{book.title}" is already unavailable'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


def borrowed_books_list(request):
    user_id = request.session.get('user_id')
    borrowed_books = BorrowedBook.objects.filter(user_id = user_id)
    return render(request, 'borrowed_books_list.html', {'borrowed_books': borrowed_books})

def delete(request, book_id):
    borrowed_book = get_object_or_404(BorrowedBook, id=book_id)  # Use 'id=book_id' to filter objects
    book = borrowed_book.book
    book.available = True
    book.btn = 'Borrow'
    book.save()
    borrowed_book.delete()  # Call delete() method with parentheses
    return JsonResponse({'status': 'success', 'message': f'Book "{book.title}" is now available'})