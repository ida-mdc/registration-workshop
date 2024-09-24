---
title: "Image Registration Workshop"
date: 2024-09-23
draft: false
layout: workshop
author: Ella Bahry
cover: img/registration.png
---

## What is Image Registration?

{{< notes >}}
In this workshop, we will explore fundamental concepts and practical techniques for image registration, focusing on applications in microscopy, material science, and earth science.
{{</ notes >}}

![](img/registration_big.png)

<h4>Spatial alignment of two or more images.</h4>
 
- It's an essential  step for comparing or integrating data in many scientific fields.


{{< notes >}}
Image registration is the process of aligning multiple datasets into a common coordinate system, enabling accurate comparison and analysis.
{{</ notes >}}

---

## Common needs in research

{{< horizontal >}}
Multimodal:
![](img/multimodal.jpg)

Stitching:
![](img/stitching.jpg)

Stack:
![](img/slice_to_slice.jpg)  

Viewpoint:
![](img/coregistration.jpg)

Temporal:
![](img/timesteps.jpg)

{{</ horizontal >}}

{{< notes >}}
Image registration is widely used across multiple disciplines.
{{</ notes >}}

- **Microscopy**: Aligning slices in a 3D stack, channels, runs, time points, tiles (stitching), and modalities.

- **Medical Imaging**: Viewpoints, stacks, normalization to an atlas, co-registering images from different modalities (e.g., MRI, CT).

- **Earth Science**: Georeferencing, integration from different sensors, aligning satellite images for change detection.

- **Material Science**: Comparing material properties under varying conditions.

---


## Image Transformation Types

{{< horizontal >}}

![](img/transformations.png)

![](img/affine.png)

{{</ horizontal >}}

[Link to: example_notebooks/transformation_examples.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/transformation_examples.ipynb
) 

{{< notes >}}
The type of transformation should be chosen based on the expected deformations in the images.  
It's common to apply a more rough transformation first (e.g. affine), followed by an elastic transformation to correct for local deformations (e.g. TPS).  
But more is not always better, as more complex transformations can lead to overfitting and with each transformation some errors are introduced (due to interpolation).

The transformation matrix can also be used to warp other channels or annotation data such as segmentation labels.  

Rigid transformation requires 2 points, affine 3 points, perspective 4 points, ideally for local deformations require more.
{{</ notes >}}

---

## Image Interpolation - Reason

- When we transform an image, we need to estimate pixel values at the new coordinates.
- If for example, you transform an image by up-scaling it: 

![](img/grids.png)

- Interpolation is the process of estimating pixel values at non-integer coordinates.

---

## Image Interpolation - Common Types

{{< notes >}}
When you transform an image to a new space, you need to estimate the pixel values at the new locations.
Interpolation is used to estimate pixel values at non-integer coordinates.
{{</ notes >}}

{{< horizontal >}}
![](img/interpolation_functions.png) 

![](img/interpolation_weights.png)
{{</ horizontal >}}

Image by [Cmglee](https://commons.wikimedia.org/wiki/User:Cmglee), license: CC BY-SA 4.0  
[Link to interpolation weights and examples notebook: example_notebooks/interpolation.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/interpolation.ipynb
) 

{{< notes >}}
- Interpolation weights demo: For each interpolation type it randomly picks subpixel localization and shows weights of surrounding pixels.
- Example toy image: Shows the effect of different interpolation types on a simple image.
- Example of anti-aliasing when down-sampling.
{{</ notes >}}

---

## Image Interpolation Example

![](img/interpolation_rotation.png)
![](img/interpolation_shearing.png)

---

## Image Interpolation - Anti-Aliasing in Down-Sampling

![](img/antialias.png)

- When down-sampling an image, aliasing artifacts can occur, thus applying anti-alising filters can help to reduce these artifacts.
- But, anti-aliasing filters can also blur the image, so it's a trade-off between sharpness and aliasing artifacts.

---

## Integrated Image Registration Techniques

{{< notes >}}
Introducing registration methods that combine both matching and transformation into one smooth process, simplifying image alignment. 
{{</ notes >}}

- **Intensity-Based Registration**
  - Iterative process that optimizes aligned pixel intensity similarities (e.g. **correlation coefficient** or **MSE**).
- **Mutual Information-Based Registration**
  - Iteratively aligns multimodal images by maximizing the statistical relationship between them.
- **Frequency Domain Methods**
  - Transforms images into the Fourier space to compute alignment transformations.
- **Deep Learning-Based Registration**
  - Uses neural networks to predict transformations from image data, learning complex patterns.

---

## Technique: Intensity Based (Correlation Coefficient)

![](img/correlation_r45_s1.5.png)
![](img/correlation_r10_s1.1.png)
![](img/correlation_r2_s1.png)
![](img/correlation_r0_s1.png)

{{< notes >}}
[Examples were generated using: example_notebooks/correlation_example.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/correlation_example.ipynb
)
{{</ notes >}}

---

## Technique: Mutual Information

{{< horizontal >}}

<img src="img/joint_histogram_iterative.gif" alt="Mutual Information iterations"/>

![](img/hist.png)
![](img/mutual_information_equation.png)

{{</ horizontal >}}

- Looking at the equation, the more structure we have in the joint histogram, the lower its entropy, and thus the mutual information is higher.

{{< notes >}}
Entropy is maximized when there is maximum uncertainty or randomness in the pixel intensities.  
Meaning that an image with a single pixel intensity value will have minimum entropy, and an image with a uniform distribution of pixel intensities will have maximum entropy.
{{</ notes >}}

- [Mutual Information implementation notebook: example_notebooks/mutual_information.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/mutual_information.ipynb
) 

---

<h2>2 Step Techniques - Feature Detection & Transformation</h2>

{{< notes >}}
 An overview of common methods used in image registration, highlighting the two main steps involved.
{{</ notes >}}

two main steps:
1. **Detecting and matching similarities**: identifying corresponding regions or features 
   - **Feature-Based Registration** (SIFT, SURT, ORB, BRISK, FAST)
   - **Segmentation-Based Registration**
   - **Model Fitting**
   - **Graph-Based Methods**
2. **Estimating and applying transformations**: Finding and applying the optimal transformation

{{< notes >}}
Estimating and applying transformations will be discussed in more detail in the next slides.
{{</ notes >}}

---

## Technique: Feature-Based Registration (SIFT)

{{< notes >}}
An example of applying a feature-based registration pipeline to align two images from different modalities.
{{</ notes >}}

{{< horizontal >}}

1. **Detecting Similarities**: 
   - **Feature Detection:** Detect keypoints and their descriptors (e.g. using SIFT)
   - **Feature Matching:** Match features between images to select keypoints to use.
2. **Estimating and Applying Transformations**: one image is transformed in space to match the other
    - **Transformation Estimation:** Compute transformation matrix (e.g. affine) using matched keypoints.
    - **Warping:** Apply transformation to align images.

<img src="img/sift_route.png" alt="sift keypoints and matches"/>

{{</ horizontal >}}
- [SIFT based registration notebook: example_notebooks/sift_example.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/sift_example.ipynb) 

{{< notes >}}
SIFT can be robust and thus can be used for multimodal registration.
{{</ notes >}}

---

## Technique: Model Based (Pose Estimation)

{{< notes >}}
In cases where many images need to be registered to the same space and pre-known features can be identified, a model-based registration pipeline can be applied.
When the relationship of the distances between the features are pre-known, similar graph-based methods can be used.
Deap learning based approaches can perform well on those tasks with minimal training data.
{{</ notes >}}

{{< horizontal >}}

1. **Predefined Feature Detection**: e.g. pose estimation.
   - **Manual selection of features**
   - **Annotation of training data**
   - **Deep learning landmark detection**
     - Model selection 
     - training 
     - prediction of landmark locations on all images of the dataset
2. **Estimating and Applying Transformations** using the detected landmarks.

<img src="img/wing_landmarks.png" alt="wing landmarks model"/><img src="img/wing_registration.png" alt="wing landmarks model"/>

{{</ horizontal >}}

{{< notes >}}
DeepLabCut is a tracking tool that is open-source and offer great models that can be used for pose estimation and predefined feature detection.
{{</ notes >}}

---

<h2>Challenges & Considerations</h2>

{{< horizontal >}}

- **Method Selection**:
  - Match image type (e.g., multimodal) to appropriate method
- **Transformation Type**:
  - Fit transformation to deformation (e.g., rigid vs. non-rigid)
- **Preprocessing**:
  - Denoising, intensity correction, rescaling, applying filters
  - In hard cases - Use extrinsic information (e.g., physical landmarks)

![](img/edge_detection.png)

{{</ horizontal >}}

- Image source - Erik Meijering: [https://www.youtube.com/watch?v=ecu8kreTwYM](https://www.youtube.com/watch?v=ecu8kreTwYM)

---

{{< horizontal >}}

## Image Registration Guideline

![Image Registration Guideline](img/flowchart.png)

{{</ horizontal >}}

---

## Software Tools for Image Registration

{{< notes >}}
Overview of common tools, libraries, and plugins for image registration.
{{</ notes >}}

- **Fiji/ImageJ**
  - Popular plugins: **Feature Extraction**, **Warpy** (QPath), **TrakEM2**, **Register Virtual Stack Slices**
- **Python Libraries**
  - **OpenCV** (C++), **scikit-image**
- **[Elastix](https://elastix.dev/index.php)**
  - ITKElastix (C++) is a powerful open-source tool (standalone or as a python package) for  intensity-based registration.
- **[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut)**
  - Open-source deep learning based pose estimation and model based feature detection (and tracking).

<br>

- VoltRon: R package that includes an interactive GUI for image registration.  
[https://bioinformatics.mdc-berlin.de/VoltRon/index.html](https://bioinformatics.mdc-berlin.de/VoltRon/index.html)
- SIFT based image registration Python package:   
[https://gitlab.com/ida-mdc/image-registration-tool](https://gitlab.com/ida-mdc/image-registration-tool)

---

## Thank You!

##### Thanks for participating. Please feel free to reach out with any questions.

{{< horizontal >}}
![](img/people/hi-support-staff.png)

![](img/logos/hi.png)
{{</ horizontal >}}

Contact:&nbsp;&nbsp;&nbsp;&nbsp; **ella.bahry@mdc-berlin.de**&nbsp;&nbsp;&nbsp;&nbsp;**support@helmholtz-imaging.de**

Presentation template: Deborah Schmidt - [3d Data Visualization Workshop](https://ida-mdc.gitlab.io/workshops/3d-data-visualization/)




