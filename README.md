# หลักการทำงานของ MYWEBAPPMODEL

## 📕1. [DjangoApp](https://github.com/Lynnn01/MyWebappModel/tree/main/DjangoApp)

```shell
django-admin startproject [ชื่อ Project]
```
**🔺 main folder ของ project โดยใช้คำสั่งดังกล่าวในการสร้าง project**

## 📕2. [env](https://github.com/Lynnn01/MyWebappModel/tree/main/env)

```shell
pyton -m vene env
```

**🔺การจำลอง environment เพื่อใช้ในการทำงานภายใน project**

## 📕3. [requirments.txt](https://github.com/Lynnn01/MyWebappModel/blob/main/requirments.txt)

```text
django >= 3
```
**🔺 การควบคุม Version ในการติดตั้ง django ภายใน environment โดยการใช้คำสั่งในการติดตั้ง ดังนี้**

```shell
pip install -r requirments.txt
```

## 📕4. [MainApp](https://github.com/Lynnn01/MyWebappModel/tree/main/MainApp)

```shell
python manage.py startapp [ชื่อ Projectapp]
```
**🔺 สร้าง sub-folder ในการสร้าง ProjectApp ภายใน DjangoApp**

## 📕5. [template](https://github.com/Lynnn01/MyWebappModel/tree/main/templates)
**🔻 เป็น folder สำหรับการกำหนดลักษณะของแต่ละ pages โดยจะมีการเรียกใช้จาก [views.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/views.py)**

```python
from  django.shortcuts  import  render

def  Home (request):

	return  render(request,"index.html")

def  About(request):

	return  render (request,"about.html")

def  Contact(request):

	return  render (request,"contact.html")
```

**🔻 และ  [views.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/views.py) จะถูกเรียกใช้โดย [urls.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/urls.py) เพื่อเป็นการ set url สำหรับแต่ละ page**

```python
from  django.urls  import  path
from . import  views

urlpatterns  = [

	path('',views.Home, name='home'),

	path('about',views.About, name='about'),

	path('contact',views.Contact, name='contact'),

]
```
## 📕6. [model.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/models.py)

```python
from  django.db  import  models

prefix_choices  = (

(1, "นาย"),

(2, "นางสาว"),

(3, "นาง"),

)

class  Student(models.Model):

	std_id  =  models.IntegerField()

	prefix  =  models.IntegerField(choices=prefix_choices, default=1)

	name  =  models.CharField(max_length=255)

	lastname  =  models.CharField(max_length=255)

	phone  =  models.CharField(max_length=15)

	address  =  models.TextField()


	class  Meta:

	verbose_name  =  "Student"

	verbose_name_plural  =  "Students"


	def  __str__(self):

	return  self.name


	def  get_absolute_url(self):

	return  reversed("Student_detail", kwargs={"pk": self.pk})
```

**🔺 การสร้างตารางสำหรับการเก็บข้อมูลบนพื้นฐานของ db.sqlite3**
## 📕7. [admin.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/admin.py)

```python
from django.contrib import admin

from .models import Student

@admin.register(Student)
class Admin(admin.ModelAdmin):
	list_display = ("std_id", "prefix", "name", "lastname", "phone")
	search_fields = ("std_id", "name", "lastname", "phone")
```
**🔺 การแสดงตารางข้อมูลใน admin โดยมีการแสดงแบบแถว และมีการค้นหา**

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

**🔺 ใช้คำสั่ง makemigrations และ migrate เพื่อสร้างข้อมูล แล้วจึงใช้คำสั่ง  createsuperuser เพื่อสร้าง admin user ในการเข้าถึงฐานข้อมูล**
## 📕8. การสั่ง Run server
![enter image description here](https://cdn.discordapp.com/attachments/1026853768505081868/1136316668583362671/2023-08-02_221604.png)

```shell
python manage.py runserver
```

**🔺 สั่ง run server เพื่อใช้งาน**

![enter image description here](https://cdn.discordapp.com/attachments/1026853768505081868/1136315785229373550/2023-08-02_221228.png)

```text
http://127.0.0.1:8000/admin/
```

**🔺 การเข้าถึง admin และใช้การ login ตาม createsuperuser ที่เราสร้างไว้**

![enter image description here](https://cdn.discordapp.com/attachments/1026853768505081868/1136316700049023137/2023-08-02_221516.png)
**🔺 ตารางสำหรับการเก็บข้อมูลบนพื้นฐานของ db.sqlite3**

![enter image description here](https://cdn.discordapp.com/attachments/1026853768505081868/1136316685234753627/2023-08-02_221547.png)
**🔺 การแสดงแบบแถว และการค้นหา**

## 💾 CREDIT
[💻 YOUTUBE :   Phisan Sookkhee](https://www.youtube.com/watch?v=EC6k9KduQYU&list=PLUD6z42fSjQq785dtC6bl9BTSlO-_EjY9)
