''' Test for using py_and_id in a script with interactive pyplot window  '''
import py_and_id
import py_and_id.elements as elm

#py_and_id.use('svg')

with py_and_id.Drawing(file='cap.svg') as d:
    d.add(elm.Resistor().label('1K'))
    d.add(elm.Capacitor().down())

with py_and_id.Drawing(file='res.svg') as d2:
    d2.add(elm.Diode().fill(True))
