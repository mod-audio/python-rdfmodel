#!/usr/bin/env python

import sys
from lv2 import Bundle
from pprint import pprint as pp

if len(sys.argv) < 2:
    print "Usage: demo.py bundle_path"
    print "   ex: demo.py /usr/lib/lv2/invada.lv2"
    sys.exit(1)

bundle = Bundle(sys.argv[1])
pp(bundle.data['plugins'])
