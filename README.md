![alt tag](http://wiki.winehq.org/wiki/winehq/img/PythonPowered.png)    Pyrecognize 
===========

Face recognition using OpenCV and Python.

Pyrecognize takes the feed from a webcam and labels the detected faces with the best match.

The training data consists of a root directory (./faces) and a subdirectory for each subject, with multiple images each. All of images must be of the same resolution.

When training the database, it takes 50 photos of the subject, using the webcam.

The main OpenCV functions used by Pyrecognize are detectMultiScale (face detection) and createFisherFaceRecognizer (face recognition).

Based on facerec_video.cpp from the OpenCV documentation. Only tested in OS X Mavericks with Python 2.7.6.

Usage
-----

##### Unix
To train the database:
```bash
./facerec train Name
```
To recognize faces:
```bash
./facerec
```
##### Windows
To train the database:
```bash
train.py Name
```
To recognize faces:
```bash
facerec.py
```

Press Esc to exit.

Installation
------------

After installing OpenCV (see below), download [pyrecognize](https://github.com/noahingham/pyrecognize/archive/master.zip), unzip it and run the executable. In Windows, or to use the training feature, you will have to run it from the command line.

Installing OpenCV:

##### OS X - Macports
```bash
sudo port install opencv +python27
wget https://github.com/noahingham/pyrecognize/archive/master.zip
```

##### Debian/Ubuntu - apt
```bash
sudo apt-get install numpy python-opencv
wget https://github.com/noahingham/pyrecognize/archive/master.zip
```

##### Fedora - yum
```bash
yum install numpy opencv*
wget https://github.com/noahingham/pyrecognize/archive/master.zip
```

##### Windows
Download [Python](http://python.org/ftp/python/2.7.3/python-2.7.3.msi), [Numpy](http://sourceforge.net/projects/numpy/files/NumPy/1.6.1/numpy-1.6.1-win32-superpack-python2.7.exe/download)
and [OpenCV](http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.1/OpenCV-2.4.1.exe/download), and install them in that order. When OpenCV prompts for a folder, enter C:\\.
Now, copy everything in C:\opencv\build\python\x86\2.7\ to C:\Python27\Lib\site-packages\\.



Preview
------------

![alt tag](http://i.imgur.com/l3l9ie0.png)

