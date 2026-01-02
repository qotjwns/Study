import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import make_grid
import matplotlib.pyplot as plt

tfm = transforms.ToTensor()
train_ds = datasets.CIFAR10(root="./data", train=True, download=True, transform=tfm)
loader = DataLoader(train_ds, batch_size=64, shuffle=True)

imgs, labels = next(iter(loader))

grid = make_grid(imgs, nrow=8, padding=2)            # (3, H, W)
grid = grid.permute(1, 2, 0)                         # (H, W, 3)

plt.figure(figsize=(8, 8))
plt.imshow(grid)
plt.axis("off")
plt.show()