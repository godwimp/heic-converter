import os
import pillow_heif
from PIL import Image

def convert_heic_to_jpg():
    """
    Convert HEIC files in the current directory to JPG format.
    """
    # Ensure pillow_heif is registered to handle HEIC files
    pillow_heif.register_heif_opener()
    
    # Counter for successful and failed conversions
    conversion_count = 0
    error_count = 0
    
    # Get the current directory
    current_dir = os.getcwd()
    
    # Iterate through all files in the current directory
    for filename in os.listdir(current_dir):
        # Full path to the current file
        file_path = os.path.join(current_dir, filename)
        
        # Check if the file is a HEIC image
        if filename.lower().endswith('.heic'):
            try:
                # Open the HEIC image
                with Image.open(file_path) as img:
                    # Create the new filename
                    jpg_filename = f"{os.path.splitext(filename)[0]}_converted.jpg"
                    jpg_path = os.path.join(current_dir, jpg_filename)
                    
                    # Convert and save as JPG
                    img.convert('RGB').save(jpg_path, 'JPEG')
                
                # Print debug information
                print(f"Successfully converted: {filename} -> {jpg_filename}")
                conversion_count += 1
            
            except Exception as e:
                # Print error if conversion fails
                print(f"Error converting {filename}: {str(e)}")
                error_count += 1
    
    # Final summary
    print("\nConversion Summary:")
    print(f"Total HEIC files converted: {conversion_count}")
    print(f"Conversion errors: {error_count}")

def main():
    # Run the conversion
    convert_heic_to_jpg()

if __name__ == "__main__":
    main()