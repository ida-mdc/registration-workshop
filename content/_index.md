---
title: "Image Registration Workshop"
date: 2024-09
draft: false
layout: workshop
---

{{< title_meta title="Image Registration Workshop" presenter="Ella Bahry" position="MDC / Helmholtz Imaging" date="September 2024">}}

{{< notes >}}
In this workshop, we will explore fundamental concepts and practical techniques for image registration, focusing on applications in microscopy, material science, and earth science.
{{</ notes >}}

---

## What is Image Registration?

{{< horizontal >}}

<span style="font-size: 24px; color: white;">♡</span>
<span style="font-size: 24px; color: white;">♡</span>

<img src="img/registration.png" alt="MRI CT registration" style="width: 700px;" />

<span style="font-size: 24px; color: white;">♡</span>
<span style="font-size: 24px; color: white;">♡</span>

{{</ horizontal >}}

<h4>Spatial alignment of two or more images.</h4>

{{< notes >}}
Image registration is the process of transforming different sets of data into one coordinate system.
{{</ notes >}}

---

## Applications in Various Fields

{{< notes >}}
Image registration is widely used across multiple disciplines.
{{</ notes >}}

- **Microscopy**: Aligning slices in a 3D stack, channels, runs, tiles, modalities, or time points.
- **Medical Imaging**: Viewpoints, stacks, normalization to an atlas, co-registering images from different modalities (e.g., MRI, CT).
- **Material Science**: Comparing material properties under varying conditions.
- **Earth Science**: Aligning satellite images for change detection, georeferencing, integration from different sensors.

---

## Common needs in research

{{< horizontal >}}

Multimodal:
![](img/multimodal.jpg)

Stack:
![](img/slice_to_slice.jpg)  

Viewpoint:
![](img/coregistration.jpg)

Stitching:
![](img/stitching.jpg)

Temporal:
![](img/timesteps.jpg)

{{</ horizontal >}}

- Essential for comparing or integrating data

---

## Fundamental Technique #1 - Feature Detection & Transformation

{{< notes >}}
 An overview of common methods used in image registration, highlighting the two main steps involved.
{{</ notes >}}

two main steps:
1. **Detecting and matching similarities**: identifying corresponding regions or features 
   - **Feature-Based Registration** (SIFT, SURT, ORB, BRISK, FAST)
   - **Segmentation-Based Registration**
   - **model Fitting**
   - **Graph-Based Methods**
2. **Estimating and applying transformations**: Finding and applying the optimal transformation

{{< notes >}}
Estimating and applying transformations will be discussed in more detail in the next slides.
{{</ notes >}}

---

## Example Pipeline: Feature-Based Registration

{{< notes >}}
An example of applying a feature-based registration pipeline to align two images from different modalities.
{{</ notes >}}

{{< horizontal >}}

1. **Detecting Similarities**: identifying corresponding features
   - **Feature Detection**
     - Detect keypoints and their descriptors (e.g. using SIFT)
   - **Feature Matching**
     - Match features between images
2. **Estimating and Applying Transformations**: one image is transformed in space to match the other
    - **Transformation Estimation**
      - Compute transformation matrix (e.g. affine) using matched keypoints
    - **Warping**
      - Apply transformation to align images

<img src="img/sift_route.png" alt="sift keypoints and matches"/>

{{</ horizontal >}}

- [https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/sift_example.ipynb
](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/sift_example.ipynb
) 

{{< notes >}}
SIFT can be robust and thus can be used for multimodal registration.
{{</ notes >}}

---

## Image Transformation Types

![](img/transformations.png)

{{< notes >}}
The transformation matrix can also be used to warp other channels or annotation data such as segmentation.  

It's common to apply a more rough transformation first (e.g. affine), followed by an elastic transformation to correct for local deformations (e.g. TPS).
{{</ notes >}}

---

## Image Transformation Generation

![](img/transformation_nb.png)

- [https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/transformation_examples.ipynb
](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/transformation_examples.ipynb
) 

---

## Image Interpolation

![](img/interpolation_rotation.png)
![](img/interpolation_shearing.png)

{{< notes >}}
Interpolation is used to estimate pixel values at non-integer coordinates.
{{</ notes >}}

---

## Image Interpolation Generation

![](img/interpolation_nb.png)

- [https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/interpolation_example.ipynb
](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/interpolation_example.ipynb
) 

---

## Integrated Techniques: One-Step Registration

{{< notes >}}
Introducing registration methods that integrate detection and transformation into a single process.
{{</ notes >}}

- **Intensity-Based Registration**
  - Iterative - Optimize pixel intensity similarities directly to align images
- **Mutual Information-Based Registration**
  - Iterative - Use statistical dependence to align multimodal images
- **Frequency Domain Methods**
  - Compute transformations using Fourier transforms in the frequency domain.
- **Deep Learning-Based Registration**
  - Neural networks predict transformations directly from image data

---

## Challenges & Considerations

{{< notes >}}
Key challenges and preprocessing steps for effective image registration.
{{</ notes >}}

- **Preprocessing**:
  - Denoising, intensity correction, rescaling, applying filters

- **Performance vs. Complexity**:
  - Trade-off between accuracy and speed

- **Transformation Type**:
  - Fit transformation to deformation (e.g., rigid vs. non-rigid)

- **Method Selection**:
  - Match image type (e.g., multimodal) to appropriate method

---

## Software Tools for Image Registration

{{< notes >}}
Overview of common tools, libraries, and plugins for image registration.
{{</ notes >}}

- **Fiji/ImageJ**
  - Popular plugins: **Feature Extraction**, **Warpy** (QPath), **TrakEM2**, **Register Virtual Stack Slices**
- **Python Libraries**
  - **OpenCV** (C++), **SimpleITK**, **scikit-image**
- **Elastix**
  - Powerful tool for rigid and non-rigid registration
- **MATLAB**
  - Image Processing Toolbox (functions like `imregister`, `cpselect`)

---

## Hands-On Session

{{< tutorial-link >}}

{{< notes >}}
We will work through practical examples using Fiji/ImageJ and Python.
{{</ notes >}}

---

## Conclusion

{{< notes >}}
Recap of key concepts and encouragement to apply these techniques.
{{</ notes >}}

- Importance of image registration in research
- Next steps for implementing in your own work

---

## Thank You!

{{< notes >}}
Thank you for participating. Please feel free to reach out with any questions.
{{</ notes >}}

Contact: **ella.bahry at mdc-berlin.de**

