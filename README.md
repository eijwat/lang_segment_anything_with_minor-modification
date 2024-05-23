# Language Segment-Anything

Language Segment-Anything is an open-source project that combines the power of instance segmentation and text prompts to generate masks for specific objects in images. Built on the recently released Meta model, segment-anything, and the GroundingDINO detection model, it's an easy-to-use and effective tool for object detection and image segmentation.

![person.png](/assets/outputs/person.png)

## 動かし方
今回はDockerを使って動かしています。

Dockerのインストール
```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Docker composeのインストール
```
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.4.1/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
```


dockerのビルド
```
git clone git@github.com:NIBB-Neurophysiology-Lab/lang-segment-anything.git
cd lang-segment-anything
docker compose up -d
```

実行
```
docker compose exec lang-segment-anything /bin/bash
pip install git+https://github.com/IDEA-Research/GroundingDINO.git
python3 demo.py
# fish_result.pngが保存される
```

## ビルド済みのイメージを使う場合
```
docker compose -f docker-compose.prebuild.yml up -d
docker compose -f docker-compose.prebuild.yml exec lang-segment-anything /bin/bash
python3 demo.py
```

## Features

- Zero-shot text-to-bbox approach for object detection.
- GroundingDINO detection model integration.
- Easy deployment using the Lightning AI app platform.
- Customizable text prompts for precise object segmentation.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- torch (tested 2.0)
- torchvision

### Installation

```
pip install torch torchvision
pip install -U git+https://github.com/luca-medeiros/lang-segment-anything.git
```

Or
Clone the repository and nstall the required packages:

```
git clone https://github.com/luca-medeiros/lang-segment-anything && cd lang-segment-anything
pip install torch torchvision
pip install -e .
```
Or use Conda
Create a Conda environment from the `environment.yml` file:
```
conda env create -f environment.yml
# Activate the new environment:
conda activate lsa
```


### Usage

To run the Lightning AI APP:

`lightning run app app.py`

Use as a library:

```python
from PIL import Image
from lang_sam import LangSAM

model = LangSAM()
image_pil = Image.open("./assets/car.jpeg").convert("RGB")
text_prompt = "wheel"
masks, boxes, phrases, logits = model.predict(image_pil, text_prompt)
```

Use with custom checkpoint:

First download a model checkpoint. 

```python
from PIL import Image
from lang_sam import LangSAM

model = LangSAM("<model_type>", "<path/to/checkpoint>")
image_pil = Image.open("./assets/car.jpeg").convert("RGB")
text_prompt = "wheel"
masks, boxes, phrases, logits = model.predict(image_pil, text_prompt)
```

## Examples

![car.png](/assets/outputs/car.png)

![kiwi.png](/assets/outputs/kiwi.png)

![person.png](/assets/outputs/person.png)

## Roadmap

Future goals for this project include:

1. **FastAPI integration**: To streamline deployment even further, we plan to add FastAPI code to our project, making it easier for users to deploy and interact with the model.

1. **Labeling pipeline**: We want to create a labeling pipeline that allows users to input both the text prompt and the image and receive labeled instance segmentation outputs. This would help users efficiently generate results for further analysis and training.

1. **Implement CLIP version**: To (maybe) enhance the model's capabilities and performance, we will explore the integration of OpenAI's CLIP model. This could provide improved language understanding and potentially yield better instance segmentation results.

## Acknowledgments

This project is based on the following repositories:

- [GroundingDINO](https://github.com/IDEA-Research/GroundingDINO)
- [Segment-Anything](https://github.com/facebookresearch/segment-anything)
- [Lightning AI](https://github.com/Lightning-AI/lightning)

## License

This project is licensed under the Apache 2.0 License
