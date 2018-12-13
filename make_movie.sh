# $1 Is the input file names
# $2 is the output file name
# $3 is the frame rate
# $4 is the padding around the numbers i.e for 01 $4=2 001 $4=3

ffmpeg -r $3 -f image2 -s 1920x1080 -i $1"%d.png" -vcodec libx264 -crf 25  -pix_fmt yuv420p $2.mp4 -vf scale=1280:720
