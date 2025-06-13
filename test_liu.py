from matplotlib import colormaps
import numpy as np
import pyvista as pv
colors=colormaps['tab10']
from liu_3d import text_to_3d

if __name__=='__main__':
    text_3d_1=text_to_3d(r'公式 $x^2+y^2=\sqrt{z}$',height=20)

    pt=pv.Plotter()
    pt.add_mesh(text_3d_1,style='surface',color=colors(1))
    pt.camera_position='xy'
    # pt.show_bounds()
    pt.show()