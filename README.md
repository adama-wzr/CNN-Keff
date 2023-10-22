# CNN-Keff
Physics blind CNN model for predicting effective thermal conductivity in 2D images.

Each of the folders is one trained CNN for predicting the effective thermal conductivity of a 128x128 binary image. The file "load_and_predict.py" is an example of how to use the trained models to predict the effective thermal conductivity of one of the example images.

The Python script utilizes one of the folders with the trained models to predict the effective thermal conductivity of the image uploaded, just a brief and simple example of how to use the trained models.

The packages required to run this code are PIL, numpy, Tensorflow/Keras, and os.

If you find this work useful for your research, please cite the publication (pre-proof, will add the actual publication when available):

 - Adam, A., Fang, H., & Li, X. (2023). Effective thermal conductivity estimation using a convolutional neural network and its application in topology optimization. In Energy and AI (p. 100310). Elsevier BV. https://doi.org/10.1016/j.egyai.2023.100310

The training dataset can be found on MendeleyData, using the link below:

Adam, Andre; Li, Xianglin; Fang, Huazhen (2023), “2D Binary Images and Effective Thermal Conductivity CFD Results”, Mendeley Data, V1, doi: 10.17632/454dsrmdyf.1

An updated, ever evolving version of the CFD algorithm can be found in the following GitHub Repository:

https://github.com/adama-wzr/Keff-CFD

 If there are any questions, please reach the corresponding author or one of the other authors via email.
