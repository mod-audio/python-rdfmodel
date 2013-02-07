#!/usr/bin/env python

from lv2 import Bundle
from pprint import pprint as pp

invada = Bundle('/usr/lib/lv2/invada.lv2')
pp(invada.data['plugins'])
