# beaglecar
This is an attempt to convert a freescale race car using BeagleBone blue

Dependencies:
Check requirements.txt

1. 3D stand was created by Kenrick Tan (from Temple University)

2. Machine Learning Car was created by Kendrick Tan (from Australia) [https://github.com/kendricktan/suiron]

2. Install tensorflow [https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases]

```
sudo apt update && sudo apt upgrade
sudo apt install python-opencv python3-dev libhdf5-dev \
    libfreetype6-dev pkg-config gfortran python-dev python3-virtualenv \
    python3-venv python3-pip python-pip \
    libblas3 liblapack3 liblapack-dev libblas-dev build-essentials 
```
#1. Install Tensorflow [about 20 mins]
```
git clone https://github.com/3keepmovingforward3/tf-1.1.0-cp35.git 
cd tf-1.1.0-cp35 && wget -c https://github.com/3keepmovingforward3/tf-1.1.0-cp35/raw/master/tensorflow-1.1.0-cp35-cp35m-linux_armv7l.whl
sudo pip3 install --user tensorflow-1.1.0-cp36-cp36m-linux_armv7l.whl 
```

#3. Install other package according to requirement.txt, but you will need to make sure you have enough swapping space [roughly 9 hours...]
```
cd ~
git clone https://github.com/lbaitemple/beaglecar
cd ~/beaglecar
sudo dd if=/dev/zero of=/swapfile bs=1M count=1024 
sudo mkswap /swapfile 
sudo swapon /swapfile
sudo python3 -m pip install --ignore-installed -r requirements.txt

```


# Suiron
### Machine Learning for RC Cars 

## Prediction visualization (green = actual, blue = prediction)
![](https://thumbs.gfycat.com/DarlingForkedAcaciarat-size_restricted.gif)

## Click the video below to see it in action!
[![IMAGE ALT TEXT](http://img.youtube.com/vi/tFwCyHdAWf0/0.jpg)](https://youtu.be/tFwCyHdAWf0 "Machine Learning Car")

## Dependencies
#### __Python 2.7__ was chosen as it was supported by all the libraries used at the time
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-opencv python-dev

export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
sudo pip install --upgrade $TF_BINARY_URL

sudo pip install -r requirements.txt
```

## Collecting data
```
python collect.py
```

## Visualizing collected data
```
python visualize_collect.py
```

## Training data
```
python train.py
```

## Visualizing predicted data
```
python visualize_predict.py
```

# References

Blog Post detailing how the hardware and software communicate - [Communicating between RC Car and the On-board Computer - Jabelone](http://jabelone.com.au/blog/make-autonomous-car-code-included/)


Communication between hardware and software repo - [car-controller](https://github.com/jabelone/car-controller)

Neural Network architecture was based on NVIDIA's Self-driving car paper - [End-To-End Learning for Self-Driving Cars](https://arxiv.org/pdf/1604.07316v1.pdf)
