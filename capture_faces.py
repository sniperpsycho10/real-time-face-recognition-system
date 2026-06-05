import os
import cv2
import time
from src.database_builder import DatabaseBuilder

def capture_faces():

    print(
        "\n===== FACE DATASET CAPTURE =====\n"
    )

    person_name = input(
        "Enter Person Name: "
    ).strip()

    folder_path = os.path.join(
        "data",
        "known_faces",
        person_name
    )

    if not os.path.exists(
        folder_path
    ):

        print(
            "\nPerson not registered."
        )

        print(
            "Run register_person.py first."
        )

        return

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        print(
            "Could not access webcam."
        )

        return

    image_count = 0

    target_images = 20

    print(
        "\nLook at the camera."
    )

    print(
        "Capturing starts in 3 seconds..."
    )

    time.sleep(3)

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
            f"Captured: {image_count}/{target_images}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "Dataset Capture",
            frame
        )

        print(
            f"Saved: image_{image_count}.jpg"
        )

        cv2.waitKey(1)

        time.sleep(0.3)

    cap.release()

    cv2.destroyAllWindows()

    print(
        "\nCapture Complete."
    )

    print(
        f"{target_images} images saved."
    )

    print(
        "\nRebuilding Face Database..."
    )

    builder = DatabaseBuilder()

    builder.build_database(
        "data/known_faces"
    )

    builder.save_database(
        "embeddings/face_database.pkl"
    )

    print(
        "\nDatabase Updated Successfully."
    )


if __name__ == "__main__":

    capture_faces()