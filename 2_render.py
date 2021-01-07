import time
import math

from contour_draw_3d import image_processing, util

ut = util.Util()
im = image_processing.ImageProcessing()


################################################################################


prj_name = "bunny_offset"


### WINDOWS 10
dir_path = "C:\\Users\\ysoky\\Documents\\Contour_Draw_3D\\"
prj_path = dir_path + "_prj_\\" + prj_name + "\\"


DIR_SRC = prj_path + "image_0_src\\"
DIR_AFF = prj_path + "image_1_affine_transformation\\"
DIR_REN = prj_path + "image_2_render\\"


IMAGE_SIZE = (800, 800)
RENDER_SIZE = 1000

################################################################################


time_0 = time.time()


### Prepare Project Foloder
ut.prepare_prj_dir(dir_path, prj_name)

### Get File Count
count = ut.get_file_count(DIR_SRC)

for i in range(count):

    ### Format
    index = "%04d"%(int(i))
    index_before = "%04d"%(int(i - 1))

    aff_ = DIR_AFF + "image_{}.png".format(index)
    ren_ = DIR_REN + "image_{}.png".format(index)
    ren_before = DIR_REN + "image_{}.png".format(index_before)

    if i >= 0:
        img_render = im.run_render(aff_, ren_before, count, i, RENDER_SIZE)
        im.export_image(img_render, ren_)

time_1 = time.time()


################################################################################

print("Time_01 : {}Sec".format(time_1 - time_0))