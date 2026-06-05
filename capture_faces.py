import os
import cv2
import time

from src.database_builder import DatabaseBuilder


def capture_faces(person_name):

    folder_path = os.path.join(
        "data",
        "known_faces",
        person_name
    )

    if not os.path.exists(folder_path):

        raise Exception(
            f"{person_name} not registered."
        )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        raise Exception(
            "Could not access webcam."
        )

    image_count = 0

    target_images = 20

    print(
        "\nCapturing Faces..."
    )

    time.sleep(2)

    while image_count < target_images:

        ret, frame = cap.read()

        if not ret:
            continue

        image_count += 1

        image_path = os.path.join(
            folder_path,
            f"image_{image_count}.jpg"
        )

        cv2.imwrite(
            image_path,
            frame
        )

        cv2.putText(
            frame,
            f"{image_count}/{target_images}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "Capturing Faces",
            frame
        )

        cv2.waitKey(1)

        time.sleep(0.3)

    cap.release()

    cv2.destroyAllWindows()

    print(
        "Capture Complete"
    )

    print(
        "Updating Database..."
    )

    builder = DatabaseBuilder()

    builder.build_database(
        "data/known_faces"
    )

    builder.save_database(
        "embeddings/face_database.pkl"
    )

    print(
        "Database Updated"
    )


if __name__ == "__main__":

    person_name = input(
        "Enter Person Name: "
    )

    capture_faces(
        person_name
    )