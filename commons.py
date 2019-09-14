import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import cv2
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, models
from PIL import Image
import torchvision.transforms as transforms
from collections import OrderedDict


def get_model(filepath):

    checkpoint = torch.load('project_checkpoint.pth', map_location='cpu')
    # checkpoint = 'project_checkpoint.pth'
    # if checkpoint['arch'] == 'vgg16':

    model = models.vgg16(pretrained=True)

    for param in model.parameters():
        param.requires_grad = False
        # else:
        #     print("Architecture not recognized.")

    model.class_to_idx = checkpoint['class_to_idx']

    classifier = nn.Sequential(OrderedDict([('fc1', nn.Linear(25088, 5000)),
                                            ('relu', nn.ReLU()),
                                            ('drop', nn.Dropout(p=0.5)),
                                            ('fc2', nn.Linear(5000, 102)),
                                            ('output', nn.LogSoftmax(dim=1))]))

    model.classifier = classifier

    model.load_state_dict(checkpoint['model_state_dict'])
    print('Model Returned')
    return model


def get_tensor(image_bytes, file):
    my_transforms = transforms.Compose([transforms.Resize(255), transforms.CenterCrop(
        224), transforms.ToTensor(), transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    # image = Image.open(io.BytesIO(image_bytes))
    image = Image.open('static/' + file.filename)
    return my_transforms(image).unsqueeze(0)
