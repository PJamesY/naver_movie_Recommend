# Movie Recommend System

##  1. 프로젝트

- 네이버 영화 사이트에서 데이터 [영화 제목, 평점, user id]를 크롤링해서 user에게 영화 추천


## 2. 사용한 데이터

- training data / test data: 네이버 영화 사이트에서 데이터 크롤링 추출 : https://movie.naver.com/
- [영화 제목, 평점, user id]


##  3. 모델링 방법

Keras Deep learning을 이용한 embedding matrix를 이용한 평점 예측
- Matrix Factorization 활용

##  4. 모델 평가

training 데이터로 학습되어져서 나온 rating matrix(user latent matrix * movie latent matrix)와 test real 데이터의 rating의 차이를 비교해서 모델 성능 평가
