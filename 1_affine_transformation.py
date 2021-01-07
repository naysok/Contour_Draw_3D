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

IMAGE_SIZE = (800, 800)

ROT_UNIT = 90
ROT_COUNT = 2
### rotate = ROT_UNIT * ROT_COUNT


################################################################################


time_0 = time.time()


### Prepare Project Foloder
ut.prepare_prj_dir(dir_path, prj_name)

### Get File Count
count = ut.get_file_count(DIR_SRC)

### Define Matrix for Render
mat_aff = im.define_matrix_for_render(IMAGE_SIZE)
# print("Matrix_Render :", mat_aff)


for i in range(count):

    ### Format
    index = "%04d"%(int(i))

    src_ = DIR_SRC + "image_{}.png".format(index)
    aff_ = DIR_AFF + "image_{}.png".format(index)


    # if i == 420:
    if i >= 0:
        
        ### Open
        img = im.open_image(src_)

        ### (1) Rotation
        img_rot = im.rotate_image(img, ROT_UNIT * ROT_COUNT)
        # img_rot.show()
        
        ### (2) Affine Transform
        img_eddited = im.run_transform(img_rot, IMAGE_SIZE, mat_aff)

        # img_eddited.show()
        im.export_image(img_eddited, aff_)


time_1 = time.time()


################################################################################

print("Time_01 : {}Sec".format(time_1 - time_0))