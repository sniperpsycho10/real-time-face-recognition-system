import cv2

from src.face_engine import FaceEngine
from src.database_loader import DatabaseLoader
from src.recognizer import Recognizer


def main():

    loader = DatabaseLoader(
        "embeddings/face_database.pkl"
    )

    database = loader.load_database()

    recognizer = Recognizer(
        database,
        threshold=18.0
    )

    engine = FaceEngine()

    image = cv2.imread(
        "data/test_images/ayush_test.jpg"
    )

    if image is None:

        print(
            "Image not found"
        )

        return

    faces = engine.get_faces(
        image
    )

    print(
        f"Faces Found: {len(faces)}"
    )

    for face in faces:

        name, distance = (
            recognizer.recognize(
                face.embedding
            )
        )

        confidence = (
            recognizer
            .distance_to_confidence(
                distance
            )
        )

        print(
            f"Name: {name}"
        )

        print(
            f"Distance: {distance:.4f}"
        )

        print(
            f"Confidence: {confidence:.2f}%"
        )


if __name__ == "__main__":
    main()