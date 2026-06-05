import os
import pickle
import cv2

from src.face_engine import FaceEngine


class DatabaseBuilder:

    def __init__(self):

        self.engine = FaceEngine()

        self.database = {}

    def build_database(
        self,
        dataset_path
    ):

        people = os.listdir(
            dataset_path
        )

        for person_name in people:

            person_folder = os.path.join(
                dataset_path,
                person_name
            )

            if not os.path.isdir(
                person_folder
            ):
                continue

            print(
                f"\nProcessing {person_name}"
            )

            embeddings = []

            for image_name in os.listdir(
                person_folder
            ):

                image_path = os.path.join(
                    person_folder,
                    image_name
                )

                image = cv2.imread(
                    image_path
                )

                if image is None:

                    print(
                        f"Could not load {image_name}"
                    )

                    continue

                faces = (
                    self.engine
                    .get_faces(image)
                )

                if len(faces) == 0:

                    print(
                        f"No face found: {image_name}"
                    )

                    continue

                embedding = (
                    faces[0]
                    .embedding
                )

                embeddings.append(
                    embedding
                )

                print(
                    f"✓ {image_name}"
                )

            if len(
                embeddings
            ) > 0:

                self.database[
                    person_name
                ] = embeddings

        return self.database

    def save_database(
        self,
        output_path
    ):

        with open(
            output_path,
            "wb"
        ) as file:

            pickle.dump(
                self.database,
                file
            )

        print(
            f"\nDatabase saved to {output_path}"
        )