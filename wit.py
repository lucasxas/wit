import Image, ImageEnhance, os
from os.path import join

def batch():
	infolder = os.getcwd()
	watermark = str(raw_input('Type the watermark\'s file name (including the .png or .jpg): '))
	if not watermark: watermark = "watermark.png"
	outfolder = os.getcwd()+"/output/"
	if not os.path.exists(outfolder): os.makedirs(outfolder)
	mark_dir = infolder+"/"+watermark
	mark = Image.open(mark_dir)
	for root, dir, files in os.walk(infolder):
		if watermark in files: files.remove(watermark)
		for name in files:        
			try:
				im = Image.open(join(root, name))
				if im.mode != 'RGBA':
					im = im.convert('RGBA')
				layer = Image.new('RGBA', im.size, (0,0,0,0))
				position = (im.size[0]-(mark.size[0]*2), im.size[1]-(mark.size[1]*2))
				layer.paste(mark, position)
				Image.composite(layer, im, layer).save( join(outfolder, name))
			except Exception, (msg):
				print ""
 
if __name__ == '__main__':
    batch()