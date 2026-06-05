from insightface.app import FaceAnalysis
class FaceEncoder:
    def __init__(self):
        self.app = FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )
        self.app.prepare(
            ctx_id=0,
            det_size=(640, 640)
        )
    def get_embedding(self, image):
        faces = self.app.get(image)
        if len(faces) == 0:
            return None
        largest_face = max(
            faces,
            key=lambda x: (
                x.bbox[2] - x.bbox[0]
            ) * (
                x.bbox[3] - x.bbox[1]
            )
        )
        return largest_face.embedding