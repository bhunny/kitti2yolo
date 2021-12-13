import os
import cv2
class_mapping = {
    'Car':0, 'Van':1, 'Truck':2,
                     'Pedestrian':3, 'Person_sitting':4, 'Cyclist':5, 'Tram':6,
                     'Misc':7,'DontCare':7
}
# 파일 목록 읽어 오고 저장
path = './'
file_list = os.listdir(path)

# png 이미지 리스트
png_list = [file for file in file_list if file.endswith('.png')]

def Convert(txt, file_value,image_w, image_h):
    with open(txt, 'r') as f:
        lines = f.readlines()  # for save lines
        for line in lines[0:]:
            elements = line.split()

            label = elements[0]

            left = elements[4]
            right = elements[6]
            top = elements[5]
            bottom = elements[7]

            xmin = float(left)
            xmax = float(right)
            ymin = float(top)
            ymax = float(bottom)
            print(label+' '+str(class_mapping[label])+' '+left+' '+right+' '+top+' '+bottom)

            bbox = {
                "x": (xmax + xmin) / 2,
                "y": (ymax + ymin) / 2,
                "w": xmax - xmin,
                "h": ymax - ymin
            }
            nom_bbox = {
                "x": bbox["x"] / image_w,
                "y": bbox["y"] / image_h,
                "w": bbox["w"] / image_w,
                "h": bbox["h"] / image_h
            }
            print(bbox)
            print(nom_bbox)


            line_output ="{} {:.3f} {:.3f} {:.3f} {:.3f}".format(class_mapping[label],nom_bbox["x"],nom_bbox["y"],nom_bbox["w"],nom_bbox["h"])
            #print(line_output)
            dir_name = os.path.join("labels")
            save_file_name = os.path.join(dir_name, file_value[0]+'.txt') # labels/000001
            #print(save_file_name)
            if not(os.path.isdir(dir_name)):
                os.makedirs(os.path.join(dir_name))
            #for python2
            #f = open(save_file_name,'a')
            #f.write(line_output+"\n")
            #f.close()
            #for python3
            print(line_output, file = open(save_file_name, 'a'))



for png in png_list:
    # 이미지 파일 읽기
    img = cv2.imread(png_list[0])
    image_w = img.shape[1]
    image_h = img.shape[0]
    file_value = png.split('.')
    Convert('labels_org/'+file_value[0]+'.txt', file_value,image_w,image_h)


