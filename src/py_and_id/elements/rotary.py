''' Rotarys, meters, and lamp elements '''

import math

from .elements import Element2Term, gap
from .twoterm import resheight
from ..segments import Segment, SegmentCircle, SegmentText
from .. import util

class Rotary(Element2Term):
    ''' Generic pump element '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        end = kwargs.get("end", (0, 0))
        self.segments.append(Segment([(0, 0), gap, (0.25, -0.5), (0.15, -0.7), (0.9, -0.7), (0.8, -0.5), gap, end]))
        self.segments.append(SegmentCircle((0.5, 0), 0.5))
        


class Pump(Rotary):
    ''' Generic pump element '''
    def __init__(self, *d, **kwargs):
        super().__init__(end=(1.75, 0.35), *d, **kwargs)
        self.segments.append(Segment([(-0.5, 0), (0.5, 0), gap,
                                       (0.5, 0.5), (1.1, 0.5), (1.1, 0.2), 
                                       (1, 0.2), (1.1, 0.2), (1.1, 0.35), (1.75, 0.35)
                                       ], arrow="->"))


class PumpV(Rotary):
    ''' Voltage Rotary '''
    def __init__(self, *d, **kwargs):
        super().__init__(end=(0.9, 1.25), *d, **kwargs)
        self.segments.append(Segment([(-0.5, 0), (0.5, 0), gap,
                                       (1, 0.2), (1, 0.70), (0.65, 0.7), (0.65, 0.5), (0.65, 0.7), (0.9, 0.7), (0.9, 1.25)
                                       ], arrow="->"))
       


class RotaryI(Rotary):
    ''' Current Rotary '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment([(.25, 0), (.75, 0)], arrow='->'))


class RotarySin(Rotary):
    ''' Rotary with sine '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        sin_y = util.linspace(-.25, .25, num=25)
        sin_x = [.2 * math.sin((sy-.25)*math.pi*2/.5) + 0.5 for sy in sin_y]
        self.segments.append(Segment(list(zip(sin_x, sin_y))))


class RotaryPulse(Rotary):
    ''' Pulse Rotary '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        sq = .15
        x = .4
        self.segments.append(Segment(
            [(x, sq*2), (x, sq), (x+sq, sq), (x+sq, -sq),
             (x, -sq), (x, -sq*2)]))


class RotaryTriangle(Rotary):
    ''' Triangle Rotary '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment([(.4, .25), (.7, 0), (.4, -.25)]))


class RotaryRamp(Rotary):
    ''' Ramp/sawtooth Rotary '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment([(.4, .25), (.8, -.2), (.4, -.2)]))


class RotarySquare(Rotary):
    ''' Square wave Rotary '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment([(.5, .25), (.7, .25), (.7, 0),
                                      (.3, 0), (.3, -.25), (.5, -.25)]))


class RotaryControlled(Element2Term):
    ''' Generic controlled Rotary '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment([(0, 0), (.5, .5), (1, 0),
                                      (.5, -.5), (0, 0), gap, (1, 0)]))
        self.params['theta'] = 90


class RotaryControlledV(RotaryControlled):
    ''' Controlled voltage Rotary '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        plus_len = .2
        self.segments.append(Segment([(.25, -plus_len/2),
                                      (.25, plus_len/2)]))  # '-' sign
        self.segments.append(Segment([(.75-plus_len/2, 0),
                                      (.75+plus_len/2, 0)]))  # '+' sign
        self.segments.append(Segment([(.75, -plus_len/2),
                                      (.75, plus_len/2)]))  # '+' sign


class RotaryControlledI(RotaryControlled):
    ''' Controlled current Rotary '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment([(.25, 0), (.75, 0)], arrow='->'))


batw = resheight*.75
bat1 = resheight*1.5
bat2 = resheight*.75


class BatteryCell(Element2Term):
    ''' Cell '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment([(0, 0), gap, (batw, 0)]))
        self.segments.append(Segment([(0, bat1), (0, -bat1)]))
        self.segments.append(Segment([(batw, bat2), (batw, -bat2)]))


class Battery(Element2Term):
    ''' Battery '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment([(0, 0), gap, (batw*3, 0)]))
        self.segments.append(Segment([(0, bat1), (0, -bat1)]))
        self.segments.append(Segment([(batw, bat2), (batw, -bat2)]))
        self.segments.append(Segment([(batw*2, bat1), (batw*2, -bat1)]))
        self.segments.append(Segment([(batw*3, bat2), (batw*3, -bat2)]))


class Solar(Rotary):
    ''' Solar Rotary '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        cellw = resheight*.5
        cellw2 = cellw + .15
        cellx = .4
        self.segments.append(Segment([(cellx, cellw),
                                      (cellx, -cellw)]))
        self.segments.append(Segment([(cellx+.2, cellw2),
                                      (cellx+.2, -cellw2)]))
        self.segments.append(Segment([(0, 0), (cellx, 0), gap,
                                      (cellx+.2, 0), (1, 0)]))
        self.segments.append(Segment([(1.1, .9), (.8, .6)], arrow='->',
                                          arrowwidth=.16, arrowlength=.2))
        self.segments.append(Segment([(1.3, .7), (1, .4)], arrow='->',
                                          arrowwidth=.16, arrowlength=.2))


class MeterV(Rotary):
    ''' Volt meter '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(SegmentText((.5, 0), 'V'))


class MeterI(Rotary):
    ''' Current Meter (I) '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(SegmentText((.5, 0), 'I'))


class MeterA(Rotary):
    ''' Ammeter '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(SegmentText((.5, 0), 'A'))


class MeterOhm(Rotary):
    ''' Ohm meter '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(SegmentText((.5, 0), r'$\Omega$'))


class Lamp(Rotary):
    ''' Incandescent Lamp '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        a = .25
        b = .7
        t = util.linspace(1.4, 3.6*math.pi, 100)
        x = [a*t0 - b*math.sin(t0) for t0 in t]
        y = [a - b * math.cos(t0) for t0 in t]
        x = [xx - x[0] for xx in x]  # Scale to about the right size
        x = [xx / x[-1] for xx in x]
        y = [(yy - y[0]) * .25 for yy in y]
        self.segments.append(Segment(list(zip(x, y))))


class Neon(Rotary):
    ''' Neon bulb '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        cellw = resheight
        cellx = .4
        self.segments.append(Segment([(cellx, cellw), (cellx, -cellw)]))
        self.segments.append(Segment([(cellx+.2, cellw), (cellx+.2, -cellw)]))
        self.segments.append(Segment([(0, 0), (cellx, 0), gap,
                                      (cellx+.2, 0), (1, 0)]))
        self.segments.append(SegmentCircle((cellx-.15, .2), .05, fill=True))
