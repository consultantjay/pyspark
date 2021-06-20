#Code to Test imports are successful or not
#import sys
try:
    import os
    from pyspark import SparkContext
    print ("Successfully imported Spark Modules")
except ImportError as e:
    print ("Can not import Modules", e)
#    sys.exit(1)
