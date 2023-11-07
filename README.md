# Django_Blog - 소방 헬퍼: 생명을 지키는 정보 공유 블로그
소방 관련 업무를 하는 사람들끼리 업무 관련 꿀팁 및 소방 관련법 변동사항 같은 정보를 공유하는 블로그입니다.

## 1. 목표와 기능
### 1.1 목표
- 소방업무 종사자들끼리 관련 정보를 공유하는 커뮤니티
### 1.2 기능
- 분야별 종사자 들이 자신들의 업무 노하우에 관련해서 소통할 수 있도록 댓글 기능 구현
- 카테고리 및 태그 별로 게시글을 확인할 수 있는 기능 구현

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경
#### [FrontEnd]  
<div>
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white">
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
</div>

#### [BackEnd]
<div>
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
</div>

#### [Tool]
<div>
    <img src="https://img.shields.io/badge/visualstudio-007ACC?style=for-the-badge&logo=visualstudio&logoColor=white">
    <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</div>

### 2.2 배포 URL(AWS Lightsail)
http://15.165.255.207:8000/ <- 보류

## 3. 프로젝트 구조와 개발 일정

### 3.1 프로젝트 구조
📦@@231026-1107 2차 프로젝트(Django mini)  
 ┣ 📂.static_root  
 ┃ ┣ 📂admin  
 ┃ ┣ 📂css  
 ┃ ┣ 📂fonts  
 ┃ ┣ 📂images  
 ┃ ┣ 📂js  
 ┃ ┣ 📂scss  
 ┃ ┣ 📜about.html  
 ┃ ┣ 📜contact.html  
 ┃ ┣ 📜fashion.html  
 ┃ ┣ 📜index.html  
 ┃ ┣ 📜prepros-6.config  
 ┃ ┣ 📜single.html  
 ┃ ┗ 📜travel.html  
 ┣ 📂accounts  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜forms.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂blog  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜forms.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂firehelper  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜asgi.py  
 ┃ ┣ 📜settings.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜wsgi.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂main  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂media  
 ┃ ┣ 📂blog  
 ┃ ┗ 📂profile_pics  
 ┣ 📂static  
 ┃ ┣ 📂css  
 ┃ ┣ 📂fonts  
 ┃ ┣ 📂images  
 ┃ ┣ 📂js  
 ┃ ┣ 📂scss  
 ┃ ┣ 📜.DS_Store  
 ┃ ┣ 📜about.html  
 ┃ ┣ 📜contact.html  
 ┃ ┣ 📜fashion.html  
 ┃ ┣ 📜index.html  
 ┃ ┣ 📜prepros-6.config  
 ┃ ┣ 📜single.html  
 ┃ ┗ 📜travel.html  
 ┣ 📂templates  
 ┃ ┣ 📂accounts  
 ┃ ┃ ┣ 📜agreement.html  
 ┃ ┃ ┣ 📜change_password.html  
 ┃ ┃ ┣ 📜form.html  
 ┃ ┃ ┣ 📜profile.html  
 ┃ ┃ ┗ 📜profile_update.html  
 ┃ ┣ 📂blog  
 ┃ ┃ ┣ 📜category.html  
 ┃ ┃ ┣ 📜form.html  
 ┃ ┃ ┣ 📜posttag.html  
 ┃ ┃ ┣ 📜post_confirm_delete.html  
 ┃ ┃ ┣ 📜post_detail.html  
 ┃ ┃ ┗ 📜post_list.html  
 ┃ ┣ 📂main  
 ┃ ┃ ┣ 📜about.html  
 ┃ ┃ ┗ 📜index.html  
 ┃ ┣ 📜404.html  
 ┃ ┣ 📜base.html  
 ┃ ┗ 📜base_detail.html  
 ┣ 📂utils  
 ┃ ┣ 📂__pycache__  
 ┃ ┗ 📜context_processors.py  
 ┣ 📂venv  
 ┣ 📜.gitignore  
 ┣ 📜db.sqlite3  
 ┣ 📜manage.py  
 ┣ 📜README.md  
 ┣ 📜requirements.txt  
 ┗ 📜secrets.json  

### 3.2 URL 구조

||||  
|app:main|views명|templates|  
|'\'|index|main/index.html|  
|'about/'|about|main/about.html|  

### 3.3 개발 일정
<div align="center">
<img width="800" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/11ea9ce8-1f56-4421-af63-861caae0118e"><br>
- 타임라인 -<br>
<br>
<img width="800" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/b56bee4f-07e7-4aa5-b8e3-f5eb8ee28a9f"><br>
<img width="800" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/36cd9cd4-37f3-4c86-b0a3-db0c10084437"><br>
<img width="800" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/ba43a159-fb26-4147-96d2-b312ee47479e"><br>
- WBS -<br>
</div>

## 4. 데이터베이스 모델링(ERD)
<div align="center">
<img width="800" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/ee50c0b9-2cab-47a7-8c4d-3e6b0859084c"><br>
- 기능 요구사항(마인드맵) - <br>
<br>
<img width="800" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/ac898123-b17e-461b-9981-f8c677b6e229"><br>
- 데이터베이스 모델링(ERD 설계) - <br>
</div>

## 5. UI
### 5-1. 와이어프레임
- [Mockup 테스트 페이지](https://ovenapp.io/view/RLB4pSeIPvYpCHhRChBNKNLbPwiuccir/6psTJ)  
<img src="https://github.com/Alexmint001/Django_Blog/assets/142385654/630b1129-0f92-49d3-a034-028a899bf831" width="10%">  

|||
|-|-|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/d9d0cdc3-cb80-41a0-9b02-f7e224d5a346">01_메인페이지 - 로그인 전|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/41c2559b-d4c6-41f2-a4e6-c27f4c676c57">02_회원가입 페이지|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/9ee28c98-44b2-4f2d-ac42-e3de627b50a0">03_프로필 페이지|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/71b47345-72b3-479c-b75e-e7970d8739d9">04_메인페이지 - 로그인 후|
|<img width="500" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/b97dfc1d-8c68-42c2-978e-1855e4439b8e">05_카테고리 별 페이지|<img width="500" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/cdd3b93c-c6c1-41fe-8b73-391f78ded4ec">06_콘텐츠 별 페이지|
|<img width="500" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/8489a293-75ad-4d96-a700-6a447a6ddc3c">07_댓글 작성 시 페이지|<img width="500" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/47bd4c0a-a2dc-477b-b8ec-033e5275c363">08_글 작성 시 페이지|
|<img width="500" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/ad3e88e0-db38-4f1f-8024-1a9090772640">08_글 수정 시 페이지||

### 5-2. 실제 UI
|||
|-|-|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/834269c6-b393-439d-9239-31779f956f62">01_메인페이지 - 로그인 전|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/82263f9d-cea0-40b5-bfc2-756fd5257ee6">02_회원가입 페이지|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/66ad9ddd-5daf-4357-9cb9-ba66647e9fc0">03_프로필 페이지|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/7491d809-41ea-49da-a831-475f012dae99">04_메인페이지 - 로그인 후|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/740fc51f-78a0-400f-93f4-9d937b8b6456">05_블로그 입장|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/dd244027-c34e-4730-86d7-c1e7f00f8830">06_about페이지|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/db446e43-2b46-4a45-afae-f1712b82c2b7">07_카테고리별페이지-1|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/93529fb7-b47e-487f-aeb5-034193b9b9bd">08_카테고리별페이지-2|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/6949b66d-1269-4cb6-a462-861f07dd750f">09_태그별페이지|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/004eef28-0f1d-4cf7-8ed2-03ed72540763">10_콘텐츠별페이지|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/e6b34e41-ebae-4135-9c28-5a5d18437882">11_댓글작성페이지|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/d6be06d0-fc00-4a8b-91bf-30ded70a47f0">12_대댓글작성페이지|

## 6. 메인 기능

## 7. 추가 기능

## 8. 개발하며 경험한 오류와 해결방법
- 2023.10.26
  - admin 페이지 깨지는 문제
  - 원인: 404Error 페이지 따로 만든다고 `settings.py`에서 `DEBUG` 설정을 `False`로 해놓은 것에서 문제가 발생한 것으로 확인
    - `DEBUG` 설정을 `False`로 놓으면 `Django`가 디버그 정보를 더이상 제공하지 않으며, 정적파일을 자동으로 제공하지 않음.
    - `Django`의 admin 페이지는 정적파일인 (JavaScript, CSS 등)을 사용하기 때문에 `DEBUG` 설정이 `False`인 상태에서 페이지가 깨지는 문제가 발생할 수 있습니다.
  - 해결방안
    - 정적 파일을 따로 제공하는 `collectstatic` 명령어를 사용하여 `STATIC_ROOT`에 지정된 위치로 복사하여 `DEBUG` 설정이 `FALSE` 이더라도 정적파일을 사용할 수 있도록 하여 해결하였음.
- 2023.10.27
  - 카테고리 context 문제
    - 원인: `blog`의 `views.py`에서 `category.html`로만 `context`를 넘기는 것 때문에 `base.html`에서 해당 `context`를 받고 싶어도 받을 수 없었다.
  - 해결방안
    - `html`로 넘기고 싶은 `context`만 따로 utils폴더에 py파일로 만든 후 `settings.py`에 `context_procerssers`로 넘겨서 전체 파일에서 접근할 수 있도록 하였음.
  ```python
  # utils/context_processors.py
  from blog.models import Category

  def categories(request):
      return {
          'categories': Category.objects.all(),
              }
  ```
  ```python
  # settings.py
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'utils.context_processors.categories', # <- 해당 부분에 추가
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```
  ```html
  # base_detail.html
  ...생략...
  {% for category in categories %} <!-- context_processors.py에서 작성한 categories로 접근 -->
      <li>
          <a href="{% url 'blog:category' category.name %}">
              {{ category.category_name }}
          </a>
      </li>
  {% endfor %}
  ...생략...
  ```
- 2023.10.30
  - 프로필 업데이트 기능 추가하다가 `405 Error` 발생
    ```
    Method Not Allowed (POST): /accounts/profile_update/
    Method Not Allowed: /accounts/profile_update/
    ```
  - 원인: `urls.py`에서 url 중복 관련으로 확인
  - 해결방안
    - 분명히 `ProfileUpdateView` 클래스를 구현하면서 `GET` 메소드랑 `POST` 메소드 둘다 작성을 해주었고, url 도 중복되지 않도록 작성하였다.
    - 이유를 찾다가 `views.py` 에서 `def post(self, request)` 라고 작성해야 할 것을 하나를 대문자로 `def Post(self, request)` 라고 작성해서 생긴 오류였다.
    - 즉, `Python`의 클래스 메서드는 대소문자를 구분하기 때문에 `post` 에 대한 기능이 없어서 허용되지 않은 메소드라고 출력한 것.
    - 단순한 오타로 발생한 오류이지만, 이를 계기로 더욱 꼼꼼하게 봐야겠다고 생각되었음.
- 2023.11.01
  - 댓글 수정 기능을 기존 함수형으로 구현했던 것을 클래스형으로 다시 구현하다가 `404 Error` 발생
  - 원인: 쿼리 결과에 `comment`가 없습니다.
    ```
    Request Method:POST
    Request URL:http://127.0.0.1:8000/blog/19/comment/edit/
    Raised by:blog.views.CommentUpdateView
    ```
    - `CommentUpdateView` 클래스를 구현하면서 `comment`를 수정하고, `post`의 pk값을 받는 것으로 구현하여 문제가 발생한 것으로 확인.
  - 해결방안
    - `models.py`에서 `comment`에 `post`를 외래키로 이미 구현을 해놓았기 때문에 `comment`의 `post`로 접근을 하고, `html`파일에서 `comment.pk`를 인자로 받도록 수정하여 해결하였음.
   
- 2023.11.07
    - AWS lightsail로 배포 후 git pull 이후 static 파일과 media파일을못읽어오는 error 발 
