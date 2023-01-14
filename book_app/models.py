from django.db import models
from datetime import datetime,timedelta
import uuid

class Students(models.Model):
    roll_number = models.CharField(max_length=100,unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    Guardian_name=models.CharField(max_length=100,help_text="Người giám hộ/phụ huynh sinh viên")
    Email=models.EmailField(max_length=100,help_text="Email người giám hộ/phụ huynh")
    def __str__(self):
        return self.fullname

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_pages = models.PositiveIntegerField()
    summary=models.TextField(max_length=500, help_text="Tóm tắt về cuốn sách",null=True,blank=True)
    def __str__(self):
        return self.book_title

class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Đặt id duy nhất trên Thư viện")
    book=models.ForeignKey('Book', on_delete=models.CASCADE,null=True)
    book_number=models.PositiveIntegerField(null=True,help_text="Số sách của sách thuộc loại tiết kiệm")
    Is_borrowed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id} {self.book}"

def get_returndate():
    return datetime.today() + timedelta(days=8)

class Book_Issue(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    book_instance = models.ForeignKey('BookInstance', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True,help_text="Ngày mượn")
    due_date = models.DateTimeField(default=get_returndate(),help_text="Ngày đến hạn trả")
    date_returned=models.DateField(null=True, blank=True,help_text="Ngày sách được trả lại")
    remarks_on_issue = models.CharField(max_length=100, default="Sách ở tình trạng tốt", help_text="Nhận xét/tình trạng sách khi mượn")
    remarks_on_return = models.CharField(max_length=100, default="Sách ở tình trạng tốt", help_text="Nhận xét/tình trạng sách khi trả")

    def __str__(self):
        return self.student.fullname + " borrowed " + self.book.book_title