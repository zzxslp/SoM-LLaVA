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
