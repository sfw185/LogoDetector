from subprocess import call
import glob
import sys
import os

def get_url():
  if len(sys.argv) < 2:
    sys.exit("Please pass in a video URL to download")

  url = sys.argv[1]

  if not url.startswith('http://') and  not url.startswith('https://'):
    sys.exit('Please pass in a valid video URL to download')

  return url

def download(url):
  print 'Downloading {0}'.format(url)
  call(['youtube-dl', '--prefer-ffmpeg', '--no-playlist', '-oinput/%(title)s.%(ext)s', url])

def detect_logos():
  print 'Can\'t do this yet'
