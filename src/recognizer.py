import numpy as np


class Recognizer:

    def __init__(
        self,
        database,
        threshold=16.5
    ):

        self.database = database

        self.threshold = threshold

    def recognize(
        self,
        embedding
    ):

        best_match = None

        best_distance = float("inf")

        for person_name, embeddings in self.database.items():

            for known_embedding in embeddings:

                distance = np.linalg.norm(
                    embedding -
                    known_embedding
                )

                if distance < best_distance:

                    best_distance = distance

                    best_match = person_name

        print(
            f"Best Match: {best_match}"
        )

        print(
            f"Distance: {best_distance:.4f}"
        )

        if best_distance > self.threshold:

            return (
                "UNKNOWN",
                best_distance
            )

        return (
            best_match,
            best_distance
        )

    def distance_to_confidence(
        self,
        distance
    ):

        confidence = max(
            0,
            min(
                100,
                100 - ((distance - 10) * 20)
            )
        )

        return confidence