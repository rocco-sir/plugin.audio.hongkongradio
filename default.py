#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcgui
import xbmcplugin
import xbmcaddon

addon = xbmcaddon.Addon()

# URL list
url881 = "https://#"
url903 = "https://#"
url864 = "https://#"
urlrthk1 = "https://rthk.hk/live1.m3u"
urlrthk2 = "https://rthk.hk/live2.m3u"
urlrthk3 = "https://rthk.hk/live3.m3u"
urlrthk4 = "https://rthk.hk/live4.m3u"
urlrthk5 = "https://rthk.hk/live5.m3u"
urlpth = "https://rthk.hk/livepth.m3u"
#
item21 = xbmcgui.ListItem('881 WIP', iconImage='special://home/addons/plugin.audio.hongkongradio/resources/media/881.png')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), url881, item21, isFolder=0)

item22 = xbmcgui.ListItem('903 WIP', iconImage='special://home/addons/plugin.audio.hongkongradio/resources/media/903.png')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), url903, item22, isFolder=0)

item23 = xbmcgui.ListItem('864 WIP', iconImage='special://home/addons/plugin.audio.hongkongradio/resources/media/864.png')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), url864, item23, isFolder=0)     

item24 = xbmcgui.ListItem('RTHK 1, iconImage='special://home/addons/plugin.audio.hongkongradio/resources/media/radio1.png')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), urlrthk1, item24, isFolder=0)     

item25 = xbmcgui.ListItem('RTHK 2', iconImage='special://home/addons/plugin.audio.hongkongradio/resources/media/radio2.png')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), urlrthk2, item25, isFolder=0)   

item26 = xbmcgui.ListItem('RTHK 3', iconImage='special://home/addons/plugin.audio.hongkongradio/resources/media/radio3.png')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), urlrthk3, item26, isFolder=0)   

item27 = xbmcgui.ListItem('RTHK 4', iconImage='special://home/addons/plugin.audio.hongkongradio/resources/media/radio4.png')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), urlrthk4, item27, isFolder=0)   

item28 = xbmcgui.ListItem('RTHK 5', iconImage='special://home/addons/plugin.audio.hongkongradio/resources/media/radio5.png')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), urlrthk5, item28, isFolder=0)   

item29 = xbmcgui.ListItem('PTH', iconImage='special://home/addons/plugin.audio.hongkongradio/resources/media/pth.png')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), urlpth, item29, isFolder=0)   

xbmcplugin.endOfDirectory(pluginhandle)
