import os
import sys

def installxcode():
    os.system('xcode-select --install')

def downaldmcports():
    os.system('curl -O https://distfiles.macports.org/MacPorts/MacPorts-2.11.6.tar.bz2')
    os.system('tar xf MacPorts-2.11.6.tar.bz2')

def installmcports():
    os.system('cd MacPorts-2.11.6/')
    os.system('./configure')
    os.system('make')
    os.system('make install')

print('Welcome to Unofficial Auto MacPorts installer\n1.Install with xcode\n2.Install\n0.Exit')
while True:
    act = input()
    if act == 1:
        installxcode()
        downaldmcports()
        installmcports()
    if act == 2:
        downaldmcports()
        installmcports()
    if act == 0:
        sys.exit()
