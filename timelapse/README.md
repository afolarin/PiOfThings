#using avconv to create a timelapse with non-zero prefixed input image numbering
#i.e. 1,2,3...300 rather than 0001,0002,...300.respectively image%00d.jpg rather than obased image%03d.jpg)
avconv -r 10 -i cat-spy_%00d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4

if using a padded numbering system then use e.g. for 3 prefix padded zeros:
avconv -r 10 -i cat-spy_%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4

