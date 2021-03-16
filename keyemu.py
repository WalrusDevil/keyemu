import ctypes
import platform as _platform
if _platform.system() == 'Windows':
 emu = ctypes.WinDLL('user32')
elif _platform.system() == 'Linux':
 print("Not Supported")
else:
 print("Not Supported")

"""
Windows Mouse Events
emu.SetCursorPos(X, Y) #Set Mouse Pos #X and Y are an int
emu.mouse_event(0x1, X, Y, 0, 0) #Move Mouse Relative #X and Y are an int
emu.mouse_event(0x8, 0, 0, 0x10000, 0) #Right Down
emu.mouse_event(0x10, 0, 0, 0x10000, 0) #Right Up
emu.mouse_event(0x2, 0, 0, 0x10000, 0) #Left Down
emu.mouse_event(0x4, 0, 0, 0x10000, 0) #Left Up
emu.mouse_event(0x20, 0, 0, 0x10000, 0) #Middle Down
emu.mouse_event(0x40, 0, 0, 0x10000, 0) #Middle Up
"""

"""
Windows Keyboard Events
0x08 Backspace
0x09:Tab
0x0d Enter
0x10 Shift
0x11 Ctr
0x12 Alt
0x14 Caps
0x1b Esc
0x20 Space
0x21 Pg Up
0x22 Pg Down
0x23 End
0x24 Home
0x25 Left
0x26 Up
0x27 Right
0x28 Down
0x2d Insert
0x2e Delete
0x30 0
0x31 1
0x32 2
0x33 3
0x34 4
0x35 5
0x36 6
0x37 7
0x38 8
0x39 9
0x41 a
0x42 b
0x43 c
0x44 d
0x45 e
0x46 f
0x47 g
0x48 h
0x49 i
0x4a j
0x4b k
0x4c l
0x4d m
0x4e n
0x4f o
0x50 p
0x51 q
0x52 r
0x53 s
0x54 t
0x55 u
0x56 v
0x57 w
0x58 x
0x59 y
0x5a z
0x5b Windows
0x60 NumPad0
0x61 NumPad1
0x62 NumPad2
0x63 NumPad3
0x64 NumPad4
0x65 NumPad5
0x66 NumPad6
0x67 NumPad7
0x68 NumPad8
0x69 NumPad9
0x6a NumPad*
0x6b NumPad+
0x6c Separator #Tab?
0x6d NumPad-
0x6e NumPad.
0x6f NumPad/
0x70 f1
0x71 f2
0x72 f3
0x73 f4
0x74 f5
0x75 f6
0x76 f7
0x77 f8
0x78 f9
0x79 f10
0x7a f11
0x7b f12
0x7c f13
0x7d f14
0x7e f15
0x7f f16
0x80 f17
0x81 f18
0x82 f19
0x83 f20
0x84 f21
0x85 f22
0x86 f23
0x87 f24
0x90 NumLock
0x91 ScrollLock
0xa0 LeftShift
0xa1 RightShift
0xa2 LeftCtr
0xa3 RightCtr
0xbb =
0xbc ,
0xbd -
0xbe .
0xbf /
#Use Shift To Get The Alternate Char ex: Shift with 0xbb for +
#Format
emu.keybd_event(X, 0, Y, 0)
emu.GetKeyState(Z) #Z Should Be 0 or 1 If not pressed
Replace X or Z with key value ex: 0xbb for +
Replace Y with 0 for press and 2 for release
"""

###Custom Funcs
def presrel(key): #Replace key with a key value ex: 0xbb for +
 emu.keybd_event(key, 0, 0, 0)
 emu.keybd_event(key, 0, 2, 0)
###
"""
#Example of using GetKeyState loop with keybd_event
while 1 == 1:
 while(emu.GetKeyState(0x58) > 60000):
  emu.keybd_event(0x58, 0, 2, 0) #If You try something like this have the first thing it does to unrelease the key
  emu.keybd_event(0x59, 0, 0, 0)
  emu.keybd_event(0x59, 0, 2, 0)
"""