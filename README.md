# ⚗Chemical Compound Property DataBase Website

## 📌프로젝트 소개

#### 1. 메인 기능

화합물의 이름을 검색하면 해당 물질의 물성을 나열해 준다.

#### 2. 구성

- 검색창 중심의 메인 페이지

- 해당 화합물의 정보를 나타내주는 detail 페이지

  

#### 99. 추가로 넣고 싶은 기능

- 그래프에 커서를 두면 해당 점의 좌표값이 뜨는 기능
- 버전 update(What's New)나 tutorial 등으로 구성된 blog



## 📌프로젝트 제작 과정

1. DB에 기본 물성 변수 저장하기

     - `views.py`를 사용해서 저장하면 안되는 이유

       

2. Cp, Pvap 그래프 그려서 저장하기

   - 그래프 중첩
   - `Fail to create pixmap with Tk_GetPixmap in TkImgPhotoInstanceSetSize`

   

3. template에 변수명을 사용해서 img 넣기