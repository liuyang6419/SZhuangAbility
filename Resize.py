from PIL import Image
import os

all = 13547
count = 0
failed_count = 0
outfile = 'resized_images/'
if not (os.path.exists(outfile)):
    os.mkdir(outfile)
infile = 'images/'
for i in range(0, all):
    try:
        img = Image.open(infile+str(i)+'.jpg')
        out = img.resize((300, 300))
        out.save(outfile+str(count)+'.jpg')
        count = count + 1
    except IOError:
        count -= 1
        failed_count += 1
        print('Failed in resizing Image ' + str(i))
        print('Total : 'str(failed_count))
        continue
    
# infile = '/images'
# outlife = '/Resized_images'
# for i in range(0,13260):
#   outfile = os.path.splitext(infile)[0] + ".jpg"
#   if infile != outfile:
#     try:
#       Image.open(infile).save(outfile)
#     except IOError:
#       print "cannot convert", infile