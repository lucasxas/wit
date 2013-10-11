import Image, ImageEnhance, os
from os.path import join

def batch():
    infolder = os.getcwd()
    p = str(raw_input('Type the watermark\'s position (1 to 5, default: 5): '))
    if not p: p = 5
    p = int(p)
    watermark = str(raw_input('Type the watermark\'s file name (including the .png or .jpg): '))
    if not watermark: watermark = "watermark.png"
    outfolder = os.getcwd()+"/output/"
    mark_dir = infolder+"/"+watermark
    mark = Image.open(mark_dir)
    for root, dir, files in os.walk(infolder):
        if watermark in files: files.remove(watermark)
        for name in files: 
            try:
                im = Image.open(join(root, name))
                layer = Image.new('RGBA', im.size, (0,0,0,0))               
                if im.mode != 'RGBA':
                    im = im.convert('RGBA')
                position = getPos(im, mark, p)
                layer.paste(mark, position)
                if not os.path.exists(outfolder): os.makedirs(outfolder)
                Image.composite(layer, im, layer).save( join(outfolder, name))
            except Exception, (msg):
                print ""
 
def getPos(ima, mar, pos):
    if pos == 1:
        return (50, 50)
    elif pos == 2:
        return (ima.size[0]-(mar.size[0]) -50, 50)
    elif pos == 3:
        return ((ima.size[0]-mar.size[0])/2 -25, (ima.size[1]-mar.size[1])/2 -25)
    elif pos == 4:
        return (50, ima.size[1]-(mar.size[1])-50)
    else:
        return (ima.size[0] - mar.size[0] - 50, ima.size[1]-mar.size[1] - 50)
        
if __name__ == '__main__':
    batch()
