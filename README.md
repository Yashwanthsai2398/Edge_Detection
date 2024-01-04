Experiment Overview:
 • Conducted edge detection using Sobel and Canny algorithms on three images: Dog Food Can, Wrench 1, and Wrench 2.
 • Analyzed the impact of these algorithms on edge detection in grayscale images.
Findings:
Dog Food Can:
 • Sobel: Detected edges appear sharp and defined, highlighting contours and edges effectively.
 • Canny: Produced smoother edges compared to Sobel, might miss some fine details but 
reduced noise.
Wrench 1:
 • Sobel: Identified clear edges but might be affected by noise in the image.
 • Canny: Smoothed out noise better compared to Sobel, capturing major edges effectively.
Wrench 2:
 • Sobel: Detected edges prominently but seemed to capture noise as well.
 • Canny: Produced cleaner edges by suppressing noise, albeit some finer details might be 
missed.
Performance Analysis:
Sobel Algorithm:
 • Generally, faster in computation time compared to Canny.
 • Tends to capture more noise in edges.
Canny Algorithm:
 • Slower computation time due to the multi-step process.
 • Provides smoother, cleaner edges by suppressing noise better.
Conclusion:
The choice between Sobel and Canny algorithms depends on the specific image characteristics and the trade-off between edge clarity and noise suppression. Sobel offers faster processing but might 
capture more noise, while Canny produces cleaner edges at the cost of longer computation time.
