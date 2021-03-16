# django-shopping_mall
## Shopping mall for the blind
---
## 실행영상링크
[유튜브연동](https://youtu.be/T9NfAIdmxuA)

## 개발기간
- 2020.03.02.~06.22. (약4개월)

### 적용기술
Framwork: Django <br>
Language : Python/HTML/JS/CSS<br>
Server : Apache/AWS/Docker<br>
Code : Git<br>

### 상세 내용
- 쇼핑몰 서버 구축
- 데이터베이스 관리

- 기능
  - 로그인
  - 상품관리 / 재고 관리
  - 주문 관리
  - 장바구니
  - TTS
  - 확대
  - allauth
  - API

- 서버
  - NAS-Doker
  - Apache Tomcat

- 데이터베이스
  - Django ORM
  - Query Set
---

## 실행방법
1. clone django project
2. 프로젝트 경로에서 $ python -m venv <가상환경이름>
3. 가상환경 실행 $ source <가상환경>/scripts/activate (mac은 scripts->bin)
4. pip 설치 $ pip install -r requirements.txt
5. db update $ python manage.py makemigrations
6. 서버 실행 $ python manage.py runserver
