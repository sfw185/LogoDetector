import image
import video

url = video.get_url()
video_path = video.download(url)
video.extract_frames(video_path)
image.detect_logos()