#!/opt/homebrew/bin/python3

import os
import glob
import shutil
import time
from tqdm import tqdm
from PIL import Image

# https://www.youtube.com/watch?v=_Zzp6SpMm7g

directoryPath:str               = input("경로를 String으로 입력해주세요 : \n")
recursiveType:str               = input("현재 폴더에서만 실행(N), 내부 폴더까지 순회해서 실행(Y) : \n")
targetExtentionType:str         = input("변환할 이미지 형식을 입력해주세요 : \n")
resultExtentionType:str         = input("변환될 결과 이미지 형식을 입력해주세요 : \n")

def getTargetFiles():
    if recursiveType == "Y":
        return glob.glob(os.path.join(directoryPath, "**/*.s" % targetExtentionType), recursive=True)
    elif recursiveType == "N":
        return glob.glob(os.path.join(directoryPath, "**/*.s" % targetExtentionType), recursive=False)
    else:
        raise Exception("폴더 순회 여부 문자가 잘못 입력됨 (Y/N)")

try :
    os.chdir(directoryPath)
    print(os.getcwd())
except OSError as error :
    print(error)
    raise 

list_filepath = getTargetFiles()

print("작업파일 개수 : %d" % list_filepath.count)

for imgItem in tqdm(list_filepath):
    try :
        im = Image.open(imgItem)
        im.save(os.path.splitext(imgItem)[0] + ".%s" % resultExtentionType)
    except Image.UnidentifiedImageError as error:
        print(error)
        raise
    time.sleep(0.1)

exit()