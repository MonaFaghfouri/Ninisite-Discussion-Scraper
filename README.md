# 🔎 Ninisite Discussion Scraper

A Python-based web scraping pipeline for collecting, structuring, and exporting **Persian online discussion data** from Ninisite.

The project demonstrates an end-to-end workflow for extracting user-generated content from dynamic web pages using **Playwright**, transforming raw discussion content into structured datasets, and preparing the resulting data for downstream **NLP, social media analytics, and consumer insight analysis**.

> **Portfolio Version**  
> This repository contains a public demonstration of the original scraping pipeline. Production-specific selectors, authentication logic, and parts of the extraction implementation are intentionally omitted.

---

## 🚀 Project Overview

Online discussion forums contain valuable information about consumer experiences, product perceptions, recurring concerns, and emerging topics.

This project was developed to transform unstructured Persian forum discussions into analysis-ready datasets.

The pipeline follows the complete data collection process:

```text
Search Keyword
      ↓
Search Result Discovery
      ↓
Topic URL Collection
      ↓
Discussion Crawling
      ↓
Post & Comment Extraction
      ↓
Persian Text Cleaning
      ↓
Duplicate Handling
      ↓
Structured Dataset
      ↓
CSV / Excel Export
```

---

## ✨ Key Features

- 🔍 Keyword-based discussion discovery
- 🌐 Automated browser interaction using Playwright
- 🔗 Automatic topic URL collection
- 📄 Search-result pagination handling
- 💬 Post and comment extraction
- 🔄 Multi-page discussion crawling
- 🧹 Persian text cleaning and normalization
- ♻️ Duplicate-content handling
- 🏷️ Post-level metadata extraction
- 📊 Structured Pandas DataFrames
- 📁 Automatic CSV and Excel export
- 📝 Topic-level error logging
- ⚙️ Environment-based configuration

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core scraping and processing |
| **Playwright** | Browser automation and dynamic-page interaction |
| **Pandas** | Data transformation and tabular processing |
| **OpenPyXL** | Excel output generation |
| **Regex** | Persian text cleaning and normalization |

---

## 📊 Output Structure

The scraper transforms forum discussions into structured records containing fields such as:

| Field | Description |
|---|---|
| Search Query | Keyword used to discover the discussion |
| Topic Title | Title of the discussion thread |
| Topic URL | Source discussion URL |
| Search Page | Search-result page where the topic was found |
| Topic Page | Page number inside the discussion |
| Post Number | Sequential post/comment number |
| Type | Original post or comment |
| Post ID | Extracted post identifier |
| Username | Author metadata when available |
| Date / Time | Published date and time |
| Text | Cleaned discussion content |
| Scrape Timestamp | Data-collection timestamp |

This structure makes the collected data suitable for subsequent analytical workflows.

---

## 🧠 Potential Applications

The resulting dataset can be used for:

- Sentiment analysis
- Topic modeling
- Consumer insight mining
- Product perception analysis
- Complaint and pain-point detection
- Brand monitoring
- Trend discovery
- Keyword and phrase analysis
- Social listening
- Persian NLP research

For example, forum discussions around a product category can be transformed from thousands of unstructured comments into structured data suitable for identifying recurring consumer concerns and product attributes.

---

## 📁 Repository Structure

```text
Ninisite-Discussion-Scraper/
│
├── ninisite_scraper_demo.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── sample_output/
│   └── sample_data.csv

```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd Ninisite-Discussion-Scraper
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Install the Playwright browser:

```bash
python -m playwright install firefox
```

---

## 🔐 Configuration & Security

Sensitive information should **never be hard-coded into the source code**.

Where authentication is required, credentials should be provided through environment variables or another secure configuration mechanism.

Example:

```bash
NINISITE_USERNAME=your_username
NINISITE_PASSWORD=your_password
```

Files containing credentials, private datasets, and generated production outputs should be excluded through `.gitignore`.

---

## 🧪 Public Demo Version

This repository is intended to demonstrate the **architecture, engineering approach, and data pipeline design** of the project rather than distribute the complete production scraper.

Therefore, some components of the original implementation have intentionally been simplified or omitted, including:

- Production-specific DOM selectors
- Full authentication workflow
- Complete extraction rules
- Anti-failure/recovery logic
- Production configuration
- Private datasets and credentials

The public version focuses on demonstrating the underlying scraping workflow and software design.

---

## 🔄 Data Pipeline

```text
┌─────────────────────┐
│    Search Keyword   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Search Results    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Topic Discovery   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Discussion Crawler  │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Posts & Comments    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Text Cleaning     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Structured Dataset  │
└──────────┬──────────┘
           ↓
      CSV / Excel
```

---

## 🎯 Design Goals

The project was designed around four main principles:

**Scalability** — automatically process multiple search-result pages and discussion threads.

**Reproducibility** — convert the scraping process into a repeatable pipeline rather than manual data collection.

**Structured Output** — transform unstructured Persian discussions into analysis-ready tabular data.

**Separation of Collection and Analysis** — keep data acquisition independent from downstream NLP and business analytics workflows.

---

## 📈 From Scraping to Analytics

Web scraping is only the first stage of the pipeline.

The structured output can subsequently feed analytical workflows such as:

```text
Web Data
   ↓
Data Cleaning
   ↓
Persian NLP
   ↓
Topic / Sentiment Analysis
   ↓
Consumer Insights
   ↓
Dashboard & Decision Support
```

This allows large volumes of online discussion data to be transformed into actionable information for research and business applications.

---

## ⚖️ Responsible Use

This project is intended for educational, research, and portfolio purposes.

Users are responsible for ensuring that their use of web scraping complies with applicable laws, privacy requirements, website terms, robots policies where applicable, and appropriate data-handling practices.

The repository does not include private datasets, credentials, or intentionally restricted production components.

---

## 👩‍💻 Author

**Mona Faghfouri Azar**

Data Analyst | Python Developer | Web Scraping & NLP

Research interests include:

- Web Scraping & Data Collection
- Natural Language Processing
- Computational Social Science
- Social Media Analytics
- Consumer & Business Analytics
- Machine Learning

GitHub: `MonaFaghfouri`

---

## ⭐ About This Repository

This repository is part of my technical portfolio demonstrating practical experience in:

**Python automation · Web scraping · Browser automation · Data engineering · Persian NLP · Structured data collection**

If you find the project useful, feel free to explore the repository and its methodology.
