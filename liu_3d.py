
from matplotlib import colormaps
import numpy as np
import pyvista as pv
colors=colormaps['tab10']


def text_to_3d(text=r'你好',font='Dengxian',resolution=1000,height=10):
    #

    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    import io
    import pyvista as pv
    from pathlib import Path
    plt.style.use('classic')


    plt.figure(figsize=(6, 4))
    plt.text(0,0,s=text,font_properties=font)
    plt.axis('off')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution, bbox_inches='tight', pad_inches=0.1)
    plt.close()  # 关闭图形释放内存
    buf.seek(0)  # 移动指针到缓冲区开头

    # 用 PIL 打开缓冲区中的图像
    pil_img = Image.open(buf)

    numpy_img = np.array(pil_img.convert('L'))

    ind_row,ind_column=np.where(numpy_img<128)
    c_row=np.mean(ind_row)
    c_column=np.mean(ind_column)
    c1=-ind_row+c_row
    c2=ind_column-c_column
    c3=np.zeros_like(ind_row)
    c=np.column_stack((c2,c1,c3)).astype(np.float32)

    data=pv.PolyData(c)
    data.delaunay_2d(alpha=1,inplace=True)
    data.extrude(vector=(0,0,height),capping=True,inplace=True)

    return data


if __name__=='__main__':
    _text_3d=text_to_3d(r'This is a formula $x^2+y^2=\sqrt{z}$')
    _pt=pv.Plotter()

    _pt.add_mesh(_text_3d,style='surface',color=colors(1),show_edges=False)
    _pt.camera_position='xy'
    # pt.show_bounds()
    _pt.show()










