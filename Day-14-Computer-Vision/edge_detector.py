import cv2
import numpy as np
import os
import time

def run_vision_system():
    print("\n========================================================")
    print(" 👁️ AI COMPUTER VISION: EDGE DETECTION PIPELINE")
    print("========================================================\n")

    # 1. Generate a "Synthetic" Image to look at (so we don't need to download one)
    print("Step 1: Generating a synthetic test image (Canvas with shapes)...")
    # Create a blank 500x500 black canvas
    image = np.zeros((500, 500, 3), dtype="uint8")
    
    # Draw a blue rectangle and a red circle on the canvas
    cv2.rectangle(image, (100, 100), (400, 250), (255, 0, 0), -1)
    cv2.circle(image, (250, 350), 80, (0, 0, 255), -1)
    
    # Save the original image so you can look at it
    cv2.imwrite("1_original_image.png", image)
    print("-> Saved '1_original_image.png' to your folder.")
    time.sleep(1)

    # 2. Pre-process the image for the AI (Convert to Grayscale)
    # AI models process single-channel (black/white) data much faster than RGB color
    print("\nStep 2: Converting image to Grayscale (Optimizing for AI)...")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("2_grayscale_image.png", gray_image)
    print("-> Saved '2_grayscale_image.png' to your folder.")
    time.sleep(1)

    # 3. Apply the Canny Edge Detection Algorithm
    print("\nStep 3: Running Canny Edge Detection Algorithm...")
    # 100 and 200 are the lower and upper thresholds for determining what constitutes an "edge"
    edges = cv2.Canny(gray_image, 100, 200)
    cv2.imwrite("3_detected_edges.png", edges)
    print("-> Saved '3_detected_edges.png' to your folder.")
    
    print("\n========================================================")
    print("✅ Vision Pipeline Complete!")
    print("Open your 'Day-14-Computer-Vision' folder in Windows Explorer to see how the AI stripped the image down to its core geometry!")
    print("========================================================")

if __name__ == "__main__":
    run_vision_system()