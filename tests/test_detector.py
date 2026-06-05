import cv2
from src.face_detector import FaceDetector
def main():
    detector = FaceDetector()
    image = cv2.imread(
        "data/known_faces/Ayush/1.jpeg"
    )
    faces = detector.detect_faces(
        image
    )
    print(
        f"Faces Found: {len(faces)}"
    )
    for face in faces:
        bbox = face.bbox.astype(int)
        x1, y1, x2, y2 = bbox
        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )
        confidence = face.det_score
        cv2.putText(
            image,
            f"{confidence:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )
    cv2.imshow(
        "Detection Test",
        image
    )
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()