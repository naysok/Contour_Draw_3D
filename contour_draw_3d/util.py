import os


class Util():


    def get_file_count(self, _dir):

        count = len([name for name in os.listdir(_dir) if os.path.isfile(os.path.join(_dir, name))])
        return count


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