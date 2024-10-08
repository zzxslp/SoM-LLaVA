# :pencil: [COLM-2024] List Items One by One: A New Data Source and Learning Paradigm for Multimodal LLMs
*Empowering Open-Source Multimodal LLMs with Set-of-Mark Prompting and Improved Visual Reasoning Ability.*


**List Items One by One: A New Data Source and Learning Paradigm for Multimodal LLMs** [[Paper](https://arxiv.org/abs/2404.16375)] [[HF Model](https://huggingface.co/zzxslp/som-llava-v1.5-13b)] <br>

:mega: **Note:** Our new dataset is complementary to existing training sources, add it to your train set and boost your multimodal LLMs with Set-of-Mark prompting and improved general capacity! No cost at inference time!

## :fire: News
* [08/20] [BLIP-3](https://www.arxiv.org/abs/2408.08872) is out! Our dataset is used in the finetuning stage of BLIP-3 to boost performance!
* [07/10] Our paper is accepted at [COLM-2024](https://colmweb.org), see you in Philly!
* [04/26] Thanks [AK](https://x.com/_akhaliq/status/1783715007366099318) and [HF daily papers](https://huggingface.co/papers) for featuring our work!
* [04/25] Our paper is on arxiv! [[Paper](https://arxiv.org/abs/2404.16375)]
* [04/23] Models and datasets of SoM-LLaVA are released! [[HF Model](https://huggingface.co/zzxslp/som-llava-v1.5-13b)] [[Dataset](https://huggingface.co/datasets/zzxslp/SoM-LLaVA)] 


## :scroll: Contents
- [Results](#bar_chart-results)
- [Dataset](#seedling-SoM-dataset)
- [Model Weights](#cake-model-checkpoints)
- [Showcases](#dango-showcases)
- [Training](#mushroom-training)
- [Using SoM](#snowflake-notes-for-using-SoM)
- [LLaVA on Huggingface](#blush-using-llava-in-hf)


## :bar_chart: Results
<table>
    <tr>
        <td>Method</td>
        <td>GQA</td>
        <td>POPE</td>
        <td>MME</td>
        <td>MMB</td>
        <td>SEED-I</td>
        <td>LLaVA-Wild</td>
        <td>MM-VET</td>
    </tr>
    <tr>
        <td>LLaVA-1.5-7B</td>
        <td>62.0</td>
        <td> 85.9 </td>
        <td> 1464.0</td>
        <td> 65.4 </td>
        <td> 64.8 </td>
        <td> 63.4 </td>
        <td> 30.5 </td>
    </tr>   
    <tr>
        <td><b>SoM-LLaVA-1.5-7B</b></td>
        <td><b>62.7</b></td>
        <td><b>86.5</b></td>
        <td><b>1507.0</b></td>
        <td><b>66.5</b></td>
        <td><b>67.0</b></td>
        <td><b>66.9</b></td>
        <td><b>33.3</b></td>
    </tr>
    <tr>
        <td>LLaVA-1.5-13B</td>
        <td>63.3</td>
        <td>85.9</td>
        <td>1531.3</td>
        <td> 68.9 </td>
        <td>68.2</td>
        <td>70.7</td>
        <td>35.4</td>
    </tr>
    <tr>
        <td><b>SoM-LLaVA-1.5-13B<b></td>
        <td><b>63.8</b></td>
        <td><b>86.6</b></td>
        <td><b>1563.1</b></td>
        <td><b>69.5</b></td>
        <td><b>69.6</b></td>
        <td><b>75.3</b></td>
        <td><b>35.9</b></td>
    </tr>
</table>

:mega: **Note:** 

We get 1% to 6% relative improvements on all MLLM benchmarks, by simply adding 30k SoM data to the visual instruction tuning stage of LLaVA. 

You can optionally feed the model with tagged images during inference to boost performance on some benchmarks, but you can enjoy the performance gain with just standard images!

## :seedling: SoM Dataset 
[[Training data for SoM-LLaVA](https://huggingface.co/datasets/zzxslp/SoM-LLaVA)]

som_llava_mix695k.json: Full SFT data with llava-665k + SoM-30k

som_listing_coco10k.json: listing all items with SoM images.

som_qa_coco20k.json: QA with SoM images. (Note: QA used the same 10k images from listing, with another batch of 10k added.)

som_train2017.zip: A subset of 20k coco images that is annotated with SoM, used in our data construction.


## :cake: Model Checkpoints
We release our main model, SoM-LLaVA trained with LLaVA-665k and SoM-style Listing + QA data.

[[SoM-LLaVA-v1.5-13B-HF](https://huggingface.co/zzxslp/som-llava-v1.5-13b-hf)] (model weights converted into HF format, see usage [below](#blush-using-llava-in-hf))

[[SoM-LLaVA-v1.5-7B](https://huggingface.co/zzxslp/som-llava-v1.5-7b)] (model weights in original LLaVA format, load and eval with [LLaVA](https://github.com/haotian-liu/LLaVA))

[[SoM-LLaVA-v1.5-13B](https://huggingface.co/zzxslp/som-llava-v1.5-13b)] (model weights in original LLaVA format, load and eval with [LLaVA](https://github.com/haotian-liu/LLaVA))

Two additional models for ablation study:

[[SoM-LLaVA-v1.5-13B-listing](https://huggingface.co/zzxslp/som-llava-v1.5-13b-listing)]

[[SoM-LLaVA-v1.5-13B-qa](https://huggingface.co/zzxslp/som-llava-v1.5-13b-qa)]


## :dango: Showcases
<p align="center">
  <img src="examples/case1.png" width="80%"/>
</p>
<p align="center">
  <img src="examples/case2.png" width="80%"/>
</p>
<p align="center">
  <img src="examples/list1.png" width="80%"/>
</p>


## :mushroom: Training
We adopt the training code of [LLaVA](https://github.com/haotian-liu/LLaVA). Please set up environments following the instructions. Currently our data is used in the Visual Instruction Tuning stage.

1. Prepare data

Please download the annotation of the final mixture of our instruction tuning data [som_llava_mix695k.json
](https://huggingface.co/datasets/zzxslp/SoM-LLaVA/resolve/main/som_llava_mix695k.json), which is a mixture of llava_mix665k and 30k SoM data, and download the images from the following datasets:

- COCO: [train2017](http://images.cocodataset.org/zips/train2017.zip)
- COCO: [som_train2017](https://huggingface.co/datasets/zzxslp/SoM-LLaVA/resolve/main/som_train2017.zip)
- GQA: [images](https://downloads.cs.stanford.edu/nlp/data/gqa/images.zip)
- OCR-VQA: [download script](https://drive.google.com/drive/folders/1_GYPY5UkUy7HIcR0zq3ZCFgeZN7BAfm_?usp=sharing), **we save all files as `.jpg`**
- TextVQA: [train_val_images](https://dl.fbaipublicfiles.com/textvqa/images/train_val_images.zip)
- VisualGenome: [part1](https://cs.stanford.edu/people/rak248/VG_100K_2/images.zip), [part2](https://cs.stanford.edu/people/rak248/VG_100K_2/images2.zip)

After downloading all of them, organize the data as follows in your data folder.

```
├── coco
│   ├── train2017
│   └── som_train2017
├── gqa
│   └── images
├── ocr_vqa
│   └── images
├── textvqa
│   └── train_images
└── vg
    ├── VG_100K
    └── VG_100K_2
```

2. Training

After downloading our data (or preparing your own SoM data), train SoM-LLaVA via command line: 

`bash scripts/v1_5/finetune.sh`


## :snowflake: Using SoM
**Note:** Our implementation is improved over the original SoM repo, by removing overlapping regions for each mask (otherwise there will be confilicts/overlaps for tag positions).

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
# download repo and navigate to SoM folder
git clone https://github.com/zzxslp/SoM-LLaVA.git
cd ~/SoM-LLaVA/SoM/

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

# install additional packages
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

## :blush: Using LLaVA in HF
If you would like to load our model in huggingface, here is an example script:

```python
from PIL import Image
import requests
from transformers import AutoProcessor, LlavaForConditionalGeneration

model_path = "zzxslp/som-llava-v1.5-13b-hf"

model = LlavaForConditionalGeneration.from_pretrained(model_path)
processor = AutoProcessor.from_pretrained(model_path)

prompt = "USER: <image>\nWhat's the content of the image? ASSISTANT:"
url = "https://www.ilankelman.org/stopsigns/australia.jpg"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=prompt, images=image, return_tensors="pt")

# Generate
generate_ids = model.generate(**inputs, max_new_tokens=20)
output = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
print (output)
```

Note: to reproduce the results reported in the paper, we recommend using the [official LLaVA repo](https://github.com/haotian-liu/LLaVA) with our [LLaVA-format model](https://huggingface.co/zzxslp/som-llava-v1.5-13b).

## :cat: Citation

If you find our data or model useful for your research and applications, please cite our paper:

```
@article{yan2024list,
  title={List Items One by One: A New Data Source and Learning Paradigm for Multimodal LLMs},
  author={Yan, An and Yang, Zhengyuan and Wu, Junda and Zhu, Wanrong and Yang, Jianwei and Li, Linjie and Lin, Kevin and Wang, Jianfeng and McAuley, Julian and Gao, Jianfeng and others},
  journal={arXiv preprint arXiv:2404.16375},
  year={2024}
}
```


## :beers: Acknowledgments
This project is a collaboration between UC San Diego, Microsoft GenAI, and Microsoft Research, built on top of [SoM](https://github.com/microsoft/SoM) and [LLaVA](https://github.com/haotian-liu/LLaVA). Thank the authors for their contributions to the community!

