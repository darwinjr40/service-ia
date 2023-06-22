import imagehash

def compare_images(image1, image2):
  """Compares two images and returns the similarity score."""
  hash1 = imagehash.average_hash(image1)
  hash2 = imagehash.average_hash(image2)
  return hash1.difference(hash2)

image1 = "static/images/1-disco-wagner.png"
image2 = "static/images/2-disco-freno-kashima.jpg"

similarity_score = compare_images(image1, image2)
print(similarity_score)
if similarity_score < 10:
  print("The images are similar.")
else:
  print("The images are not similar.")
  
  
  
  
  
  