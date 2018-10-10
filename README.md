# Create a Japanese Anime Face by GAN
Can you image one day machine paint out an anime girl face by itself? You will trust this point by this project. Our model is implementing Pytorch's GAN to do such stuff. We train the adversial network by a new dataset and generate a bunch of good-quality picture. The whole project has three steps: crawling images, crop images, and train GAN by processed images. Thus, there are three .py files needed to run (crawler_module.py, face detector.py, AnimeGAN.ipynb). By runing those in order, GAN will generate a bunch pictures like here.

![alt text](https://github.com/Hierifer/AnimeGAN/blob/master/anime1.jpeg)
![alt text](https://github.com/Hierifer/AnimeGAN/blob/master/anime2.jpeg)
![alt text](https://github.com/Hierifer/AnimeGAN/blob/master/anime3.jpeg)

## Getting Started
The project bases on python 3.6 and Pytorch. Running it requires all packages from PREREQUISITES. 

### Prerequisites
* Python 3.6
* MXNET
* CUDA
* selenium
* openCV

## Running the demo

## Built With

## Author
* **Teng Hu** - *Initial work FrameWork & Data* - Email: thu4@dons.usfca.edu
* **Zijia Chen** - *Initial work Network* - Email: zic138@ucsd.edu

## Acknowledgments
