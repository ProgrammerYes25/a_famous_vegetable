# 🌿 명의 나물 프로젝트 설명
***
## 💡 명의 나물 프로젝트 소개

- **유명한 명언, 명대사**를 모아서 **한 눈에 조회, 추가, 기록할 수 있는 프로그램**입니다. 
***
## 😀😀 팀원

- 2214 조예서 (기획, 개발)
- 2114 황유솔 (기획)

## 📅 기획&개발 기간

- 기획 : 2022.08.10 ~ 2022.08.13
- 개발 : 2022.12.02 ~ 2022.12.04

## 💻 개발 환경

- Language : Python
- IDE : Pytcharm
- DB : MySQL
- GUI : Tkinter
***

## 📌 기능

### 주요기능
- 명언, 명대사 조회, 추가, 삭제
- 일기 추가, 조회
***
- 메인 화면

![메인화면](https://user-images.githubusercontent.com/108272947/205522869-36551561-e32d-4426-b34a-6708921d6ab1.gif)
#### 명언
- 명언 추가

![명언 추가](https://user-images.githubusercontent.com/108272947/205522866-1ee6f6db-17ff-494e-bbaf-5c49cda8f823.gif)

- 명대사 명가사 추가

![명대사 명가사 추가](https://user-images.githubusercontent.com/108272947/205522867-9fecfcab-70f0-4544-a35f-1204583d478b.gif)

- 명언, 명대사 조회

![메뉴판](https://user-images.githubusercontent.com/108272947/205522874-f67a2ea2-92a0-452d-8405-e6592f4cd904.gif)

#### 일기
- 일기추가 일기  

![일기 추가](https://user-images.githubusercontent.com/108272947/205522860-c3760557-6039-41b0-8d7c-55c809c62356.gif)

- 일기 조회

![식탁](https://user-images.githubusercontent.com/108272947/205522863-ca478c13-ce56-4edf-97c9-67a2332867f2.gif)

- 일기 열람

![일기 열람](https://user-images.githubusercontent.com/108272947/205522865-5e5c07e6-9b0d-49fb-89bb-64451edb98d3.gif)

## 📎기술
### 라이브러리
- tkinter
- pymysql
***
### 데이터 구성
- 명언 테이블
![saying_tb](https://user-images.githubusercontent.com/108272947/205522875-9439380c-9922-4830-817a-7032f3018a65.gif)
- 일기 테이블
![diary_tb](https://user-images.githubusercontent.com/108272947/205522876-5b0ba375-9c89-422b-abc4-5507346c71cb.gif)

### Class 구성
#### DBHelper dB py
- 데이터 베이스 사용 하게 도와주는 Class
#### inOutputClass
- 데이터 베이스에 넣고 빼는 동작들이 들어 있는 Class
#### main
- 화면 구성 동작들이 들어있는 Class
