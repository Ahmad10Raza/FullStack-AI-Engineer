——————————————————

3-Month Roadmap

——————————————————

Month 1 – Core Foundations (C++, GPU Basics, ONNX, Benchmarking)

Week 1: C++ for ML Engineering

Learn only the parts of C++ needed for ML inference:

• C++17 basics

• Pointers, references, memory management

• OOP essentials

• Standard Library (STL)

• Multithreading (std::thread, mutexes)

• CMake basics

Mini-Projects

✔ Implement a simple matrix multiplication in C++

✔ Implement a basic inference pipeline in C++ calling ONNX Runtime API

Tools: CMake, g++, VS Code, ONNX Runtime C++ API

Week 2: ONNX + Model Exporting + ONNX Runtime

Learn:

• Export PyTorch → ONNX

• Export TensorFlow → ONNX

• Optimize ONNX graphs

• Dynamic vs static shapes

• Running ONNX inference (Python + C++)

• ONNX operators & compatibility

Mini-Projects

✔ Convert a ResNet / BERT model to ONNX

✔ Benchmark ONNX vs PyTorch model speed

Week 3: GPU Basics + CUDA Fundamentals (Beginner level)

You don’t need deep CUDA, just ML-oriented GPU knowledge:

• GPU architecture (SM, warp, grid, block)

• memory hierarchy (global/shared/registers)

• how inference engines use GPU kernels

• performance factors: batch size, precision, IO

Mini-Projects

✔ Write a very basic CUDA kernel (vector add)

✔ Profile GPU inference throughput

Week 4: Benchmarking & Profiling ML Models

Learn:

• Torch.profiler

• TensorFlow profiler

• ONNX Runtime profiler

• NVIDIA Nsight Systems

• warmup steps

• p50/p90/p99 latency

• throughput measurement

Mini-Projects

✔ Create a benchmarking script for CNN + Transformer

✔ Compare FP32 vs FP16 vs INT8 performance

——————————————————

Month 2 – Model Optimization & Inference Engines

——————————————————

Week 5: TensorRT (Most Important for Binaire)

Learn:

• Build TRT engines from ONNX

• INT8 quantization

• FP16 precision

• calibration datasets

• debugging TensorRT errors

• TensorRT benchmarking

Mini-Projects

✔ Convert YOLO / ResNet / BERT to TensorRT

✔ Benchmark ONNX vs TensorRT

Week 6: TensorFlow Lite (TFLite)

Learn:

• Convert TF models → TFLite

• dynamic range quantization

• full-integer (INT8) quantization

• post-training quantization

• model size reduction and accuracy trade-offs

• running TFLite on CPU/GPU

Mini-Projects

✔ Convert a MobileNet model to TFLite

✔ Compare FP32 vs INT8 accuracy drop

Week 7: Pruning, Quantization, Distillation (Theory + Implementation)

Learn:

• magnitude pruning

• structured pruning

• knowledge distillation

• low-rank approximation

• quantization-aware training (QAT)

Mini-Projects

✔ Prune a CNN by 20–40%

✔ Train a small student model using distillation from BERT

Week 8: Edge & Compiler-Based Optimization

Learn:

• OpenVINO (Intel)

• TVM (model compiler)

• XLA (Accelerated Linear Algebra compiler)

• graph-simplification techniques

Mini-Projects

✔ Convert a model to OpenVINO and benchmark

✔ Compile a PyTorch model using TVM

——————————————————

Month 3 – Multi-Modal Models + ML Systems + Portfolio Projects

——————————————————

Week 9: Multi-Modal Learning (CLIP, ViT, Image+Text Models)

Learn:

• CLIP architecture

• dual encoders

• contrastive learning (InfoNCE)

• image-text embedding alignment

• ViT basics

Mini-Projects

✔ Train a mini CLIP model on a custom dataset

✔ Build an image-text search system (embeddings)

Week 10: Model Serving & Deployment

Learn:

• Triton Inference Server

• TorchServe

• TensorFlow Serving

• gRPC vs REST

• batch inference

• model versioning

• logging, monitoring, health checks

Mini-Projects

✔ Deploy a model in Triton with batching

✔ Build a simple ML API using gRPC

Week 11: ML Systems Design (Very Important for Interviews)

Learn:

• end-to-end ML pipelines

• data → model → inference → monitoring

• scaling inference

• offline vs online inference

• caching, batching, load balancing

• hardware-aware ML

Mini-Projects

✔ Design an inference system for a multimodal model

✔ Simulate high-throughput batch inference

Week 12: Final Portfolio Projects (Binaire-Aligned)

Build 2–3 production-grade ML engineering projects:

Project 1 — **Model Optimization Benchmark Suite**

What you include:

• ONNX, TensorRT, TFLite versions of a model

• latency/throughput/memory benchmarks

• FP32 vs FP16 vs INT8

• report + charts

This directly matches their JD.

Project 2 — **Multi-Modal Inference Web Demo**

Stack: PyTorch + ONNX + TensorRT + React

Features:

• upload image + text → multi-modal prediction

• benchmarks included

• optimized inference

Project 3 — **Inference Engine Comparison Dashboard**

Stack: Python + FastAPI + Grafana

Functions:

• upload model

• auto-convert to ONNX/TensorRT

• run inference tests

• display metrics

This is resume-gold for ML Infra roles.

——————————————————

TOOLS YOU WILL MASTER IN 90 DAYS

——————————————————

• C++17

• ONNX Runtime

• TensorRT

• TensorFlow Lite

• OpenVINO

• TVM

• CUDA basics

• TensorFlow Serving / TorchServe

• Triton Inference Server

• Nsight Systems

• Torch.profiler

• TFLite quantization

• PyTorch/TensorFlow model export and optimization

——————————————————

THEORY YOU WILL MASTER

——————————————————

• quantization (PTQ + QAT)

• pruning (structured vs unstructured)

• knowledge distillation

• contrastive learning (CLIP, dual encoders)

• performance metrics (latency, p99, throughput)

• compute graph optimization

• model serving architecture

• GPU memory hierarchy

——————————————————

If you want, I can also create:

• a **weekly study timetable**

• a **book + course list** for each topic

• a **GitHub roadmap repository** with tasks

• a **resume version tailored for Binaire**

Just tell me what you want next.
