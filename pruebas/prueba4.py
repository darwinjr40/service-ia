import cv2
import scipy.spatial.distance

def compare_images(image1, image2):
  """Compares two images and returns the similarity score."""
  image1_features = extract_features(image1)
  image2_features = extract_features(image2)
  similarity_score = scipy.spatial.distance.euclidean(image1_features, image2_features)
  return similarity_score

def extract_features(image):
  """Extracts features from an image."""
  # TODO: Implement this function

image1 = "static\images\3-disco-freno-raybestos.jpg"
image2 = "static\images\4-disco-freno-ibiza.png"
frame = cv2.imread(image1)
cv2.imshow("Comparacion de Objetos", frame)

# similarity_score = compare_images(image1, image2)

# if similarity_score < 10:
#   print("The images are similar.")
# else:
#   print("The images are not similar.")