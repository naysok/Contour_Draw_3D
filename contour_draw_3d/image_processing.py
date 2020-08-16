import math
from PIL import Image, ImageDraw, ImageOps, ImageEnhance

class ImageProcessing():


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


    def oparete_rgba_channel(self, img):

        r, g, b = img.split()

        img_r = ImageEnhance.Contrast(r)
        rr = img_r.enhance(3)

        img_new = Image.merge("RGBA", (rr, rr, rr, rr))
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


    def affine_transform(self, img, mat):
        img_aft = img.transform(img.size, Image.AFFINE, mat)
        return img_aft


