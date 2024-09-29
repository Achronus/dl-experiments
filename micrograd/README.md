# Exploring Micrograd

Backpropagation is the backbone of training Neural Networks. It enables efficient computation of gradients, allowing the model to adjust its weights and minimize error during training. Without it, Neural Networks would be useless, unable to learn from data or generalize effectively. 

Understanding it at a deep level is incredibly valuable and heavily abstracted away in most Deep Learning frameworks like PyTorch and Tensorflow. Andrej Karpathy created a miniature Autograd engine called [micrograd](https://github.com/karpathy/micrograd) which aims to build intuition behind *Reverse-Mode Auto-Differentiation*, the method used to compute gradients in these frameworks.

This repository is an extension of that to help gain a deeper understanding of how it works. We'll dive into the math of the system and build it from scratch, incrementally increasing complexity as we go. If this sounds interesting to you, then strap yourself in and let's get started!

## Reverse-Mode Auto-Differentiation

First, let's tackle the scary beast that is *Reverse-Mode Auto-Differentiation*.

