''' Test for using py_and_id in a script WITHOUT interactive pyplot window  '''
import py_and_id
import py_and_id.elements as elm

py_and_id.use('svg')

with py_and_id.Drawing(backend='svg', file='testcircuit.svg', show=False) as d:
    d.add(elm.Resistor().label('1K'))
    d.add(elm.Capacitor().down())
print(d.get_imagedata('svg'))
