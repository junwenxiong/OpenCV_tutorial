import numpy as np
import matplotlib.pyplot as plt
import flow_vis
import cv2 as cv

# img =  cv.imread("resource/1.jpg")
# flow_uv = np.array(img)
# np.save("resource" + '.npy', flow_uv)
flow_uv = np.load("resource.npy")
print(flow_uv[...,:2].shape)
flow_color = flow_vis.flow_to_color(flow_uv[...,:2], convert_to_bgr=False)


plt.imshow(flow_uv)
plt.imshow(flow_color)
plt.show()



# plt.show()