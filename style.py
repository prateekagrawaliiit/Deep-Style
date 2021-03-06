# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-06 21:48:56
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-06 21:54:32
import argparse
import os
import sys
import time
import re

import numpy as np
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
import torch.onnx

import utils
from transformer_net import TransformerNet
from vgg import Vgg16
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def load_model(modelpath):
    with torch.no_grad():
        style_model = TransformerNet()
        state_dict = torch.load(modelpath)
        # remove saved deprecated running_* keys in InstanceNorm from the checkpoint
        for k in list(state_dict.keys()):
            if re.search(r'in\d+\.running_(mean|var)$', k):
                del state_dict[k]
        style_model.load_state_dict(state_dict)
        style_model.to(device)
        style_model.eval()
        return style_model

def stylize(style_model,content_image,output_image):

    content_image = utils.load_image(content_image)
    content_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])
    content_image = content_transform(content_image)
    content_image = content_image.unsqueeze(0).to(device)

    with torch.no_grad():
        output = style_model(content_image).cpu()
    utils.save_image(output_image, output[0])