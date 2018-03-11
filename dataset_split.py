import glob
import shutil
import numpy as np
from PIL import Image
import math

classes = ['aceriform',
'acicular',
'cordate',
'deltoid',
'elliptic',
'falcate',
'flabellate',
'lanceolate',
'linear',
'oblancceolate',
'oblong',
'obovate',
'ovate',
'spathulate',
'subulate',
'tulip']

apex = ['acuminate',
        'apiculate',
        'obtuse',
        'acute',
        'mucronate',
        'round',
        'bilobed',
        'emarginate']

base = ['acute',
        'cordate',
        'obtuse',
        'oblique',
        'hastate',
        'attenuate',
        'truncate']

folder = "/Users/pokkang/Documents/dataset/leaves_flavia_oriented_800_600/full/"
apexfolder = "/Users/pokkang/Documents/dataset/leaves_flavia_oriented_800_600/apex/"
basefolder = "/Users/pokkang/Documents/dataset/leaves_flavia_oriented_800_600/base/"

for ii in apex:
    arr = []
    for file in glob.iglob(apexfolder+'full/' + ii + '/*.jpg'):
        arr.append(file)
    nparr = np.array(arr)
    count = nparr.size
    eighty = int(math.floor(count*0.8))
    twenty = int(math.ceil(count*0.2))
    idx = np.hstack((np.ones(eighty), np.zeros(twenty)))
    np.random.shuffle(idx)
    train = nparr[idx == 1]
    test = nparr[idx == 0]
    #
    # print(train)
    # print(test)
    c = 0
    for i in train:
        # print(i)
        shutil.copyfile(i, apexfolder+'train/'+ii+'/'+ str(c) + '.jpg')
        c += 1
    x = 0
    for i in test:
        # print(i)
        shutil.copyfile(i, apexfolder+'test/' + ii + '/' + str(x) + '.jpg')
        x += 1

            #
    # print(arr)