# Image Compression Using Singular Value Decomposition (SVD)

## Overview

This project implements an Image Compression System using Singular Value Decomposition (SVD). The system reduces image size by retaining only the most significant singular values while preserving important visual features.

The application supports both grayscale and color images through a user-friendly graphical interface developed using Python.

---

## Objective

- Reduce image storage requirements.
- Preserve visual quality after compression.
- Provide adjustable compression levels using k values.
- Evaluate compression quality using MSE and PSNR.

---

## Features

- Supports grayscale and color images.
- Adjustable compression using k value slider.
- Displays original and compressed images.
- Calculates MSE and PSNR metrics.
- Downloads compressed images.
- GUI-based application using Tkinter.

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core implementation |
| NumPy | Matrix operations and SVD |
| OpenCV | Image processing |
| Pillow (PIL) | Image handling |
| Tkinter | GUI development |
| Matplotlib | Visualization |

---

## System Requirements

### Hardware
- Processor: Intel i3 or above
- RAM: Minimum 4 GB
- Storage: 500 GB HDD/SSD

### Software
- Python 3.x
- NumPy
- OpenCV
- Pillow
- Matplotlib
- Tkinter

---

## System Workflow

```text
Input Image
      ↓
Preprocessing
      ↓
SVD Decomposition
      ↓
Select k Singular Values
      ↓
Reconstruction
      ↓
Compressed Image
      ↓
Performance Evaluation
```

---

## Modules

### 1. Input Module
Loads image files such as JPG, PNG, and BMP.

### 2. Preprocessing Module
Converts images into a suitable matrix format for processing.

### 3. SVD Decomposition Module
Decomposes the image matrix into U, Σ, and Vᵀ matrices.

### 4. Compression Module
Retains only the top k singular values and removes redundant information.

### 5. Reconstruction Module
Reconstructs the compressed image using reduced matrices.

### 6. Evaluation Module
Calculates image quality metrics such as MSE and PSNR.

---

## Mathematical Model

An image is represented as a matrix A and decomposed using Singular Value Decomposition:

A = U Σ Vᵀ

Where:

- A = Original image matrix
- U = Left singular vectors
- Σ = Diagonal matrix of singular values
- Vᵀ = Transpose of right singular vectors

For compression:

Ak = Uk Σk Vkᵀ

Where:

- k is the number of singular values retained.
- Smaller k provides higher compression.
- Larger k provides better image quality.

---

## Performance Metrics

### Mean Squared Error (MSE)

Measures the average squared difference between the original and compressed image.

### Peak Signal-to-Noise Ratio (PSNR)

Measures image quality after compression.

- Lower MSE indicates better compression quality.
- Higher PSNR indicates better reconstructed image quality.

---

## Sample Results

### Grayscale Image

- MSE: 1.9095
- PSNR: 45.32 dB
- Compression Ratio: 6.26 : 1

### Color Image

- MSE: 0.5712
- PSNR: 50.56 dB
- Compression Ratio: 5.33 : 1

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Image-Compression-Using-SVD.git
```

Move to the project directory:

```bash
cd Image-Compression-Using-SVD
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python STEMPRO.py
```

---

## Application Usage

1. Upload an image.
2. Select Grayscale or Color mode.
3. Adjust the k value using the slider.
4. Click Compress Image.
5. View compression results.
6. Download the compressed image.

---

## Future Scope

- Integration with Deep Learning and AI.
- Video Compression using SVD.
- Hybrid DWT-DCT-SVD Compression Models.
- GPU and FPGA acceleration.
- Medical and Satellite Image Compression.

---

## References

[1] M. A. Alam, M. R. Islam, and S. Rahman, "Singular Value Decomposition 
Guided Image Compression," IEEE Access, vol. 12, pp. 45678–45689, 2024. 

[2] S. Banerjee and A. Roy, "Image Compression using Hybrid Transform 
Techniques," IEEE International Conference on Smart Computing, pp. 210–215, 
2023. 

[3] T. Chlubna and P. Zemčík, "Comparative Study of Image Compression 
Techniques," Journal of Real-Time Image Processing, vol. 22, no. 3, pp. 567
580, 2025. 

[4] G. Garg and R. Kumar, "Multi-Level Image Compression using SVD and 
DCT," International Journal of Computer Applications, vol. 180, no. 25, pp. 12
18, 2022. 

[5] G. Garg, A. Sharma, and R. Kumar, "Adaptive Hybrid Image Compression 
using DCT and SVD," International Journal of Signal Processing Systems, vol. 
12, no. 1, pp. 34–42, 2024. 

--- 
