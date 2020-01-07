Camera notes
============

Increase the memory available to the GPU from 128 to 256 on the pi configuration>>performance [memory]

#note to exit camera preview use Ctrl+Alt+t to get a focus of the terminal (hidden behind the preview, which you can then exit, ctrl+D or pkill python )

#grab a preview without recording, also configure the different effects modes and exposure modes
raspistill --imxfx colourswap -t 60000 --rotation 270
raspistill --imxfx none --exposure nightpreview -t 60000 --rotation 270

#grab a still
raspistill -o Desktop/image.jpg





#grab a raw video
raspivid -o Desktop/video.h264




#playing on pi3 .h256 raw video  (on pi4 the vlc works but not pi3)
# see https://www.raspberrypi.org/documentation/usage/video/


#using omxplayer
omxplayer video.h256

#confert to mpg
ffmpeg -r 30 -i video.h264 -c:v copy video.mp4


#using avconv to create a timelapse with non-zero prefixed input image numbering
#i.e. 1,2,3...300 rather than 0001,0002,...300.respectively image%00d.jpg rather than obased image%03d.jpg)
avconv -r 10 -i cat-spy_%00d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4

