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
    frameLength = int(sys.argv[4])
    print(os.path.dirname(os.path.abspath(__file__)))

    convertSpriteSheetToGif(stickFile, row, col, frameLength)


def convertSpriteSheetToGif(stickFile, row, col, frameLength):
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
    alpha = spriteSheet.getchannel('A')
    spriteSheet = spriteSheet.convert('RGB').convert(
        'P', palette=Image.ADAPTIVE, colors=255)

    mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
    spriteSheet.paste(255, mask)
    gifWidth = spriteSheet.width / col
    gifHeight = spriteSheet.height / row
    alpha.save("splitFiles/alpha.png")
    count = 0
    output = []
    isDone = False
    for y in range(row):
        for x in range(col):
            cropX = x * gifWidth
            cropY = y * gifHeight

            frame = spriteSheet.crop(
                (cropX, cropY, cropX+gifWidth, cropY+gifHeight))

            frame.save("splitFiles/{}.png".format(count))
            frame.info['transparency'] = 255
            output.append(frame)
            count += 1
            if(count == frameLength):
                isDone = True
                break
        if(isDone == True):
            break

    output[0].save(os.path.dirname(os.path.abspath(__file__)) + "/outputs/" + datetime.datetime.now().strftime("%Y%m%d%H%M%f") + ".gif",
                   save_all=True,
                   append_images=output[1:],
                   duration=100,
                   disposal=2,
                   loop=0)
    print("convert successfully")


if __name__ == "__main__":
    main()
