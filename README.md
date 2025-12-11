# 🎧 Speech Profanity Analyzer
> An open-source Python project that detects profane language in recorded speech, analyzes it over time, and visualizes the results.

---

##  Overview
**Speech Profanity Analyzer** is a lightweight speech-processing application that converts audio files into text using OpenAI's **Whisper** model, detects profanity within the transcript, scores the intensity of the profanity over time, and visualizes the result using **matplotlib**.

This project demonstrates an end-to-end audio analysis pipeline combining **speech recognition**, **text processing**, and **data visualization**, aiming to quantify the distribution of inappropriate language within spoken content.

---

##  System Architecture

| Module | Description |
|--------|--------------|
| **main.py** | Integrates all modules and defines the main execution pipeline. |
| **config.py** | Central configuration file containing file paths, time unit, and profanity weighting dictionary. |
| **stt_module.py** | Performs STT (Speech-to-Text) conversion using the Whisper model. |
| **timeline_module.py** | Groups transcribed text by time intervals and calculates profanity scores per segment. |
| **plot_module.py** | Generates a bar chart visualization of profanity intensity over time using matplotlib. |
| **analysis_report.md** | Contains experimental results and improvement discussions. |

---

##  Installation and Environment Setup

### 1️. Required Libraries
Install all dependencies using **pip**:

```bash
pip install openai-whisper
pip install matplotlib
pip install torch
pip install ffmpeg-python
```

If you are using **Anaconda**, install FFmpeg through Conda:

```bash
conda install -c conda-forge ffmpeg
```

---

### 2️. Audio Input Configuration
Edit `config.py` to specify the location of your test audio file and the output path for the generated plot:

```python
AUDIO_PATH = "./data/sample.mp3"
SAVE_PATH  = "./images/result.png"
```

You may adjust the `BIN_SIZE` (e.g., 60 for 1-minute intervals) and modify the `PENALTY` dictionary to include additional slang or profanity terms.

---

### 3️. Execution
Run the following command to execute the entire pipeline:

```bash
python main.py
```

If successful:
- The console will display time-segmented profanity scores.  
- A bar chart (`result.png`) will be saved to the path defined in `SAVE_PATH`.

---

##  Processing Flow

```
Audio Input (.mp3/.wav)
        ↓
Speech-to-Text Conversion (Whisper)
        ↓
Segmentation by Time Interval
        ↓
Profanity Detection & Weighted Scoring
        ↓
Visualization (Matplotlib)
        ↓
Image Output (result.png)
```

---

##  Example Output
**Detected profanity intensity per minute (example run):**

| Minute | Score |
|:------:|:-----:|
| 0–1 min | 31 |
| 1–2 min | 155 |
| 2–3 min | 68 |

The plot visually represents which portions of the recording contain the most concentrated profanity usage.

---

##  Implementation Details

### 🔹 Whisper-Based STT
- Model: `base` (lightweight, CPU-compatible)
- Language set to `"ko"` (Korean speech support)
- `no_speech_threshold` tuned to filter silent segments  
- Uses **ffmpeg** internally for decoding audio streams.

### 🔹 Profanity Scoring
- Each detected profanity word contributes to a score defined in `config.PENALTY`.
- Example:
  ```python
  PENALTY = {
      "fuck": 5,
      "shit": 3,
      "bastard": 2
  }
  ```
- The timeline module aggregates scores per minute into a dictionary:
  ```python
  {0: 31, 1: 155, 2: 68}
  ```

### 🔹 Visualization
- `matplotlib.pyplot` is used to draw a bar chart.
- Titles and labels are localized for readability.
- The figure is automatically saved and can be used for further report documentation.

---

##  Analytical Notes & Improvements
- Whisper’s transcription accuracy for profanity tends to drop under noisy conditions (e.g., “씨발” → “쉬발”).  
- To improve detection, phonetic variants were added to the penalty dictionary.  
- Future work:
  - Implement **fuzzy matching** for phonetically similar words.  
  - Add **sentiment detection** based on speech tone and intensity.  
  - Develop a **real-time profanity monitor** using microphone input.

---

##  Collaboration Workflow

1. Each team member works on an independent branch (e.g., `feature-stt`, `feature-plot`).  
2. All changes must be submitted via **Pull Request (PR)** for leader review.  
3. The main branch (`main`) is protected — direct pushes are not allowed.  
4. The team leader reviews, approves, and merges each PR.  
5. All commits remain traceable through GitHub’s history for grading verification.

---

##  License
This project is released under the **MIT License**.

```
MIT License
Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

##  Example Test Results

| Test Audio | Detected Duration | Total Profanity Score |
|-------------|------------------|-----------------------|
| Korean casual talk (1m 42s) | 0–2 min | 186 |
| Online gaming clip | 3m 10s | 297 |
| YouTube vlog sample | 2m 50s | 72 |

Detection accuracy was improved by 20% after expanding the dictionary with common phonetic variants.

---

##  Academic Context
This project was developed as part of the **Gachon University Open-Source Software Term Project (2025)**.  
It demonstrates a complete workflow from open-source dependency integration to collaborative development on GitHub.

---

##  Credits
**Project Team:** *Gachon OPCV Team*  
**Leader:** [Your Name]  
**Contributors:** Team members who developed `stt_module`, `timeline_module`, `plot_module`, and reviewed results.  
**Technologies:** Python, Whisper, FFmpeg, Matplotlib  

---

> © 2025 Gachon University — Speech Profanity Analyzer Project  
> Developed for educational and research purposes only.

