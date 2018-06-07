from subprocess import call
import sys

if len(sys.argv) < 2:
  sys.exit("Please pass in a video URL to parse")

videoUrl = sys.argv[1]
print 'Downloading {0}'.format(videoUrl)

call(['youtube-dl', '--prefer-ffmpeg', '--no-playlist', '-oinput/%(title)s.%(ext)s', videoUrl])