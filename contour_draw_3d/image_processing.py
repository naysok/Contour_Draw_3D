import math
from PIL import Image, ImageDraw, ImageOps, ImageEnhance


class ImageProcessing():


    ###########################
    ###                     ###
    ###     I/O + Basics    ###
    ###                     ###
    ###########################


    def open_image(self, path):
        img = Image.open(path)
        return img


    def export_image(self, img, path):
        img.save(path, quality=100)
        print("Export : {}".format(path))
    

    def create_canvas(self, canvas_size):
        new = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
        return new


    def paste_alpha(self, img0, img1, offset):
        
        c = Image.new('RGBA', img0.size, (0, 0, 0, 0))
        c.paste(img1, offset)

        img_alpha = Image.alpha_composite(img0, c)

        return img_alpha


    def modify_rgb(self, img):

        r, g, b, a = img.split()
        img_new = Image.merge("RGBA", (r, r, b, a))
        return img_new


    def oparete_rgba_channel(self, img):

        r, g, b = img.split()

        img_r = ImageEnhance.Contrast(r)
        rr = img_r.enhance(3)

        ### Blue Canvas
        canvas_size = img.size
        c = Image.new('RGBA', canvas_size, (68, 255, 255, 255))
        cr, cg, cb, ca = c.split()

        img_new = Image.merge("RGBA", (cr, cg, cb, rr))
        
        return img_new


    def image_blend_mask(self, mtrl, mask, mask_flip):
        canvas_size = mask.size
        canvas_new = self.create_canvas(canvas_size[0])

        if mask_flip:
            mask = ImageOps.invert(mask)

        img = Image.composite(canvas_new, mtrl, mask)
        return img


    def change_scale(self, img, target_size):
        img_resize = img.resize((target_size, target_size), Image.LANCZOS)
        return img_resize


    ########################################


    ####################
    ###              ###
    ###     Draw     ###
    ###              ###
    ####################


    def draw_line_sibe_clac_size(self, target_size):
        rr = (1 / 6) * math.pi
        canvas_size = int(800.0 / (math.cos(rr) * 2)) * 2
        return canvas_size


    def draw_line_cube(self, img, cube_size, boundary, front, back):

        draw = ImageDraw.Draw(img)
        
        canvas_size = list(img.size)
        cx = canvas_size[0] * 0.5
        cy = canvas_size[1] * 0.5
        rr = (1 / 3) * math.pi
        ss = cube_size * 0.5

        x0 = cx - math.sin(rr) * ss
        x1 = cx + math.sin(rr) * ss
        y0 = cy - ss
        y1 = cy - math.cos(rr) * ss
        y2 = cy + math.cos(rr) * ss
        y3 = cy + ss

        if boundary:
            draw.line((x0, y1, cx, y0), fill=(0, 0, 0, 255))
            draw.line((x1, y1, cx, y0), fill=(0, 0, 0, 255))
            draw.line((x0, y1, x0, y2), fill=(0, 0, 0, 255))
            draw.line((x1, y1, x1, y2), fill=(0, 0, 0, 255))
            draw.line((x0, y2, cx, y3), fill=(0, 0, 0, 255))
            draw.line((x1, y2, cx, y3), fill=(0, 0, 0, 255))

        if front:
            draw.line((x0, y1, cx, cy), fill=(0, 255, 0, 255))
            draw.line((x1, y1, cx, cy), fill=(0, 255, 0, 255))
            draw.line((cx, cy, cx, y3), fill=(0, 255, 0, 255))
        
        if back:
            draw.line((cx, y0, cx, cy), fill=(0, 0, 255, 255))
            draw.line((x0, y2, cx, cy), fill=(0, 0, 255, 255))
            draw.line((x1, y2, cx, cy), fill=(0, 0, 255, 255))

        return img


    ########################################


    #####################################
    ###                               ###
    ###     Affine Transformation     ###
    ###     +                         ###
    ###     Matrix Operateion         ###
    ###                               ###
    #####################################


    def add_matrix_abc_def(self, mat0, mat1):

        a0, b0, c0, d0, e0, f0 = mat0
        a1, b1, c1, d1, e1, f1 = mat1

        aa = a0 * a1 + b0 * d1
        bb = a0 * b1 + b0 * e1
        cc = c0 + c1
        dd = d0 * a1 + e0 * d1
        ee = d0 * b1 + e0 * e1
        ff = f0 + f1

        new_mat = [aa, bb, cc, dd, ee, ff]

        return new_mat


    def affine_transform(self, img, mat):
        img_aft = img.transform(img.size, Image.AFFINE, mat)
        return img_aft


    def define_matrix_for_render(self, img_size):
        
        ### Render

        base_size = img_size
        base_rr = 1 / 4

        ### 0) Scale
        sc = 1.0 / math.sin(math.pi * base_rr)
        mat_scale_0 = [sc, 0, 0, 0, sc, 0]

        ### 1) Rotation
        rr = math.pi * base_rr * (-1)
        mat_rotation = [math.cos(rr), math.sin(rr) * (-1), 0, math.sin(rr), math.cos(rr), 0]

        ### 2) Scale
        sh = 1.0 / math.sin(math.pi * base_rr) * 2.0
        mat_scale_1 = [1.0, 0, 0, 0, sh, 0]

        ### 3) Translate
        vx = (-1) * base_size[0]
        mat_mv = [1.0, 0, vx, 0, 1.0, 0]

        ### Blend Matrix
        mat_0 = self.add_matrix_abc_def(mat_scale_0, mat_rotation)
        mat_1 = self.add_matrix_abc_def(mat_0, mat_scale_1)
        mat_2 = self.add_matrix_abc_def(mat_1, mat_mv)

        return mat_2


    def run_transform(self, img_path, img_size, mat):
        
        ### Run

        ### Open Image
        img_src = self.open_image(img_path)
        w0, h0 = img_src.size
        # print("img_src.size : {} x {}".format(w0, h0))

        ### Resize (800 x 800)
        img_resize = img_src.resize(img_size, Image.LANCZOS)
        w1, h1 = img_resize.size
        # print("img_resize.size : {} x {}".format(w1, h1))

        ### Affine Transform
        img_affine = self.affine_transform(img_resize, mat)
        w2, h2 = img_affine.size
        # print("img_affine.size : {} x {}".format(w2, h2))

        return img_affine


    ########################################


    ######################
    ###                ###
    ###     Render     ###
    ###                ###
    ######################


    def run_render(self, img_path, img_path_before, count, i, render_size):

        ### Open Images
        img_affine = self.open_image(img_path)
        size_affine = img_affine.size
        # print("img_affine.size : {} x {}".format(size_affine[0], size_affine[1]))

        ### MAGIC NUMBER = 1000
        ### render_size = 1000
        BOTTOM = 300
        HEIGHT = 530

        step = HEIGHT / count

        uu = (render_size - size_affine[0]) * 0.5
        vv = (size_affine[1] - BOTTOM) - (step * i)
        paste_uv = (round(uu), round(vv))

        # print(paste_uv)
        
        if i == 0:
            img_canvas = self.create_canvas(render_size)
            img_paste = self.paste_alpha(img_canvas, img_affine, paste_uv)
            return img_paste
        
        ### Down Sampling
        elif i%4 != 0:
            img_canvas = self.open_image(img_path_before)
            return img_canvas

        else:
            img_canvas = self.open_image(img_path_before)
            img_paste = self.paste_alpha(img_canvas, img_affine, paste_uv)
            return img_paste
