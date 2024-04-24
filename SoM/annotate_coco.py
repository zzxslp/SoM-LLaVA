# --------------------------------------------------------
# Annotate COCO images with SoM
# --------------------------------------------------------

import os
import gradio as gr
import torch
import argparse
from PIL import Image
import json
from tqdm import tqdm
import traceback

# semantic sam
from semantic_sam.BaseModel import BaseModel
from semantic_sam import build_model
from semantic_sam.utils.dist import init_distributed_mode
from semantic_sam.utils.arguments import load_opt_from_config_file
from semantic_sam.utils.constants import COCO_PANOPTIC_CLASSES
from task_adapter.semantic_sam.tasks import inference_semsam_m2m_auto, prompt_switch

from scipy.ndimage import label
import numpy as np
from datasets import load_dataset

@torch.no_grad()
def inference(image, slider, alpha, label_mode, anno_mode, *args, **kwargs):
    model_name = 'semantic-sam'
    if slider < 1.5 + 0.14:                
        level = [1]
    elif slider < 1.5 + 0.28:
        level = [2]
    elif slider < 1.5 + 0.42:
        level = [3]
    elif slider < 1.5 + 0.56:
        level = [4]
    elif slider < 1.5 + 0.70:
        level = [5]
    elif slider < 1.5 + 0.84:
        level = [6]
    else:
        level = [6, 1, 2, 3, 4, 5]

    if label_mode == 'Alphabet':
        label_mode = 'a'
    else:
        label_mode = '1'

    text_size, hole_scale, island_scale=640,100,100
    text, text_part, text_thresh = '','','0.0'
    with torch.autocast(device_type='cuda', dtype=torch.float16):
        semantic=False

        if model_name == 'semantic-sam':
            model = model_semsam
            output, mask = inference_semsam_m2m_auto(model, image, level, text, text_part, text_thresh, text_size, hole_scale, island_scale, semantic, label_mode=label_mode, alpha=alpha, anno_mode=anno_mode, *args, **kwargs)
        else:
            raise NotImplementedError

        return output

'''
build args and model
'''
semsam_cfg = "configs/semantic_sam_only_sa-1b_swinL.yaml"
semsam_ckpt = "./checkpoints/" + "swinl_only_sam_many2many.pth"
opt_semsam = load_opt_from_config_file(semsam_cfg)

model_semsam = BaseModel(opt_semsam, build_model(opt_semsam)).from_pretrained(semsam_ckpt).eval().cuda()


'''
Prepare data, download sharegpt4v coco-ids
'''
root_dir = f"./data/"
if not os.path.exists(root_dir+'sft/sharegpt4v_coco50k.json'):  
    ## save coco data used in sharegpt-4v (overlapped images are easier for comparison)  
    dataset = load_dataset("Lin-Chen/ShareGPT4V", data_files="sharegpt4v_instruct_gpt4-vision_cap100k.json", split="train")
    coco_data = []
    for example in dataset:
      if "coco" in example['image']:
          coco_data.append(example)
    with open(root_dir+'sft/sharegpt4v_coco50k.json', 'w') as file:
      json.dump(coco_data, file)

'''
launch model for training
'''
with open(root_dir+'sft/sharegpt4v_coco50k.json', 'r') as file:
    data = json.load(file)
    coco_ids = [d['id'] for d in data]
    coco_ids = list(set(coco_ids))
coco_ids.sort() ## sort to make sure orders are consistent.

slider = 1.75 # for level-2
alpha = 0.1
label_mode = 'Number'
anno_mode = ['Mark']
coco_dir = "train2017"
out_dir = root_dir + f"coco/som_{coco_dir}/"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

for cnt, i in enumerate(tqdm(coco_ids, desc="Processing images"), 1):
    if os.path.exists(out_dir+f'{i}.jpg'):
        continue
    image = Image.open(root_dir + f'coco/{coco_dir}/{i}.jpg')
    
    if image.mode != "RGB":
        image = image.convert("RGB")
    try: 
        out_img = inference(image, slider, alpha, label_mode, anno_mode)
    except:
        traceback.print_exc()
        print(f"Error with image {i}")
        continue
    out_img = Image.fromarray(out_img)
    out_img.save(out_dir + f'{i}.jpg')



'''
launch model for val
'''
slider = 1.75 # for level-2
alpha = 0.1
label_mode = 'Number'
anno_mode = ['Mark']
coco_dir = "val2017"
out_dir = root_dir + f"coco/som_{coco_dir}/"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)


coco_ids = os.listdir(root_dir+f"coco/{coco_dir}")
for cnt, i in enumerate(tqdm(coco_ids[:100], desc="Processing images"), 1):
    if os.path.exists(out_dir+f'{i}'):
        continue
    image = Image.open(root_dir + f'coco/{coco_dir}/{i}')
    
    if image.mode != "RGB":
        image = image.convert("RGB")
    try: 
        out_img = inference(image, slider, alpha, label_mode, anno_mode)
    except:
        traceback.print_exc()
        exit(f"Error with image {i}")
    out_img = Image.fromarray(out_img)
    
    # out_img.save(f'../examples/som_{i}.jpg')
    out_img.save(out_dir + f'{i}')
