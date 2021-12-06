
# class_id center_x center_y width height

# mapping label to number
import os
import shutil

class_mapping = {"Car" : 0,
                 "Van" : 1,
                 "Truck": 2}
# image size
image_w = 1242
image_h = 375


def mapping_frame2img(frame):
    return(str(frame).zfill(5))

def check_dir(dir_path): # if dir exist, remove it
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)

with open('info.txt','r') as f:
    info = f.readlines()
    #info_dict : dictionary
    #{'trackID' : Label}
    info_dict={'0':0}
    for i in info[1:]:
        elements = i.split()
        info_dict[elements[0]] = class_mapping[elements[1]]
        #print(elements)
        #print(info_dict)
    #print(info_dict['0']) #car = 0
    #print(info_dict['89']) #van = 1
with open('bbox.txt','r') as f:
    lines= f.readlines()
    line_buffer = []
    for line in lines[1:]:
        #print(line)
        elements = line.split()
        frame = elements[0]
        cameraID = elements[1]
        trackID = elements[2]
        xmin = float(elements[3])
        xmax = float(elements[4])
        ymin = float(elements[5])
        ymax = float(elements[6])
        # bbox = {
        #      "xmin":xmin,
        #      "xmax":xmax,
        #      "ymin":ymin,
        #      "ymax":ymax
        # }
        bbox = {
             "x":(xmax+xmin)/2,
             "y":(ymax+ymin)/2,
             "w":xmax-xmin,
             "h":ymax-ymin
        }
        nom_bbox ={
            "x" : bbox["x"]/image_w,
            "y" : bbox["y"]/image_h,
            "w" : bbox["w"]/image_w,
            "h" : bbox["h"]/image_h
        }

        #for test
        # nom_bbox ={
        #     "x" : xmin,
        #     "y" : xmax,
        #     "w" : ymin,
        #     "h" : ymax
        # }
        #print(bbox)
        #print(nom_bbox)
        #print(mapping_frame2img(frame))
        #line_buffer.append("{} {:.3f} {:.3f} {:.3f} {:.3f}".format(info_dict[trackID],nom_bbox["x"],nom_bbox["y"],nom_bbox["w"],nom_bbox["h"]))
        line_test ="{} {:.3f} {:.3f} {:.3f} {:.3f}".format(info_dict[trackID],nom_bbox["x"],nom_bbox["y"],nom_bbox["w"],nom_bbox["h"])
        dir_name = os.path.join("frames","rgb","Camera_"+cameraID)#("labels", "Camera_"+frame)
        save_file_name =os.path.join(dir_name, "rgb_"+mapping_frame2img(frame)+".txt")
        print(save_file_name)
        if not(os.path.isdir(dir_name)):
            os.makedirs(os.path.join(dir_name))
        print(line_test, file=open(save_file_name, 'a'))
        #save_file_name = os.path.join("labels.txt")
    #print("\n".join(line_buffer), file= open(save_file_name, 'w'))

    #def save_file()