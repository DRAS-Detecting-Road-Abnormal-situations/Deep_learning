# yolo_model 제작

## 교통 사고 감지 모델(yolov4, yolov3)

#### 개발 환경
```bash
• yolo darknet
• RTX2060 gpu(Compute Capability : 7.5)
•	window 10 
• CUDA, Cudnn, opencv
'''

#### 교통사고 감지 custom 모델 제작(yolov3, yolov4)
```bash
1. 데이터 수집
  - 자동차 사고 cctv 수집
2. 데이터 분류
  - 정면충돌, 옆면충돌, 후면충돌, 혼자 회전하여 사고 4가지로 구분하여 분류 작업
3. 프레임 추출
  - ffmpeg프로그램 사용하여 사고 영상 이미지 추출
  - 사고난 장면만 뽑아서 다시 분류
4. 정면 충돌 위주의 이미지 증분
  - 90도, 180도 회전하여 이미지 증분
5. 이미지 라벨링
  - yolomark 사용 
6. cfg파일 수정
  - class=1 -> car_accident
  - yolov3 -> filters = (classes +5)*3
7. convolution layer 파일 다운로드(pretrained model 사용)
8. test
  -test 데이터로 학습결과 확인
'''





