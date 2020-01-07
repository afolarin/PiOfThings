Camera notes
============


Pi Settings
-----------
Increase the memory available to the GPU from 128 to 256 on the pi configuration>>performance [memory]

*Tip*: If you want a continuous camera preview it is unfortunately not exitable. To exit camera preview use `Ctrl+Alt+t` to get a new active terminal (hidden behind the preview, which you can then blindly type `pkill python3` or similar to kill the preview)

Pi Camera CLI
-------------
grab a preview without recording, also configure the different effects modes and exposure modes
```sh
raspistill --imxfx colourswap -t 60000 --rotation 270
raspistill --imxfx none --exposure nightpreview -t 60000 --rotation 270
```

Grab a still
-------------
```sh
raspistill -o Desktop/image.jpg
```

Grab a raw video
----------------
```sh
raspivid -o Desktop/video.h264
```


Python PiCamera package
-----------------------
*docs* https://picamera.readthedocs.io/en/release-1.13/

- Set resolution max (2592x1944) 
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/8 .
Note framerate of 15 caveat...

- Consistent exposure image sequence (esp. for timeseries)
https://picamera.readthedocs.io/en/release-1.13/recipes1.html#capturing-consistent-images

- Low lighting settings (needs tweaking)
https://picamera.readthedocs.io/en/release-1.13/recipes1.html#capturing-in-low-light

- Various methods for image series capture
  - https://picamera.readthedocs.io/en/release-1.13/recipes1.html#capturing-timelapse-sequences
  - https://projects.raspberrypi.org/en/projects/cress-egg-heads


Using avconv for timelapse sequence video collation
---------------------------------------------------
https://projects.raspberrypi.org/en/projects/cress-egg-heads/10
```sh
avconv -r 10 -i image%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4
```
this uses zero prefix padded numbers.

To create a timelapse with non-zero prefix padded numbered files
i.e. 1,2,3...300 rather than 0001,0002,...300.respectively image%00d.jpg rather than obased image%03d.jpg)
```sh
avconv -r 10 -i cat-spy_%00d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4
```

Composite Image generation
--------------------------
Using Python PIL (pillow) package to generate a Composite Image
https://pythontic.com/image-processing/pillow/alpha-composite.

PIL Image class provides two options here (see above link) blend() and alpha_composite()
[see here:](composite-img/pil-composite.py)

Using ImageMagick 
- Composite Func
https://imagemagick.org/script/composite.php
- Blend Func
https://imagemagick.org/script/command-line-options.php#blend

Playback (raw video .h256)
--------
raw video format player
playing on pi3 .h256 raw video  (on pi4 the vlc works but not pi3)
see https://www.raspberrypi.org/documentation/usage/video/
using omxplayer
```sh
omxplayer video.h256
```
convert to mpg
```sh
ffmpeg -r 30 -i video.h264 -c:v copy video.mp4
```
