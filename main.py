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

            alpha = frame.getchannel('A')
            alpha.save("splitFiles/alpha-{}.png".format(count))
            frame = frame.convert('RGB').convert(
                'P', palette=Image.ADAPTIVE, colors=255)

            mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
            frame.paste(255, mask)
            frame.save("splitFiles/{}.png".format(count))
            frame.info['transparency'] = 255
            output.append(frame)
            count += 1
    output[0].save(os.path.dirname(os.path.abspath(__file__)) + "/outputs/" + datetime.datetime.now().strftime("%Y%m%d%H%M%f") + ".gif",
                   save_all=True,
                   append_images=output[1:],
                   duration=100,
                   loop=0)
    print("convert successfully")


if __name__ == "__main__":
    main()
