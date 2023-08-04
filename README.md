<!-- English -->


# DjangoBlog
this is an RTL Blog web application developed with the Django Framework as BackEnd.

<br>
 
## Installation Guide:  
first of all clone the project in your machine, then go to the project directory.  

<br>

### Environment variables:
to config the environment variables, just copy the `.env-sample` to the `.env` file
then edit the `.env` file with your personal config.
```bash
cp .env-sample .env
``` 

<br>

### Install and Run :
this project has been dockerized which means it is very easy to deploy and run. you just have to install the `docker` and `docker-compose` in your machine then run the following command :
```bash
docker-compose up --build
```

if you don't want to see the logs or you want to close the terminal window, run it in detached mode with the `-d` option as follows:
```bash
docker-compose up -d --build
```

<br>

## TODO:
 - [ ] Create multiple settings for different environments
 - [ ] Add users management in the admin panel
 - [ ] Make the category ordering system easy and automatic
 - [ ] Make the weblog two languages (en/fa)
 - [ ] Create a notification system on the website


<!-- Divider-->
<br><hr><br>

<!-- Persian -->
<div dir="rtl" style="text-align:right; decoration:rtl;">
	
# وبلاگ جنگو
این یک وبلاگ RTL است که با فریمورک Django به عنوان فریمورک Back-End توسعه داده شده است.

<br>
	
## راهنمای نصب :  
در ابتدا ریپوزیتوری را در کامپیوتر خود clone کنید ، سپس به پوشه ی پروژه بروید.  

<br>

### متغیر های محیطی (Environment variables) :
برای تنظیم کردن متغیر های محیطی ، فایل `env-sample.` را در `env.` کپی کنید.
سپس فایل `env.` را ویرایش کنید و تنظیمات شخصی خود را قرار دهید.
```bash
cp .env-sample .env
``` 

<br>

### نصب و اجرا :
این پروژه داکرایز شده است از این رو برای نصب و اجرا کافی است برنامه `docker` ‍‍و `docker-compose` را در کامپیوتر خود نصب کنید و سپس دستور زیر را وارد کنید.
```bash
docker-compose up --build
```
اگر نمی خواهید لاگ های برنامه را ببینید یا می خواهید پنجره ترمینال خود را ببندید ، آن را در حالت detached مطابق زیر اجرا کنید :
```bash
docker-compose up -d --build
```


</div>



	


