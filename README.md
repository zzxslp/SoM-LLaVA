# :pencil: List Items One by One: A New Data Source and Learning Paradigm for Multimodal LLMs
*Empowering Multimodal LLMs with Set-of-Mark Prompting and Improved Visual Reasoning Ability.*


**List Items One by One: A New Data Source and Learning Paradigm for Multimodal LLMs** [[Paper](https://arxiv.org/abs/xxx)] [[HF Model](https://huggingface.co/zzxslp/som-llava-v1.5-13b)] <br>

## :fire: News

* [04/23] Models and datasets of SoM-LLaVA are released!


## :seedling: Dataset 

[[Training data for SoM-LLaVA](https://huggingface.co/datasets/zzxslp/SoM-LLaVA)]

som_llava_mix695k.json: Full SFT data with llava-665k + SoM-30k

som_listing_coco10k.json: listing all items with SoM images.

som_qa_coco20k.json: QA with SoM images. (Note: QA used the same 10k images from listing, with another batch of 10k added.)


## :cake: Model Checkpoints
We release our main model, SoM-LLaVA trained with LLaVA-665k and SoM-style Listing + QA data.

[[SoM-LLaVA-v1.5-13B](https://huggingface.co/zzxslp/som-llava-v1.5-13b)]

Two additional models for ablation study:

[[SoM-LLaVA-v1.5-13B-listing](https://huggingface.co/zzxslp/som-llava-v1.5-13b-listing)]

[[SoM-LLaVA-v1.5-13B-qa](https://huggingface.co/zzxslp/som-llava-v1.5-13b-qa)]

## :coffee: Model Training
We adopt the training code of [LLaVA](https://github.com/haotian-liu/LLaVA). Please set up environments following the instructions.

After downloading our data (or preparing your own SoM data), train SoM-LLaVA via command line: 

`bash scripts/v1_5/finetune.sh`

## :snowflake: Notes for using SoM

* Init virtual envs

```bash
# create env. Note: must use 3.10, 3.11 will cause package conflicts.
conda create -n som python=3.10 -y
conda activate som

```

* Install libgeos if there is error installing SEEM

```bash
sudo apt-get update
sudo apt-get install libgeos-c1v5 libgeos-dev

```


* Install segmentation packages

```bash
# dir to SoM repo
cd ~/vlm/SoM/

# install PyTorch
pip3 install torch torchvision torchaudio

# install SEEM
pip install git+https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once.git@package
# install SAM
pip install git+https://github.com/facebookresearch/segment-anything.git
# install Semantic-SAM
pip install git+https://github.com/UX-Decoder/Semantic-SAM.git@package
# install Deformable Convolution for Semantic-SAM
cd ops && sh make.sh && cd ..

# common error fix:
python -m pip install 'git+https://github.com/MaureenZOU/detectron2-xyz.git'

# install my packages
pip install datasets
```

* Download the pretrained models

```bash
sh download_ckpt.sh
```

* Annotate COCO images with SoM

```bash
python annotate_coco.py
```

## :beers: Acknowledgments
This project is built on top of [LLaVA](https://github.com/haotian-liu/LLaVA) and [SoM](https://github.com/microsoft/SoM). Thank authors for their contributions to the community!


<!-- ## Citation

If you find our data or model useful for your research and applications, please cite our paper:

```
``` -->
