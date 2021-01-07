import math

from contour_draw_3d import image_processing, util

ut = util.Util()
im = image_processing.ImageProcessing()

################################################################################


prj_name = "cube"


### WINDOWS 10
dir_path = "C:\\Users\\ysoky\\Documents\\Contour_Draw_3D\\"
prj_path = dir_path + "_prj_\\" + prj_name + "\\"


IMAGE_SIZE = (800, 800)


################################################################################


### Calibration ??

### Prepare Project Foloder
ut.mkdir_prj(dir_path, prj_name)
# print(prj_path)

path_1 = prj_path + "cube_line.png"

img = im.create_canvas(1000)

cube_width = im.draw_line_sibe_clac_size(800)
print(cube_width)

im.draw_line_cube(img, cube_width, True, True, True)
# im.draw_line_cube(img, cube_width, False, True, False)


# img.show()
im.export_image(img, path_1)