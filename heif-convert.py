import os
import sys
from PIL import Image
import pillow_heif
import numpy as np
from skimage.metrics import structural_similarity as ssim
import cv2
import argparse

def calculate_image_quality_loss(original, converted):
    """
    Calculate quality loss between original and converted images using SSIM.
    Returns percentage of quality preserved (100 - loss%).
    """
    # Convert images to grayscale for SSIM calculation
    original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    converted_gray = cv2.cvtColor(converted, cv2.COLOR_BGR2GRAY)
    
    # Calculate SSIM score
    score = ssim(original_gray, converted_gray)
    
    # Convert to percentage (100% means identical)
    quality_preserved = score * 100
    return quality_preserved

def convert_heif(input_path, output_format):
    """
    Convert HEIF images to specified format and analyze quality loss.
    """
    # Register HEIF opener with Pillow
    pillow_heif.register_heif_opener()
    
    # Create output directory
    parent_dir = os.path.dirname(input_path)
    parent_name = os.path.basename(parent_dir)
    output_dir = os.path.join(parent_dir, f"{parent_name}-{output_format}")
    os.makedirs(output_dir, exist_ok=True)
    
    # Get list of HEIF files
    heif_files = [f for f in os.listdir(input_path) if f.lower().endswith(('.heic', '.heif'))]
    
    if not heif_files:
        print("No HEIF/HEIC files found in the directory.")
        return
    
    print(f"Found {len(heif_files)} HEIF/HEIC files to convert...")
    
    for file in heif_files:
        input_file = os.path.join(input_path, file)
        output_file = os.path.join(output_dir, f"{os.path.splitext(file)[0]}.{output_format}")
        
        try:
            # Open and convert HEIF image
            heif_image = Image.open(input_file)
            
            # For PNG, use direct conversion
            if output_format.lower() == 'png':
                heif_image.save(output_file, format='PNG')
                quality_preserved = 100.0  # PNG is lossless
            
            # For JPEG, try different quality settings
            elif output_format.lower() in ['jpg', 'jpeg']:
                # Convert to RGB if necessary
                if heif_image.mode != 'RGB':
                    heif_image = heif_image.convert('RGB')
                
                # Start with maximum quality
                heif_image.save(output_file, format='JPEG', quality=100)
                
                # Calculate quality loss
                original = cv2.imread(input_file)
                converted = cv2.imread(output_file)
                quality_preserved = calculate_image_quality_loss(original, converted)
            
            print(f"Converted {file} -> {os.path.basename(output_file)}")
            print(f"Quality preserved: {quality_preserved:.2f}%")
            print(f"Quality loss: {100 - quality_preserved:.2f}%")
            print("-" * 50)
            
        except Exception as e:
            print(f"Error converting {file}: {str(e)}")
            continue

def main():
    parser = argparse.ArgumentParser(description='Convert HEIF images to other formats')
    parser.add_argument('format', choices=['png', 'jpg', 'jpeg'], 
                       help='Output format (png, jpg, or jpeg)')
    args = parser.parse_args()
    
    # Use current directory as input path
    current_dir = os.getcwd()
    
    print(f"Converting HEIF images in {current_dir} to {args.format}")
    convert_heif(current_dir, args.format)

if __name__ == "__main__":
    main()