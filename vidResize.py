
# import os
# import sys

from copy import copy
import numpy as np
import proglog
from tqdm import tqdm

from moviepy.editor import *
from moviepy.video.fx.resize import resize
from pygame import *

dirpath = str("vid" + "/")

clip0 = VideoFileClip( dirpath +  "MITRAPIK2.mp4")

display = (clip0.w, clip0.h)

clip1 = VideoFileClip(dirpath + "asgcomp.mp4")
nclip = concatenate([clip0, clip1], method="chain")
nclip.resize(display).write_videofile('newvid.mp4', audio=True)

nclip.close()

# nclip = clip1.fx(resize, clip1, clip0.size)
# clip1.resize(display).preview()

# nclip.write_videofile('cliprz1a.mp4', audio=True, fps=20)

# nclip.close()


# clip1.write_videofile('vidrz.mp4', audio=True)

#txt_clip = ( TextClip("MITRA PIK2",fontsize=70,color='white').set_position('center').set_duration(10) )

# finalclip = CompositeVideoClip([clip])

# finalclip = concatenate([clip0, clip1], method="chain")
# finalclip.write_videofile("Combine.mp4", audio=True, fps=20)


# finalclip.close()


