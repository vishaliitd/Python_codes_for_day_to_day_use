

#https://www.youtube.com/watch?v=Lg4T9iJkwhE&list=PLX-LrBk6h3wSGvuTnxB2Kj358XfctL4BM&index=5

import os

imdir = 'images'
if not os.path.isdir(imdir):
    os.mkdir(imdir)

fidget_folders = [folder for folder in os.listdir('.') if 'fidget' in folder]

n = 0
for folder in fidget_folders:
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir, '{:06}.png'.format(n)))
        n += 1
