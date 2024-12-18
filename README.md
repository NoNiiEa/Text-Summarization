# Text Summarization Project

## Project Overview
This project focuses on text summarization by analyzing a dataset of tweets and generating a ranked summary of significant keywords or phrases. The project leverages techniques such as **Tri-Gram Graph Generation**, **PageRank**, and **TrustRank** to identify and score important nodes (words/phrases) in the graph.

The overall workflow includes:
1. **Text Preprocessing**: Clean and process raw text data.
2. **Graph Generation**: Build a tri-gram graph where nodes represent n-grams (sequences of words).
3. **Ranking Nodes**: Use algorithms like PageRank and TrustRank to rank nodes based on importance.
4. **Summarization**: Extract and rank significant keywords/phrases for summarization.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [Workflow](#workflow)
6. [File Details](#file-details)
7. [Acknowledgments](#acknowledgments)

---

## prerequisites
- Python 3.x
- Required libraries:
    - `networkx`
    - `json`
    - `nltk` (or other text preprocessing tools)

Install all required libraries:
```bash
pip install -r requirements.txt
```

---

## Project Structure
The directory contains the following files:
```
.
├── data/                       # Input data folder
│   └── Itaewon_tragedy.json    # Example input dataset
├── cache/                      # Cached outputs
│   ├── TriGraph.json           # Generated tri-gram graph
│   ├── score_pageRank.json     # PageRank scores
│   └── score_trustRank.json    # TrustRank scores
├── json_handler.py             # JSON reading and writing utilities
├── text_preprocessing.py       # Text preprocessing functions
├── triGraph.py                 # Functions for tri-gram graph generation
├── pageRank_fun.py             # PageRank algorithm implementation
├── trustRank_fun.py            # TrustRank algorithm implementation
├── summarization.py            # Pathfinding for summarization
└── main.py                     # Main entry point
```