import cv2

def remove_background(input_image_path, output_image_path):
    # Load image
    image = cv2.imread(input_image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Thresholding (adjust threshold values as needed)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    
    # Invert the mask
    mask = cv2.bitwise_not(thresh)
    
    # Apply the mask to the image
    result = cv2.bitwise_and(image, image, mask=mask)
    
    # Save output image
    cv2.imwrite(output_image_path, result)

# Example usage
input_image = 'input.jpg'
output_image = 'output.png'
remove_background(input_image, output_image)
