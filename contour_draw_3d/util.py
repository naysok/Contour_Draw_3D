class Util():


    def blend_affine_abcdef(self, mat0, mat1):

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