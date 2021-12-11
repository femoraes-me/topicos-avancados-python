import cv2
from pathlib import Path

video_path = str(Path(__file__).absolute().parent / 'inputs' / 'face.mp4')

paths = {
    "faces": str(Path(__file__).absolute().parent / "data" / "haarcascades" / "haarcascade_frontalface_default.xml"),
    "eyes": str(Path(__file__).absolute().parent / "data" / "haarcascades" / "haarcascade_eye.xml"),
    "smile": str(Path(__file__).absolute().parent / "data" / "haarcascades" / "haarcascade_smile.xml"),
    "upperbody": str(Path(__file__).absolute().parent / "data" / "haarcascades" / "haarcascade_upperbody.xml"),
}

cap = cv2.VideoCapture(video_path)

detectors = {}

for name, path in paths.items():
  detectors[name] = cv2.CascadeClassifier(path)

while True:
  ret, frame = cap.read()
  if not ret:
    break

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  bodyResults = detectors["upperbody"].detectMultiScale(gray, minSize=(180, 180))

  for bodyResult in bodyResults:
    cv2.rectangle(frame, bodyResult, (255, 0, 0), 2)
    x, y, w, h = bodyResult
    body = gray[y:y+h, x:x+w]
    faceResults = detectors["faces"].detectMultiScale(body, minSize=(150, 150))

    for faceResult in faceResults:
      faceCap = [faceResult[0] + x, faceResult[1] + y, faceResult[2], faceResult[3]]
      x, y, w, h = faceResult
      face = body[y:y+h, x:x+w]
      cv2.rectangle(frame, faceCap, (0, 255, 0), 3)
      eyes = detectors["eyes"].detectMultiScale(face, minSize=(15, 15))
      smiles = detectors["smile"].detectMultiScale(face, minSize=(25, 25))

      for eye in eyes:
        roi = eye
        roi[0:2] += faceCap[0:2]
        cv2.rectangle(frame, roi, (255, 0, 0), 3)
        if(roi[0] < (faceCap[2]/2) + faceCap[0]):
          cv2.rectangle(frame, roi, (255, 255, 255), 2)
        else:
          cv2.rectangle(frame, roi, (255, 0, 255), 2)
      for smile in smiles:
        roi = smile
        roi[0:2] += faceCap[0:2]
        cv2.rectangle(frame, roi, (0, 0, 255), 3)

  cv2.imshow("Video", frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()