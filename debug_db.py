import pickle

with open(
    "embeddings/face_database.pkl",
    "rb"
) as file:

    db = pickle.load(file)

print("\nPeople Found:\n")

for person, embeddings in db.items():

    print(
        person
    )

    print(
        f"Images: {len(embeddings)}"
    )

    print(
        f"Embedding Shape: {embeddings[0].shape}"
    )

    print()