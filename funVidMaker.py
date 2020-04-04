
# import os
# import sys

from copy import copy
import numpy as np
import proglog
from tqdm import tqdm

from moviepy.editor import *
from moviepy.video.fx.resize import resize
from pygame import *


clips_array = []
def vid_merge(clips, newname, nfps):
    for c in clips:
        clip = VideoFileClip(c)
        clips_array.append(clip)
        
    nsize = (clips_array[0].w, clips_array[0].h)    
    nclip = concatenate([cl for cl in clips_array], method="chain")
    nclip.resize(nsize).write_videofile(newname, audio=True, fps=nfps)
    nclip.close()

nVidName = "merge01.mp4"
vid_merge(["vid/MITRAPIK2.mp4","vid/asgcomp.mp4"], nVidName, 20)    
prevVid = VideoFileClip(nVidName)
prevVid.preview()

