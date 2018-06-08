from subprocess import call
import cleanup
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
  return latest_video()

def latest_video():
  files = glob.glob('./input/videos/*')
  latest = max(files, key=os.path.getctime)
  return latest

def extract_frames(video_path):
  cleanup.delete_files('./input/frames/*.jpg')
  os.system('ffmpeg -i "{0}" -vf fps=5 ./input/frames/%05d.jpg'.format(video_path))