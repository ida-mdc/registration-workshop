---
title: "Image Registration Workshop"
date: 2025-10-29
draft: false
layout: workshop
author: Ella Bahry
cover: img/registration.png
---

## Helmholtz Imaging
{{< unlisted >}}

##### Helmholtz Imaging is here for you with support units at 3 centers
{{< figure src="img/pipeline.png" >}}

{{< center >}}
{{< logos >}}img/logos/desy.png
img/logos/dkfz.png
img/logos/mdc.png{{< /logos >}}
{{< /center >}}

<br/>
{{< center >}}

**support@helmholtz-imaging.de**
{{< /center >}}


---

## What is Image Registration?

{{< notes >}}
In this workshop, we will explore fundamental concepts and practical techniques for image registration, focusing on applications in microscopy, material science, and earth science.
{{</ notes >}}

<img src="img/registration_big.png" alt="Registration" style="height: 500px; width: auto;">

<h4>Spatial alignment of two or more images.</h4>
 
- It's an essential  step for comparing or integrating data in many scientific fields.


{{< notes >}}
Image registration is the process of aligning multiple datasets into a common coordinate system, enabling accurate comparison and analysis.
{{</ notes >}}

---

## Common needs in research

<img src="img/common_needs.png" style="width: 100%; height: auto;">

---

## Image Registration Aim

![](img/fixed_moving.png)

![](img/fixed_moving_registered.png)

---

## Image Transformation Types

{{< horizontal >}}

<img src="img/transformations.png" style="height: 900px; width: auto;">

<img src="img/affine.png" style="height: 400px; width: auto;">

{{</ horizontal >}}

[Link: example_notebooks/2_transformation_examples.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/2_transformation_examples.ipynb
) 

{{< notes >}}
The type of transformation should be chosen based on the expected deformations in the images.  
It's common to apply a more rough transformation first (e.g. affine), followed by an elastic transformation to correct for local deformations (e.g. TPS).  
But more is not always better, as more complex transformations can lead to overfitting and with each transformation some errors are introduced (due to interpolation).

The transformation matrix can also be used to warp other channels or annotation data such as segmentation labels.  

Rigid transformation requires 2 points, affine 3 points, perspective 4 points, ideally for local deformations require more.
{{</ notes >}}

---

## Local Deformations - Common Approaches

<img src="img/local_deformations.png" style="width: 100%; height: auto;">

---

## Image Interpolation - Reason

- When we transform an image, we need to estimate pixel values at the new coordinates.
- If for example, you transform an image by up-scaling it: 

<img src="img/grids.png" style="height: 500px; width: auto;">

- Interpolation is the process of estimating pixel values from non-integer coordinates.

---

## Image Interpolation - Common Types

{{< unlisted >}}

{{< notes >}}
When you transform an image to a new space, you need to estimate the pixel values at the new locations.
Interpolation is used to estimate pixel values at non-integer coordinates.
{{</ notes >}}

{{< center >}}
<img src="img/interpolation_functions.jpg" style="height: 500px; width: auto;">
<br>
<img src="img/interpolation_weights.png" style="height: 450px; width: auto;">
{{< /center >}}

Image by [Cmglee](https://commons.wikimedia.org/wiki/User:Cmglee), license: CC BY-SA 4.0  
[Link to interpolation weights and examples notebook: example_notebooks/3_interpolation.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/3_interpolation.ipynb
) 

{{< notes >}}
- Interpolation weights demo: For each interpolation type it randomly picks subpixel localization and shows weights of surrounding pixels.
- Example toy image: Shows the effect of different interpolation types on a simple image.
- Example of anti-aliasing when down-sampling.
{{</ notes >}}

---

## Image Interpolation Example
{{< unlisted >}}

<img src="img/interpolation_rotation.png" style="height: 500px; width: auto;">
<img src="img/interpolation_shearing.png" style="height: 500px; width: auto;">

---

## Image Interpolation - Anti-Aliasing in Down-Sampling
{{< unlisted >}}

<img src="img/antialias.png" style="height: 500px; width: auto;">

---

## Image Registration Techniques - Categories

<img src="img/categories.png" style="width: 100%; height: auto;">

---

## Integrated Image Registration Techniques <img src="img/icon_integrated.png" style="float: right; height: 60px !important; width: auto !important; margin: 0 !important;">

{{< unlisted >}}

{{< notes >}}
Introducing registration methods that combine both matching and transformation into one smooth process, simplifying image alignment. 
{{</ notes >}}

<br/><br/>

- **Intensity-Based Registration**
  - Iterative process that optimizes aligned pixel intensity similarities (e.g. **correlation coefficient** or **MSE**).
  
<br/>

- **Mutual Information-Based Registration**
  - Iteratively aligns multimodal images by maximizing the statistical relationship between them.
  
<br/>

- **Frequency Domain Methods**
  - Transforms images into the Fourier space to compute alignment transformations.

---

## Technique: Intensity Based (Correlation Coefficient)

{{< unlisted >}}

![](img/correlation_r45_s1.5.png)
![](img/correlation_r10_s1.1.png)
![](img/correlation_r2_s1.png)
![](img/correlation_r0_s1.png)

{{< notes >}}
[Examples were generated using: example_notebooks/4_correlation_example.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/4_correlation_example.ipynb
)
{{</ notes >}}

---

## Technique: Mutual Information

{{< unlisted >}}

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

- [Mutual Information implementation notebook: example_notebooks/5_mutual_information.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/5_mutual_information.ipynb
) 

---

## ITK / ITKElastix - Common tool

{{< unlisted >}}

- **Elastix / ITKElastix** is a powerful open-source tool for intensity-based image registration, widely used in medical imaging and other fields.
  - It provides a flexible framework for various registration tasks, supporting multiple transformation models and similarity metrics.
  - ITKElastix has a Python interface. ITK + Elastix are C++ native.
  - [ITKElastix toy example: example_notebooks/6_itkelastix_toy_tutorial.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/6_itkelastix_toy_tutorial.ipynb)
- **ANTs** is another popular tool (ITK based) for intensity-based registration, known for its advanced algorithms and versatility in handling different image modalities.
  - It's especially useful for 3D and elastic deformation registration tasks.
  - Originally developed for neuroimaging applications but applicable to other domains as well.
  - Python / R / command line interface.

<br/><br/><br/><br/>

- [ITKElastix link: github.com/InsightSoftwareConsortium/ITKElastix](https://github.com/InsightSoftwareConsortium/ITKElastix)
- [ANTs link: github.com/ANTsX/ANTs](https://github.com/ANTsX/ANTs)
- [ANTsPy (Python) docs: antspy.readthedocs.io](https://antspy.readthedocs.io)

---

## Technique: Phase Correlation (Frequency Domain)

{{< unlisted >}}

<img src="img/phase_corr.png" style="width: 100%; height: auto;">

- Phase correlation does step 3 for **every possible shift at once** (using the Fourier transform), so it is fast. The best match is the shift. No optimizer, no starting guess.
- **Used for:** stitching overlapping microscopy tiles (e.g. Fiji, BigStitcher).
- **Limits:** needs overlap and similar-looking images. Fails on repetitive or low-texture regions.
- Rotation and scale are possible too, by first remapping to log-polar coordinates (Fourier-Mellin).

---

<h2>2 Step Techniques - Feature Detection & Transformation <img src="img/icon_twostep.png" style="float: right; height: 60px !important; width: auto !important; margin: 0 !important;"></h2>

{{< unlisted >}}

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

{{< unlisted >}}

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
- [SIFT based registration notebook: example_notebooks/7_sift_example.ipynb](https://github.com/bellonet/image-registration-workshop/blob/main/example_notebooks/7_sift_example.ipynb) 

{{< notes >}}
SIFT can be robust and thus can be used for multimodal registration.
{{</ notes >}}

---

## Technique: Model Based (Pose Estimation)

{{< unlisted >}}

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

## Deep Learning Based Image Registration

{{< unlisted >}}

- unlike some other vision tasks, deep learning has not completely supplanted classical methods for registration.
- However, deep learning based methods can learn complex patterns and deformations, making them suitable for challenging registration tasks and shine in speed and in leveraging training data.

<h4>VoxelMorph</h4>

{{< horizontal >}}

![](img/voxelmorph.png)

- Uses CNNs to learn spatial transformations between images (2D/3D)
- Image similarity loss + smooth transformation regularization
- Unsupervised. semi-supervised training with anatomical labels
- Training (unsupervised) is still needed - so dataset can't be small
- Offers both affine and elastic registration
- Very fast with good interpretability
- Expected user level is intermediate

{{</ horizontal >}}

Not only medical, the same idea is used on
[seismic surveys](https://doi.org/10.1109/tgrs.2021.3081516) (modified VoxelMorph),
[satellite images](https://doi.org/10.3390/rs13071294) and
[X-ray/neutron images](https://doi.org/10.1364/ao.500442) (similar approach).

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

## Registration Validation

- **Visual inspection first**: overlay the two images with different colormaps and partial opacity, or flip between the fixed and the registered image. Zoom in on small structures.
- **The optimized metric is not a verdict**: validating with the same metric used for the alignment is misleading, since the method already optimized it. Absolute values say little, but comparing runs or steps (before vs. after, affine vs. elastic) is informative.
- **Red flags without ground truth**: the image collapsed or blew up (its area changed massively), almost no overlap is left between registered and target, or (feature-based) only a few matched points, all clustered in one region.
- **Create your own ground truth**: click matching points in both images by hand. Measure their distance after registration. Don't use the same points for the registration itself.
- **Elastic transformations**: look at the deformation (grid or field). It should be smooth, without folds or extreme stretching.
- **Is the error acceptable for your use case?** Decide what accuracy your analysis needs.

{{< notes >}}
Almost no one has ground truth for scientific images, so evaluation means collecting evidence, not getting a number.  
Studies show that image similarity and tissue overlap are unreliable stand-ins for accuracy (Rohlfing 2012, IEEE TMI), and there is no agreed threshold separating a good from a poor deformable result.  
Hand-clicked landmarks are the cheapest ground truth, and they are independent of the registration metric. They must be different points from the ones used to compute the transformation.  
The red flags are cheap numbers: area of the warped image vs. the original (collapse or explosion), fraction of the registered image inside the target, number of matched inliers and how widely they are spread. They catch impossible results, not subtle errors.  
A local similarity map (e.g. mutual information computed in sliding windows) can point to regions worth inspecting, but it should not be used to label regions as failed.  
Folding of an elastic transformation can be checked numerically with the Jacobian determinant of the deformation (zero or negative means folded).
{{</ notes >}}

---

## Image Registration Guideline

<br/><br/>
![](img/flowchart.png)

---

## Summary of Software Tools for Image Registration

{{< notes >}}
Overview of common tools, libraries, and plugins for image registration.
{{</ notes >}}

- **Fiji/ImageJ**
  - Popular plugins: **Feature Extraction**, **Warpy** (QPath), **TrakEM2**, **Register Virtual Stack Slices**
- **Python Libraries**
  - **OpenCV** (C++), **scikit-image**
- **[ITKElastix](https://elastix.dev/index.php)** (C++) is a powerful open-source tool (standalone or as a python package) for  intensity-based registration.
- **[ANTs](https://github.com/ANTsX/ANTs)** Advanced normalization tools (C++) for intensity-based registration - great for local deformations and 3D.
- **[VoxelMorph](https://github.com/voxelmorph/voxelmorph)** Deep Learning based image registration framework (Python, TensorFlow/Pytorch).
- **[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut)** Open-source deep learning based pose estimation and model based feature detection (and tracking).

<br>

- VoltRon: R package that includes an interactive GUI for image registration.  
[https://bioinformatics.mdc-berlin.de/VoltRon/index.html](https://bioinformatics.mdc-berlin.de/VoltRon/index.html)
- SIFT based image registration Python package:   
[https://gitlab.com/ida-mdc/image-registration-tool](https://gitlab.com/ida-mdc/image-registration-tool)

---

## Thank You!

{{< unlisted >}}

**Thanks for participating. Please feel free to reach out with any questions.**

{{< horizontal >}}
![](img/people/hi-staff.png)

![](img/logos/hi.png)
{{</ horizontal >}}

Contact:&nbsp;&nbsp;&nbsp;&nbsp; **ella.bahry@mdc-berlin.de**&nbsp;&nbsp;&nbsp;&nbsp;**support@helmholtz-imaging.de**

Workshop available on: [github.com/ida-mdc/registration-workshop](https://github.com/ida-mdc/registration-workshop)

License: CC BY 4.0  

Thanks to the HIDA team for offering this workshop!  
[https://www.helmholtz-hida.de/en/](https://www.helmholtz-hida.de/en/)  

Thanks to Deborah Schmidt for the template!

{{< notes >}}
This workshop content (slides, non-code images, text) is released under a Creative Commons Attribution 4.0 International License (CC BY 4.0).      
What this means for you:    
You are free to: Share, copy, redistribute, and adapt (remix, transform, and build upon) the material for any purpose, even commercial use.  
You only need to do one thing (Attribution): You must give appropriate credit to the original creator ("Ella Bahry/Helmholtz Imaging") by including a link to the license and indicating if any changes were made.
We encourage you to use, adapt, and share this work!  
{{</ notes >}}


