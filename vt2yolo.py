import os

class_mapping = {"Car" : 0,
                 "Van" : 1,
                 "Truck": 2}
image_w = 1242
image_h = 375

# 파일 불러오기
path = './'
# 현재 경로에 있는 파일 목록
file_list = os.listdir(path)
#print(file_list)
# 파일 목록 중 텍스트 파일 리스트 저장
txt_list = [file for file in file_list if file.endswith('.txt')]
#print(txt_list)

def mapping_frame2img(frame):
    return(str(frame).zfill(5))

def Convert(txt, file_value):
    with open(txt, 'r') as f:
        lines = f.readlines()  # for save lines
        for line in lines[1:]:
            elements = line.split()

            frame = elements[0]
            label = elements[21]

            left = elements[6]
            right = elements[8]
            top = elements[7]
            bottom = elements[9]

            xmin = float(left)
            xmax = float(right)
            ymin = float(top)
            ymax = float(bottom)
            #print(frame+' '+label+' '+str(class_mapping[label])+' '+left+' '+right+' '+top+' '+bottom)

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
            # print(nom_bbox)
            line_output ="{} {:.3f} {:.3f} {:.3f} {:.3f}".format(class_mapping[label],nom_bbox["x"],nom_bbox["y"],nom_bbox["w"],nom_bbox["h"])
            #print(line_output)
            dir_name = os.path.join(file_value[0],file_value[1]) # ex) 0001/15-deg-left
            save_file_name = os.path.join(dir_name, mapping_frame2img(frame) +"."+ file_value[2])
            #print(save_file_name)
            if not(os.path.isdir(dir_name)):
                os.makedirs(os.path.join(dir_name))
            print(line_output, file = open(save_file_name, 'a'))
for txt in txt_list:
    #print(txt) #0001_15-deg-left.txt
    file_value = txt.replace('.','_')
    #print(file_value) #0001_15-deg-left_txt
    file_value = file_value.split('_')
    #print(file_value) #['0001', '15-deg-left', 'txt']

    Convert(txt, file_value)


