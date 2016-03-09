#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

# ['classes', 'clips']
data = np.load('data_styletransfer.npz')
clips   = data['clips']
classes = data['classes']

nb_datapoints = classes.shape[0]
nb_attributes = clips.shape[1] * clips.shape[2]

# Convert to arff

with open('motion_classifcation.arff', 'w') as mc_f:

    mc_f.write('@relation "motion_classification"\n\n')
    
    for i in range(nb_attributes):
        mc_f.write('@attribute att_' + str(i) + ' numeric\n')

    mc_f.write('@attribute class {0,1,2,3,4,5,6,7}\n')

    mc_f.write('\n@data\n')
    for i in range(nb_datapoints):
        attr_class_list = list(clips[i].flatten()) + [classes[i][0]]
        mc_f.write( ",".join(repr(item) for item in attr_class_list))
        mc_f.write('\n')

# ['fast_punching', 'fast_walking', 'jumping', 'kicking', 'normal_walking', 'punching', 'running', 'transitions']
#one_hot_motions = np.zeros(nb_datapoints, 8)
#one_hot_motions[np.arange(nb_datapoints), classes[:,0]] = 1

# ['angry', 'childlike', 'depressed', 'neutral', 'old', 'proud', 'sexy', 'strutting']
#one_hot_styles  = np.zeros(classes.shape[1], 8)
#one_hot_styles[np.arange(nb_datapoints), classes[:,1]] = 1