import cv2
import numpy as np
import matplotlib.pyplot as plt

# A. Capture the image from the RoboMaster camera
# Assuming the image is already captured and provided (image from the attachment)
image = cv2.imread('Test_camer.jpg')

# B. Show the original image and print the size of the image
cv2.imshow('Original Image', image)
print(f'Image size: {image.shape}')  # Image shape gives (height, width, channels)

# # C. Convert the original RGB image to HSL color space and show the L-channel image
hsl_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)  # Convert to HSL (OpenCV uses HLS format)
l_channel = hsl_image[:, :, 1]  # Extract L-channel
cv2.imshow('L-channel Image', l_channel)

# # D. Plot the histogram of the L-channel image
# plt.figure()
# plt.hist(l_channel.ravel(), bins=256, range=[0, 256],)
# plt.title('Histogram of L-channel')
# plt.show()

# E. Rescale the L-channel image from pixel value range [0, 255] to [-1, 1]
l_rescaled = l_channel / 127.5 - 1  # Rescale to [-1, 1]

# # F. Plot the histogram of the rescaled L-channel image
# plt.figure()
# plt.hist(l_rescaled.ravel(), bins=256, range=[-1, 1])
# plt.title('Histogram of Rescaled L-channel')
# plt.show()

# G. Create a random noise image with the equal size of the original image
noise = np.random.normal(0, 1, l_channel.shape)  # Normal distribution (mean=0, variance=1)
cv2.imshow('Noise Image', noise)

# # H. Combine the noise image with the rescaled L-channel image
combined_image = l_rescaled + noise
cv2.imshow('Combined Image', combined_image)

# # I. Rescale L-channel image back to original pixel value [0, 255] and convert back to RGB color-space
l_rescaled_back = np.clip((combined_image + 1) * 127.5, 0, 255).astype(np.uint8)
hsl_image[:, :, 1] = l_rescaled_back
final_image = cv2.cvtColor(hsl_image, cv2.COLOR_HLS2BGR)
cv2.imshow('Final Image', final_image)

# J. (Bonus) Apply the Box blur filter with kernel size = 6 to the L-channel image and show the result image
combined_image = cv2.blur(l_channel, (6, 6))
hsl_image[:, :, 1] = combined_image
final_blurred_image = cv2.cvtColor(hsl_image, cv2.COLOR_HLS2BGR)
cv2.imshow('Final Blurred Image', final_blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()