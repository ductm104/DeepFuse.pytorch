import glob
import cv2
import numpy as np

over_path = '/Users/minhduc/Desktop/cloned/DeepFuse.pytorch/dataset/images/Bracketed_images/C05/DSC02992.JPG'

under_path = '/Users/minhduc/Desktop/cloned/DeepFuse.pytorch/dataset/images/Bracketed_images/C05/DSC02987.JPG'

over = cv2.imread(over_path)
under = cv2.imread(under_path)

over = cv2.cvtColor(over, cv2.COLOR_BGR2LAB)
under = cv2.cvtColor(under, cv2.COLOR_BGR2LAB)

L1 = over[..., 0]
L2 = under[..., 0]

print(np.mean(L1))
print(np.mean(L2))


dir = '/Users/minhduc/Desktop/cloned/DeepFuse.pytorch/dataset/images/Bracketed_images/C05/'

paths = glob.glob(dir + '*.JPG')
print(len(paths))

for path in np.sort(paths):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    L = img[..., 0]
    print(path[-10:], np.mean(L))
