import argparse
import yaml
import os
import itk
import numpy as np
import matplotlib.pyplot as plt
import tifffile as tif
from scipy.ndimage import zoom
import functools
print = functools.partial(print, flush=True)

# --- Parse command-line args and load YAML configuration ---
parser = argparse.ArgumentParser(description="Elastix Registration Parameters")
parser.add_argument('--config', type=str, required=True, help="Path to config YAML file")
args = parser.parse_args()

with open(args.config, 'r') as f:
    config = yaml.safe_load(f)

fixed_image_path    = config["fixed_image_path"]
moving_image_path   = config["moving_image_path"]
downsample_factor   = config["downsample_factor"]
output_dir          = config.get("output_dir_prefix", "output")

n_resolutions       = config["n_resolutions"]
max_iterations      = config["max_iterations"]
metric              = config["metric"]
initial_step_length = config["initial_step_length"]
min_step_length     = config["min_step_length"]
num_spatial_samples = config["num_spatial_samples"]

output_dir = f'{output_dir}_ds{downsample_factor}_r{n_resolutions}_i{max_iterations}_m{metric}_is{initial_step_length}_ms{min_step_length}_ss{num_spatial_samples}'
os.makedirs(output_dir, exist_ok=True)

# --- Function definitions ---
def display_image_pair(fixed_np, moving_np):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(fixed_np)
    ax[1].imshow(moving_np)
    plt.show()

def set_itk_image_properties(image, spacing=[1.0, 1.0], origin=[0.0, 0.0]):
    image.SetSpacing(spacing)
    image.SetOrigin(origin)

def show_overlay(fixed, result, output_dir, opacity=0.5, cmap='viridis'):
    # Convert images to NumPy arrays
    fixed_np = itk.GetArrayFromImage(fixed) if isinstance(fixed, itk.itkImagePython.itkImageF2) else np.asarray(fixed)
    result_np = itk.GetArrayFromImage(result) if isinstance(result, itk.itkImagePython.itkImageF2) else np.asarray(result)

    # Normalize images
    fixed_np = (fixed_np - np.min(fixed_np)) / (np.max(fixed_np) - np.min(fixed_np))
    result_np = (result_np - np.min(result_np)) / (np.max(result_np) - np.min(result_np))

    plt.figure(figsize=(10, 10))
    plt.imshow(fixed_np, cmap='gray')
    plt.imshow(result_np, cmap=cmap, alpha=opacity)
    plt.axis('off')
    plt.title('Fixed (Gray) + Registered (Color) Overlay')
    plt.savefig(os.path.join(output_dir, "overlay.png"), bbox_inches='tight')
    plt.close()

def show_results_side_by_side(result_im, fixed, output_dir):
    fixed_np = itk.GetArrayFromImage(fixed)
    result_np = itk.GetArrayFromImage(result_im)
    diff = fixed_np - result_np

    fig, ax = plt.subplots(1, 3, figsize=(15, 10))
    ax[0].imshow(result_np)
    ax[0].set_title("Registered")
    ax[1].imshow(fixed_np)
    ax[1].set_title("Fixed")
    ax[2].imshow(diff)
    ax[2].set_title("Difference")
    plt.savefig(os.path.join(output_dir, "side_by_side.png"), bbox_inches='tight')
    plt.close()

def get_elastix_object(n_resolutions=2, 
                       max_iterations=500, 
                       metric='AdvancedMeanSquares', 
                       initial_step_length=10.0, 
                       min_step_length=0.1, 
                       num_spatial_samples=1024):
    parameter_object = itk.ParameterObject.New()
    affine_parameter_map = parameter_object.GetDefaultParameterMap('affine', n_resolutions)
    
    affine_parameter_map['AutomaticTransformInitialization'] = ['true']
    affine_parameter_map['AutomaticTransformInitializationMethod'] = ['GeometricalCenter']
    
    max_iterations_list = [str(max_iterations) for _ in range(n_resolutions)]
    affine_parameter_map['MaximumNumberOfIterations'] = max_iterations_list
    
    affine_parameter_map['MaximumStepLength'] = [str(initial_step_length)]
    affine_parameter_map['MinimumStepLength'] = [str(min_step_length)]
    affine_parameter_map['MinimumMetricDifference'] = ['0.0001']
    affine_parameter_map['NumberOfSpatialSamples'] = [str(num_spatial_samples)]
    affine_parameter_map['Transform'] = ['AffineTransform']
    affine_parameter_map['Metric'] = [metric]
    
    parameter_object.AddParameterMap(affine_parameter_map)
    
    print("Parameter Object Configuration:")
    print(parameter_object)
    return parameter_object

# --- Image loading ---
fixed_np = tif.imread(fixed_image_path)
moving_np = tif.imread(moving_image_path)

# --- Downsample images ---
fixed_np = zoom(fixed_np, 1 / downsample_factor, order=1)
moving_np = zoom(moving_np, 1 / downsample_factor, order=1)

# --- Preprocess images ---
fixed_np = fixed_np.astype(np.float32)
moving_np = moving_np.astype(np.float32)
fixed_np = fixed_np / np.max(fixed_np)
moving_np = moving_np / np.max(moving_np)

# --- Convert to ITK images ---
fixed = itk.GetImageFromArray(np.ascontiguousarray(fixed_np))
moving = itk.GetImageFromArray(np.ascontiguousarray(moving_np))

# --- Set ITK image properties ---
set_itk_image_properties(fixed)
set_itk_image_properties(moving)

# --- Create Elastix parameter object ---
parameter_object = get_elastix_object(
    n_resolutions=n_resolutions,
    max_iterations=max_iterations,
    metric=metric,
    initial_step_length=initial_step_length,
    min_step_length=min_step_length,
    num_spatial_samples=num_spatial_samples
)

# --- Run Elastix registration ---
result_image, result_transform_parameters = itk.elastix_registration_method(
    fixed, moving, parameter_object=parameter_object, log_to_console=True
)

# --- Save output images ---
show_overlay(result_image, fixed, output_dir)
show_results_side_by_side(result_image, fixed, output_dir)

