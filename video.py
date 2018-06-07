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
  call([
    'youtube-dl',
    '--prefer-ffmpeg',
    '--no-playlist',
    '-oinput/videos/%(title)s.%(ext)s',
    url]
  )
  return latest_file()

def latest_file():
  files = glob.glob('./input/videos/*')
  latest = max(files, key=os.path.getctime)
  return latest

def delete_frames():
  files = glob.glob('./input/frames/*.jpg')
  for file in files:
    os.remove(file)

def extract_frames(video_path):
  delete_frames()
  os.system('ffmpeg -i "{0}" -vf fps=5 ./input/frames/%05d.jpg'.format(video_path))