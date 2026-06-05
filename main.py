import cv2

from src.face_engine import FaceEngine
from src.database_loader import DatabaseLoader
from src.recognizer import Recognizer
from src.camera import Camera


def main():

    loader = DatabaseLoader(
        "embeddings/face_database.pkl"
    )

    database = loader.load_database()

    recognizer = Recognizer(
        database,
        threshold=15.0
    )

    engine = FaceEngine()

    camera = Camera()

    print(
        "\nFace Recognition Started"
    )

    print(
        "Press Q to Quit\n"
    )

    frame_count = 0

    cached_faces = []

    while True:

        ret, frame = (
            camera.read_frame()
        )

        if not ret:
            break

        frame_count += 1

        # Process only every 5th frame
        if frame_count % 5 == 0:

            faces = (
                engine.get_faces(
                    frame
                )
            )

            cached_faces = []

            for face in faces:

                bbox = (
                    face.bbox.astype(int)
                )

                x1, y1, x2, y2 = bbox

                embedding = (
                    face.embedding
                )

                name, distance = (
                    recognizer.recognize(
                        embedding
                    )
                )

                confidence = (
                    recognizer
                    .distance_to_confidence(
                        distance
                    )
                )

                cached_faces.append(
                    {
                        "bbox": bbox,
                        "name": name,
                        "confidence": confidence
                    }
                )

        # Draw cached results
        for face_data in cached_faces:

            x1, y1, x2, y2 = (
                face_data["bbox"]
            )

            name = (
                face_data["name"]
            )

            confidence = (
                face_data["confidence"]
            )

            color = (
                (0, 255, 0)
                if name != "UNKNOWN"
                else (0, 0, 255)
            )

            label = (
                f"{name} "
                f"{confidence:.1f}%"
            )

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                color,
                2
            )

            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

        cv2.imshow(
            "Face Recognition",
            frame
        )

        key = (
            cv2.waitKey(1)
            & 0xFF
        )

        if key == ord("q"):
            break

    camera.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()