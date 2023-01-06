"""book_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from book_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new_student', views.add_new_student, name='new_student'),
    path('add_new_book', views.add_new_book, name='new_book'),
    path('add_book_issue', views.add_book_issue, name='book_issue'),
    path('add_new_book_instance', views.add_new_book_instance, name='add_new_book_instance'),
    path('show_students', views.view_students, name='show_student_record'),
    path('view_books', views.view_books, name='show_book_record'),
    path('view_books_issued', views.view_bissue, name='show_issue_record'),
    path('edit/student/<str:roll>',views.edit_student_data,name="Edit Student data"),
    path('edit/book/<uuid:id>',views.edit_book_data,name="Edit Student data"),
    path('delete/student/<str:roll>',views.delete_student,name="Delete Student data"),
    path('delete/book/<str:id>',views.delete_book,name="Delete book data"),
    path('return_book/<int:id>',views.return_issued_book,name="return_issued_book"),
    path('edit_issued/<int:id>',views.edit_issued,name="edit_issued"),
]
