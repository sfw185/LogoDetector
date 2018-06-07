## Summary

LogoBot is a rapid image processor that can detect a series of logos in a given video.

## Usage

* Call LogoBot with `python run.py SOME_VIDEO_URL`
* LogoBot will download the given video URL and parse it for logos placed in `input/logos`
* If any of the logos are found, a report will be generated in `output/VIDEO_NAME` and displayed in the console

## Dependencies

* [FFmpeg](https://www.ffmpeg.org/) - audio/video processing
* [OpenCV](https://opencv.org/) - computer vision library
* [youtube-dl](https://rg3.github.io/youtube-dl/) - video downloader for 1000+ sites

## Installation

* `brew install ffmpeg opencv youtube-dl` (on OSX)