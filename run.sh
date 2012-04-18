#!/bin/sh
SHELL_PATH=/usr/lib/gnome-shell
LD_PRELOAD=$SHELL_PATH/libgnome-shell.so GI_TYPELIB_PATH=$SHELL_PATH python main.py $@
