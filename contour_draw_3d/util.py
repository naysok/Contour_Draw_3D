import os


class Util():


    def add_matrix_abcdef(self, mat0, mat1):

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
    

    def mkdir_prj(self, dir_path, prj_name):

        ### Check and Create Dirctory
        dirs = []
        prj_path = dir_path + "_prj_\\"

        for i in os.listdir(prj_path):
            dirs.append(i)
        dir_new = prj_path + prj_name

        if prj_name not in dirs:
            os.mkdir(dir_new)
            print("Create Directory : {}".format(prj_name))


    def mkdir_image_0(self, prj_path):

        ### Check and Create Dirctory
        dirs = []
        name = "image_0_src"

        for i in os.listdir(prj_path):
            dirs.append(i)
        dir_new = prj_path + name

        if name not in dirs:
            os.mkdir(dir_new)
            print("Create Directory : {}".format(name))


    def mkdir_image_1(self, prj_path):

        ### Check and Create Dirctory
        dirs = []
        name = "image_1_affine_transformation"

        for i in os.listdir(prj_path):
            dirs.append(i)
        dir_new = prj_path + name

        if name not in dirs:
            os.mkdir(dir_new)
            print("Create Directory : {}".format(name))


    def mkdir_image_2(self, prj_path):

        ### Check and Create Dirctory
        dirs = []
        name = "image_2_render"

        for i in os.listdir(prj_path):
            dirs.append(i)
        dir_new = prj_path + name

        if name not in dirs:
            os.mkdir(dir_new)
            print("Create Directory : {}".format(name))


    def mkdir_image_3(self, prj_path):

        ### Check and Create Dirctory
        dirs = []
        name = "image_3_XXX"

        for i in os.listdir(prj_path):
            dirs.append(i)
        dir_new = prj_path + name

        if name not in dirs:
            os.mkdir(dir_new)
            print("Create Directory : {}".format(name))


    def prepare_prj_dir(self, dir_path, prj_name):

        ### Run (Initialize)
        prj_path = dir_path + "_prj_\\" + prj_name + "\\"
        
        self.mkdir_prj(dir_path, prj_name)
        self.mkdir_image_0(prj_path)
        self.mkdir_image_1(prj_path)
        self.mkdir_image_2(prj_path)
        # self.mkdir_image_3(prj_path)