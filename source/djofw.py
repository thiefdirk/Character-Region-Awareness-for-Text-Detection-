from source.models import CRAFT, vgg16_bn

model1 = CRAFT(freeze=False)
model2 = vgg16_bn(pretrained=False, freeze=False)