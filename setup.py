from distutils.core import setup, Extension
import os

# change compiler to gcc
os.environ['CC'] = 'gcc'

src_dir = 'src'