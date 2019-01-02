from PIL import Image
import numpy as np

a = np.asarray(Image.open(r'C:\Users\Jhon117\Desktop\TOOLS\68766284_p0.png').convert('L')).astype('float')

depth = 10.         #预设深度值为10，取值范围0-100
grad = np.gradient(a)
grad_x,grad_y = grad        #提取x和y方向的梯度值
grad_x = grad_x*depth/100
grad_x = grad_y*depth/100       #根据深度调整x和y方向的梯度值
A =np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

vec_el = np.pi/2.2
vec_az = np.pi/4.
dx = np.cos(vec_el)*np.cos(vec_az)      #单位光线在地平面上的投影长度
dy = np.cos(vec_az)*np.sin(vec_az)      #dx,dy,dz是光源对x/y/z方向影响程度
dz = np.sin(vec_el)

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)
b = b.clip(0,255)

im = Image.fromarray(b.astype('uint8'))
im.save(r'C:\Users\Jhon117\Desktop\117.jpg')