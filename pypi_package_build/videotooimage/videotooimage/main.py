"""
Filename: main.py
Project Name: videotooimage
Title: Videos to image frames
Author: Raghava | Github: @raghavtwenty
Date Created: March 18, 2024 | Last Updated: May 14, 2023
Language: Python | Version : 3.10.14

Purpose :
This program can take the directory of video folder
(even if it has multiple sub folders) traverse the whole path
and create a replicate of the same folder structure and saves
each frame in video (1 sec = 1 frame = 1 image file) to the
new folder structure.
"""

# Importing required libraries
import os
import cv2
from pathlib import Path


# Video to image processing
def image_processing(
    main_video_dir, current_video_folder, current_video_name, output_dir
):
    """
    Caution: Dont use this function directly, It's for internal purpose.

    Usage:
    import videotooimage
    result = videotooimage.video_too_image("path/to/video directory","path/to/output/directory")
    print(result)

    """

    # Path
    current_video = main_video_dir + current_video_folder + current_video_name

    # Read the video from specified path
    video = cv2.VideoCapture(current_video)
    fps = int(video.get(cv2.CAP_PROP_FPS))

    current_frame = 0  # Start frame

    while True:
        # Reading from frame
        ret, frame = video.read()
        if ret:
            # If video is still left continue creating images
            if current_frame % fps == 0:
                current_fps = int(current_frame / fps)
                name = output_dir + current_video_name + str(current_fps) + ".jpg"
                try:
                    # Save current frame as image
                    cv2.imwrite(name, frame)
                except:
                    # Handle invalid frame by logging or skipping it
                    print("Error processing frame", current_frame)
                    pass

            current_frame += 1  # Increment to next frame
        else:
            break
    video.release()  # Close video object


# Create directories and save frames to image files
def video_too_image(input_location, output_location):
    """
    Parameters:
        input_location -> Relative (Full) directory path of videos folder.
        output_location -> Relative (Full) directory path of output folder

    Usage:
    import videotooimage
    result = videotooimage.video_too_image("path/to/video directory","path/to/output/directory")
    print(result)

    Purpose:
        Takes in directory of videos folder and traverses through all sub folders and files. For each video frame a new image will be saved in replicated folder of the original video directory.

    Author: Raghava | GitHub: @raghavtwenty
    """

    print("Processing...")

    # Output folder
    output_dir = output_location + "/v2i_images/"

    # Create a new folder for images
    try:
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
    except OSError:
        return "Error: Creating directory of data"

    try:
        # Traverse through all inner folders and files
        for folder_name, sub_folders, file_names in os.walk(input_location):
            # print("The current folder is " + folder_name)

            # Inner folders
            for sub_folder in sub_folders:
                os.mkdir(output_dir + sub_folder)  # Create folders with same name
                # print("SUBFOLDER OF " + folder_name + ": " + sub_folder)

            # Inner filenames
            for current_filename in file_names:
                current_folder_name = folder_name.split("/")[-1] + "/"
                if current_filename.startswith("."):  # Leave env files and variables
                    continue
                else:
                    # Video to image processing and storage
                    image_processing(
                        input_location,
                        "/" + current_folder_name,
                        current_filename,
                        output_dir + current_folder_name,
                    )
        return f"Processing done, Check the folders : {output_dir}"
    except:
        return f"Folder already exists in the same name in the location: {output_dir}"


# Main
if __name__ == "__main__":

    # User input
    user_input_path = str(input("Enter the video directory path (Absolute path): "))
    user_output_path = str(input("Enter the output directory path (Absolute path): "))
    result = video_too_image(user_input_path, user_output_path)
    print(result)
