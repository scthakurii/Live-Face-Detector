from src.detect_faces import detect_faces_live

if __name__ == "__main__":
    HAAR_CASCADE_PATH = "models/haarcascades/haarcascade_frontalface_default.xml"
    detect_faces_live(HAAR_CASCADE_PATH)
