import sys
import os
from PIL import Image
import shutil
import datetime


def main():
    print(str(sys.argv))
    if(len(sys.argv) < 2):
        print("please run file as follow python main.py sourceFile row col")
        return
    stickFile = sys.argv[1]
    row = int(sys.argv[2])
    col = int(sys.argv[3])
    print(os.path.dirname(os.path.abspath(__file__)))

    convertSpriteSheetToGif(stickFile, row, col)


def convertSpriteSheetToGif(stickFile, row, col):
    color_white = (255, 255, 255, 0)
    if(os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "/splitFiles") == True):
        shutil.rmtree(os.path.dirname(
            os.path.abspath(__file__)) + "/splitFiles")
    os.mkdir("splitFiles")
    if(os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "/outputs") == False & os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/outputs") == False):
        os.mkdir(os.path.dirname(
            os.path.abspath(__file__)) + "/outputs")
    fullPath = os.path.dirname(os.path.abspath(
        __file__)) + "/inputs/" + stickFile
    spriteSheet = Image.open(fullPath)
    gifWidth = spriteSheet.width / col
    gifHeight = spriteSheet.height / row
    count = 0
    output = []
    for y in range(row):
        for x in range(col):
            cropX = x * gifWidth
            cropY = y * gifHeight

            frame = spriteSheet.crop(
                (cropX, cropY, cropX+gifWidth, cropY+gifHeight))
            frame.thumbnail((gifWidth, gifHeight), Image.ANTIALIAS)
            offset_x = max((gifWidth - frame.size[0]) / 2, 0)
            offset_y = max((gifHeight - frame.size[1]) / 2, 0)
            pasteOffset = (offset_x, offset_y)
            finalFrame = Image.new(mode='RGBA', size=(
                gifWidth, gifHeight), color=color_white)

            finalFrame.paste(frame, pasteOffset)
            finalFrame.save("splitFiles/{}.png".format(count))
            output.append(finalFrame)
            count += 1
    output[0].save(os.path.dirname(os.path.abspath(__file__)) + "/outputs/" + datetime.datetime.now().strftime("%Y%m%d%H%M%f") + ".gif",
                   save_all=True,
                   append_images=output[1:],
                   duration=100,
                   transparency=255,
                   loop=0)
    print("convert successfully")


if __name__ == "__main__":
    main()
