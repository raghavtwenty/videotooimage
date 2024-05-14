#  VIDEO TO IMAGE
_A Python pip package for converting videos to sequential image frames_
<br><br><br>


### 🌟 MILESTONES 🌟
🏆 I published my first PyPI/PIP package. It was used by many of my friends for preprocessing in their ML/Data Science tasks.
<br><br><br>


### AVAILABLE ON PIP
https://pypi.org/project/videotooimage/ <br>

```
pip install videotooimage
```
<br><br>


### PROTOTYPE VIDEO

- PyPI
  
https://github.com/raghavtwenty/videotooimage/assets/126254197/306aef3b-1b84-4a91-8332-5c3efcfd0de8

- Local

https://github.com/raghavtwenty/videotooimage/assets/126254197/cd4b5b5b-1f81-40ee-b51f-3f19da0ce925

<br><br>

### HOW TO EXECUTE

#### Terminal
Python3
```
import videotooimage
result = videotooimage.video_too_image("path/to/video/directory","path/to/output/directory")
print(result)
```
<br><br>


### PURPOSE
- videotooimage is a Python package that provides functionality to convert video files into sequences of images. <br>
- It utilizes the OpenCV library (cv2) to process video files and extract frames.  <br>
- This package is useful for tasks such as video analysis, object detection, and machine learning model training using video data.
<br><br><br>


### FEATURES
- Convert video files (e.g., .mp4, .avi, .mov) into sequences of images.<br>
- Works with various video codecs and formats supported by OpenCV.<br>
- No need to create sub folders for directories manually, It will be created automatically. <br>
- Very useful for machine learning training purposes, the original folder structure is kept as is it.
<br><br><br>


### PROCESSING
1 sec = 1 frame = 1 image file (.jpg format)
<br><br><br>


### END USERS
1. Students <br>
2. ML Engineers <br>
3. Data Scientists <br>
4. Video editors 
<br><br><br>


### OUTPUTS

- PyPI Package <br><br>
![1](https://github.com/raghavtwenty/videotooimage/assets/126254197/2700a29c-dd83-4605-96ae-908434cb5e6f)


- Processing <br><br>
![2](https://github.com/raghavtwenty/videotooimage/assets/126254197/0550a71c-3218-49e1-8145-684bafcc4c15)


- Folder Structure after processing <br><br>
![3](https://github.com/raghavtwenty/videotooimage/assets/126254197/3d088e20-2593-4df4-9f47-06785447d1e3)

<br>

### WORKING
- Folder structure of videos directory (Input) <br>
<pre>
/project
    /videos
        /happy
            person1.mp4
            person2.mp4
            person3.mp4
        /sad
            person1.mp4
            person2.mp4
            person3.mp4
</pre>


- After conversion <br>
Folder structure of output directory <br>
<pre>
/output/folder/
    /v2i_images
        /happy
            person1(frame_number_1).jpg
            person1(frame_number_2).jpg
            person2.mp4
            person3.mp4
            ...
        /sad
            person1(frame_number_1).jpg
            person1(frame_number_2).jpg
            person2.jpg
            person3.jpg
            ... <br>
</pre>
<br><br>


### AUTHOR
Name: Raghava <br>
GitHub: https://github.com/raghavtwenty/ <br>
Email: raghavtwenty@gmail.com<br>
Date Created: March 18, 2024 | Last Updated: May 14, 2024
<br><br><br>


### LICENSE
This package is licensed under the MIT License.
<br><br><br>


### CONTRIBUTIONS
Contributions and feedback are welcome! <br>
Please submit issues or pull requests on GitHub. <br>

GitHub: https://github.com/raghavtwenty/videotooimage/
<br><br>

_END OF README_
