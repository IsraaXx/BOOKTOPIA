from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('', views.login, name='login'),
   path('home/', views.home_page, name='home_page'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('scientific-books/', views.scientific_books, name='scientific_books'),
    path('personal-development-books/', views.personal_development_books, name='personal_development_books'),
    path('historic-books/', views.historic_books, name='historic_books'),
    path('children-books/', views.children_books, name='children_books'),
    path('detective-books/', views.detective_books, name='detective_books'),
    path('Programming-books/', views.Programming_books, name='Programming_books'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    #path('login/', views.login, name='login'),
    
    path('search/', views.search_books, name='search_books'),
    #path('',views.index,name='indx') ,
    path('register/',views.register,name='register') ,
    path('Login/',views.login,name='login') ,
    path('home/',views.userProfile,name='home') ,
    path('profile/', views.userProfile, name='userProfile'),
    path('Profile/', views.adminProfile, name='adminProfile'),
    path('Myprofile/' , views.myprof , name='Myprofile'),
    path('addbook/', views.addbook, name='addbook'),
    path('adminlist/<int:book_id>/', views.adminlist, name='adminlist'), 
    path('editbook/', views.editbook, name='editbook'), 
    path('update_book/<book_id>', views.update_book, name='update-book'),
    path('Deletebook/', views.Deletebook, name='Deletebook'),
    path('Delete_event/<int:book_id>/', views.Delete_event, name='Delete_event'),
    path('borrowed_books_list.html/', views.borrowed_books_list, name='borrowedbooklist'),
    path('your-django-view/<int:book_id>/',views.your_django_view , name = "your_django_view"),
    path('delete/<int:book_id>/',views.delete , name = "delete"),
    path('DELETE/<int:book_id>/',views.DELETE, name = "DELETE"),

]
