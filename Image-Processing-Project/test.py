import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('sample.jpg')

# Check if image loaded
if image is None:
    print("Error: Image not found. Make sure sample.jpg is in the same folder.")
    exit()

# Convert to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Edge detection
edges = cv2.Canny(gray, 100, 200)

# Display images
plt.figure(figsize=(10,5))

plt.subplot(1,3,1)
plt.imshow(image_rgb)
plt.title('Original')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(gray, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(edges, cmap='gray')
plt.title('Edges')
plt.axis('off')

plt.show()