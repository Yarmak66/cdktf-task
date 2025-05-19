# CDKTF Static Website with S3 and CloudFront

This project provisions a static website hosted on Amazon S3 with CloudFront distribution using CDK for Terraform (CDKTF) in Python.

## Features

- 💡 Static website hosting via S3
- 🔐 Access controlled via CloudFront OAI
- 🌍 Public CloudFront distribution
- 🧩 Modular structure
- 📦 CI/CD with GitHub Actions (for plan, deploy, destroy)

## Requirements

- Python 3.11
- Node.js
- CDKTF CLI (`npm install -g cdktf-cli`)
- Terraform
- AWS credentials (set via GitHub Secrets or local environment)
