# beaglecar
This is an attempt to convert a freescale race car using BeagleBone blue

1. 3D stand was created by Kenrick Tan (from Temple University)


2. Machine Learnign Car was created by Kendrick Tan (from Australia) [https://github.com/kendricktan/suiron]

2. Install tensorflow [https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases]

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-opencv python3-dev libhdf5-dev
sudo apt-get install libfreetype6-dev pkg-config gfortran
sudo apt-get install libblas3 liblapack3 liblapack-dev libblas-dev
https://github.com/lbaitemple/suiron
cd suiron
sudo dd if=/dev/zero of=/swapfile bs=1M count=1024 
sudo mkswap /swapfile 
sudo swapon /swapfile
sudo python3 -m pip install --ignore-installed -r requirements.txt

wget https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases/download/v1.1.0/tensorflow-1.1.0-cp34-cp34m-linux_armv7l.whl
mv tensorflow-1.1.0-cp34-cp34m-linux_armv7l.whl tensorflow-1.1.0-cp36-cp36m-linux_armv7l.whl
sudo pip3 install tensorflow-1.1.0-cp36-cp36m-linux_armv7l.whl 
```
could install h5py first....
```
[wget https://files.pythonhosted.org/packages/22/82/64dada5382a60471f85f16eb7d01cc1a9620aea855cd665609adf6fdbb0d/h5py-2.6.0.tar.gz]
[gunzip -c h5py-2.6.0.tar.gz | tar -xvf -]
[sudo python3 setup.py build_ext --inplace --force]
```
