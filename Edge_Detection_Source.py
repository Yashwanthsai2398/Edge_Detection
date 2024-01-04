#YASHWANTH_SAI_BATHINI
from skimage import io, filters, color, feature  #Import necessary functions from skimage
import matplotlib.pyplot as plt  #Import matplotlib for visualization
import time  #Import time to measure execution time
#Read in the images
dog_food_can = io.imread('can.jpg')  #Read the dog food can image
wrench_1 = io.imread('wrench1.jpg')  #Read the first wrench image
wrench_2 = io.imread('wrench2.jpg')  #Read the second wrench image
#Function to measure execution time for edge detection
def measure_edge_detection_time(image, method):
    start = time.time()  #Record the start time
    if method == 'sobel':
        edges = filters.sobel(image) #Apply Sobel edge detection
    elif method == 'canny':
        edges = feature.canny(image) #Apply Canny edge detection
    end = time.time() #Record the end time
    return edges, end - start #Return the detected edges and execution time
#Function to display image comparisons
def display_comparison(image, sobel_edges, canny_edges, sobel_time, canny_time, title, axes):
    #Show original image
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Original') #Set title for the original image
    axes[0].axis('off') #Disable axis for better visualization
    # Show Sobel edges
    axes[1].imshow(sobel_edges, cmap='gray')
    axes[1].set_title(f'Sobel\nTime: {sobel_time:.4f} sec', fontsize=8, pad=2) #Set title for Sobel edges
    axes[1].axis('off')  # Disable axis for better visualization
    #Show Canny edges
    axes[2].imshow(canny_edges, cmap='gray')
    axes[2].set_title(f'Canny\nTime: {canny_time:.4f} sec', fontsize=8, pad=2) #Set title for Canny edges
    axes[2].axis('off')  #Disable axis for better visualization
    #Set title for the original image set
    axes[0].set_title(title, fontsize=12, pad=5)  #Adjusting title position
#Create a single figure for all comparisons
fig, axes = plt.subplots(3, 3, figsize=(12, 12))  #Create a grid of subplots
plt.tight_layout(pad=3.0)  # Adjust spacing between subplots
#Process each image
for ax_row, image, title in zip(axes, [dog_food_can, wrench_1, wrench_2], ['Dog Food Can', 'Wrench 1', 'Wrench 2']):
    gray_image = color.rgb2gray(image) #Convert image to grayscale 
    #Measure time and detect edges using Sobel and Canny methods
    sobel_edges, sobel_time = measure_edge_detection_time(gray_image, 'sobel')
    canny_edges, canny_time = measure_edge_detection_time(gray_image, 'canny')
    #Display image comparisons
    display_comparison(gray_image, sobel_edges, canny_edges, sobel_time, canny_time, title, ax_row)
plt.show() #Display all comparisons on the same screen
