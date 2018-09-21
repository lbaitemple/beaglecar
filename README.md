# beaglecar
This is an attempt to convert a freescale race car using BeagleBone blue

1. 3D stand was created by Kenrick Tan (from Temple University)


2. Machine Learnign Car was created by Kendrick Tan (from Australia) [https://github.com/kendricktan/suiron]

2. Install tensorflow [https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases]

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-opencv python3-dev libhdf5-dev
sudo apt-get install libfreetype6-dev pkg-config
sudo apt-get install libblas3 liblapack3 liblapack-dev libblas-dev
git clone https://github.com/lbaitemple/beaglecar
cd beaglecar
sudo python3 -m pip install --ignore-installed -r requirements.txt

wget https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases/download/v1.1.0/tensorflow-1.1.0-cp34-cp34m-linux_armv7l.whl
mv tensorflow-1.1.0-cp34-cp34m-linux_armv7l.whl tensorflow-1.1.0-cp36-cp36m-linux_armv7l.whl
sudo pip3 install tensorflow-1.1.0-cp36-cp36m-linux_armv7l.whl 
```
