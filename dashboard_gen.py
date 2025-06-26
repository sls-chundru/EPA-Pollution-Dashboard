#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 22:08:03 2025

@author: srilakshmi
"""

# generate_dashboard.py
import os

# Define the output directory
output_dir = "docs"
os.makedirs(output_dir, exist_ok=True)

# Define HTML content
index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>US Pollution Dashboard</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>US Pollution Dashboard</h1>
  <h2>PM2.5 Levels by City</h2>
  <iframe src="assets/charts/pm25.html" width="100%" height="600" frameborder="0"></iframe>
</body>
</html>
"""

# Write to index.html
with open(os.path.join(output_dir, "index.html"), "w") as f:
    f.write(index_html)
