import os

f = open('data/train.txt', 'w')
imagenet_basepath = './../src/tiny-imagenet-200/train/'
for p1 in os.listdir(imagenet_basepath):
  if p1.startswith('n'):
    for p2 in os.listdir(imagenet_basepath + p1 + '/images/'):
      image = os.path.abspath(imagenet_basepath + p1 + '/images/' + p2)
      image.replace('\\', '/')
      f.write(image + '\n')
f.close()
