import os
import pickle

from src.face_encoder import FaceEncoder
from src.utils import load_image


class DatabaseBuilder:
    def __init__(self):
        self.encoder = FaceEncoder()
        self.database = {}

    def build_database(self, dataset_path):
        people = os.listdir(dataset_path)
        for person_name in people:
            person_folder = os.path.join(dataset_path,person_name)
            if not os.path.isdir(person_folder):
                continue
            print(f"\nProcessing {person_name}")

            embeddings = []
            for image_name in os.listdir(person_folder):
                image_path = os.path.join(person_folder,image_name)

                try:
                    image = load_image(
                        image_path
                    )

                    embedding = (
                        self.encoder
                        .get_embedding(image)
                    )

                    if embedding is not None:

                        embeddings.append(
                            embedding
                        )

                        print(
                            f"✓ {image_name}"
                        )
                    else:

                        print(
                            f"✗ No face found in {image_name}"
                        )

                except Exception as e:
                    print(
                        f"Error: {e}"
                    )

            if embeddings:
                self.database[
                    person_name
                ] = embeddings
        return self.database

    def save_database(
        self,
        output_path
    ):

        with open(output_path,"wb") as file:

            pickle.dump(
                self.database,
                file
            )
        print(
            f"\nDatabase saved to {output_path}"
        )