# High-resolution iterative defocus deblurring in real-world scenarios via score-based diffusion model

Defocus blur commonly arises from the cameras' depth-of-field limitations.Here, a novel high-resolution iterative defocus deblurring method for real scenes driven by score-based diffusion model is proposed. This method involves establishing a score network by learning the score function of focused images at different noise levels and employing a reverse-time stochastic differential equation (SDE) to iteratively construct high-quality images.


## Training and deblurring Process

1. Defocus deblurring Workflow
<div align="center"><img src="https://github.com/yqx7150/HIDD-DM/blob/main/fig1.jpg"> </div>



##  Network Structure

1. Structure diagram of NCSN network  
<div align="center"><img src="https://github.com/yqx7150/HIDD-DM/blob/main/fig2.jpg"> </div>



## Deblurring Images process

1. Defocus images from NanChang university   
<div align="center"><img src="https://github.com/yqx7150/HIDD-DM/blob/main/fig3.jpg"> </div>


## Other Related Projects

* Accelerated model-based iterative reconstruction strategy for sparse-view photoacoustic tomography aided by multi-channel autoencoder priors  [<font size=5>**[Paper]**</font>](https://onlinelibrary.wiley.com/doi/10.1002/jbio.202300281)  [<font size=5>**[Code]**</font>](https://github.com/yqx7150/PAT-MDAE)

* Sparse-view reconstruction for photoacoustic tomography combining diffusion model with model-based iteration  [<font size=5>**[Paper]**</font>](https://www.sciencedirect.com/science/article/pii/S2213597923001118)  [<font size=5>**[Code]**</font>](https://github.com/yqx7150/PAT-Diffusion)

* Unsupervised disentanglement strategy for mitigating artifact in photoacoustic tomography under extremely sparse view  [<font size=5>**[Paper]**</font>](https://www.sciencedirect.com/science/article/pii/S2213597924000302?via%3Dihub)  [<font size=5>**[Code]**</font>](https://github.com/yqx7150/PAT-ADN)

* Score-based generative model-assisted information compensation for high-quality limited-view reconstruction in photoacoustic tomography  [<font size=5>**[Paper]**</font>](https://www.sciencedirect.com/science/article/pii/S2213597924000405)  [<font size=5>**[Code]**</font>](https://github.com/yqx7150/Limited-view-PAT-Diffusion)

* Generative model for sparse photoacoustic tomography artifact removal  [<font size=5>**[Paper]**</font>](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12745/1274503/Generative-model-for-sparse-photoacoustic-tomography-artifact-removal/10.1117/12.2683128.short?SSO=1)

* PAT-public-data from NCU  [<font size=5>**[Code]**</font>](https://github.com/yqx7150/PAT-public-data)

* GAID-PAT  [<font size=5>**[Code]**</font>](https://github.com/yqx7150/GAID-PAT)
