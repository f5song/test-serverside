# Django Test

1. สร้าง `virtual environment`
    
    ```powershell
    #Create
    py -m venv myvenv
    
    #Activate
    myvenv\Scripts\activate.bat
    ```
    
2. ติดตั้ง `django` และ `psycopg2` libraries
    
    ```powershell
    # Install Django
    pip install django
    
    pip install psycopg2
    ```
    
3. สร้างโปรเจคใหม่ใหม่ชื่อ`myshop`
    
    ```powershell
    django-admin startproject myshop
    ```
    
4. จากนั้นให้ทำการ startapp ใหม่ชื่อ `shop`
    
    ```powershell
    python manage.py startapp shop
    ```
    
5. สร้าง database ชื่อ `shop` ใน Postgres DB
6. ทำการเพิ่ม code model ในไฟล์ `shop/models.py`
7. สร้าง DB ใน postgres  สร้าง DB ชื่อ "shop"
8. เพิ่ม **'shop'** ใน `settings.py`
    
    ```python
    # Database setting
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "shop",
            "USER": "postgres",
            "PASSWORD": "1234",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
    # Add app blogs to INSTALLED_APPS
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    
        # "django_extensions",
        "shop",
    ]
    ```
    
9. ทำการ `makemigrations` และ `migrate`
    
    ```powershell
    python manage.py makemigrations
    python manage.py migrate
    ```
    
10. run คำสั่งในไฟล์ `shop.sql` ใน PgAdmin4
11. ติดตั้ง `django-extensions` และ `jupyter notebook` ด้วยคำสั่ง
    
    ```
    pip install django-extensions ipython jupyter notebook
    ```
    
12. จากนั้นให้แก้ไข version ของ package ภายใน jupyter และ notebook
    
    ```
    pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2
    ```
    
    แก้ไข version notebook
    
    ```
    pip install notebook==6.5.7
    ```
    
    หากติดตั้ง หรือ run jupyter ไม่ได้ให้ลองเปลี่ยน notebook version ดังนี้ `6.5.6`
    
13. จากนั้นสร้าง directory ชื่อ `notebooks`
    
    ```
    mkdir notebooks
    ```
    
14. เพิ่ม `django-extensions` ใน INSTALLED_APPS ในไฟล์ settings.py
    
    ```python
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    
        "django_extensions",
        "shop",
    ]
    ```
    
15. ทำการ start Jupyter Notebook server ด้วย command
    
    ```
    python manage.py shell_plus --notebook
    ```
    
16. จากนั้นใน Cell แรกของไฟล์ Notebook เพิ่ม code นี้ลงไป

```
import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
```