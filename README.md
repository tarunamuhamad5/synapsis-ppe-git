# Quick Review

-   Using model YOLOV8 medium size as base model
-   please check files synapsis-ppe-version2.pdf as the notebook for build the model
-   please [Google Drive](https://drive.google.com/drive/u/1/folders/1_kxQuXEgH4rnVANn0cZkR51wjgG6fAfr "@embed") to check the example output video using this model.
-   please check folder modeling-process-result. in this folder, the documentation for example output for training, test, and validation data, and also the evaluation of the model attached.

# Running on Colab Notebook

-   please open [Google Drive](https://drive.google.com/drive/u/1/folders/1_kxQuXEgH4rnVANn0cZkR51wjgG6fAfr "@embed") to execute in online Environment
-   please upload your video into validation-video-raw folders
-   change video_name into your file name. check the example below

```
video_path = ('validation-video-raw')
video_name = ("your-video-input.format")
video_path_out = "output-video/{}_out.mp4".format(video_name)
```

-   run the notebook, and your result will be at output-video folder
-   for the note, please change into GPU runtime to accelerate the process.

# Running on Local Machine

## Set Up Environment

-   Create Environment in python 3.10.13 in anaconda
-   Reccomendation Using GPU to acceleration the rendering
-   Install Library from requirement.txt

```
  pip install -r requirements.txt
```

## predict-video.py

-   Copy your video into input-video folders
-   Change the following code with instruction

```
video_path = "input-video/"
video_name = (
    "change-your-video-name.format"
)
video_path_out = "output-video/{}_out.mp4".format(video_name)
```

-   The result will be in folder output-video

## Real-time-Camera.py

-   Run the python code to generate app to use camera and detect the PPE
-   if you want use external camera, please change the code

```
# source = 0 is internal camera, 1 for external camera
result = model(source=1, show=True, conf=0.35, save=True, device=0)
```
