from PIL import Image
import numpy as np

a = np.asarray(Image.open(r'C:\Users\Jhon117\Desktop\TOOLS\68766284_p0.png').convert('L')).astype('float')

depth = 10.         #Ԥ�����ֵΪ10��ȡֵ��Χ0-100
grad = np.gradient(a)
grad_x,grad_y = grad        #��ȡx��y������ݶ�ֵ
grad_x = grad_x*depth/100
grad_x = grad_y*depth/100       #������ȵ���x��y������ݶ�ֵ
A =np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

vec_el = np.pi/2.2
vec_az = np.pi/4.
dx = np.cos(vec_el)*np.cos(vec_az)      #��λ�����ڵ�ƽ���ϵ�ͶӰ����
dy = np.cos(vec_az)*np.sin(vec_az)      #dx,dy,dz�ǹ�Դ��x/y/z����Ӱ��̶�
dz = np.sin(vec_el)

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)
b = b.clip(0,255)

im = Image.fromarray(b.astype('uint8'))
im.save(r'C:\Users\Jhon117\Desktop\117.jpg')