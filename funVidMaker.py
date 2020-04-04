
# import os
# import sys

from copy import copy
import numpy as np
import proglog
from tqdm import tqdm

from moviepy.editor import *
from moviepy.video.fx.resize import resize
from pygame import *

dirInput = "C:/Users/eoktavianus/OneDrive - Agung Sedayu Group/MediaASG/PIK2 MATERIAL/MediaAdsApps/Input/"
dirOutput = "C:/Users/eoktavianus/OneDrive - Agung Sedayu Group/MediaASG/PIK2 MATERIAL/MediaAdsApps/Output/"

clips_array = []
def vid_merge(clips, newname, nfps):
    for c in clips:
        clip = VideoFileClip(c)
        clips_array.append(clip)
        
    # nsize = (clips_array[0].w, clips_array[0].h)    
    # nsize = (120,120)
    nclip = concatenate([cl for cl in clips_array], method="chain")
    nclip.resize(0.10).write_videofile(newname, audio=True, fps=nfps)
    nclip.close()

nVidName = dirOutput + "ProfilePIK2Wtown.mp4"
# vid_merge(["vid/MITRAPIK2.mp4","vid/asgcomp.mp4"], nVidName, 20)    
vid_merge([dirInput + "02 VIDEO PROFILE PIK 2 (FURYCO) - ING - 2019-09-26.mp4", dirInput + "05WATERTOWN.mp4"], nVidName, 20)
# prevVid = VideoFileClip(nVidName)
# prevVid = VideoFileClip(dirInput + "02 VIDEO PROFILE PIK 2 (FURYCO) - ING - 2019-09-26.mp4")
# prevVid.resize(0.10).preview()

