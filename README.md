# SMS Word Cloud Pen Plotter

What began as a text message export/comparison project was transformed into creating physical word-cloud art using a modified Bambu A1 Mini as a pen plotter.

---

## Table of Contents

- [Description](#description)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [SMS Parsing](#sms-parsing)  
- [Word Cloud Generation](#word-cloud-generation)  
- [SVG Conversion](#svg-conversion)  
- [Pen Plotter Setup](#pen-plotter-setup)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [Contributing](#contributing)  

---

## Description

This project takes your SMS conversation export (via **SMS Backup & Restore**), parses it into “sent” and “received” text files, generates word clouds on [WordClouds.com](https://www.wordclouds.com/), composites them in Photoshop, converts the result to SVG, and then drives a **Bambu A1 Mini** (modified with 3D-printed parts) to plot the word cloud with a **Pilot G2 0.5 mm** pen.

---

## Requirements

- **Android** device with SMS Backup & Restore  
- **Python 3.11+** 
  (including xml.etree.ElementTree and argparse)
- Web browser for [WordClouds.com](https://www.wordclouds.com/)  
- **Adobe Photoshop** (optional for compositing/masking, can use GIMP/MS Paint etc)  
- Web access to [FreeConvert PNG-to-SVG](https://www.freeconvert.com/png-to-svg)  
- **Bambu A1 Mini** 3D printer + **Bambu Studio**
- These 3D printed files and hardware [Easy penholder A1 / A1 Mini Plotter](https://makerworld.com/en/models/1362648-easy-penholder-a1-a1-mini-plotter#profileId-1407684)
- Modified pen holder within ./3D Files/
- **Pilot G2 0.5 mm** gel pen
- some 65lb cardstock
- 4 small magnets to hold the cardstock

---

## Installation

1. Clone this repo:  
   ```bash
   git clone https://github.com/<your-username>/sms-wordcloud-plotter.git
   cd sms-wordcloud-plotter

---

## SMS Parsing

Use the included script to split your SMS XML into two text files:

```bash
python format_xml.py \
  -i path/to/sms_backup.xml \
  -o ./output
```

* **`format_xml.xml`**: Export from SMS Backup & Restore
* **`output/sent.txt`**, **`output/received.txt`**: ready for word-cloud input

---

## SMS Compare

Use the included script to compare your SMS text files:

```bash
python word_count_comparison.py \
  -i path/to/input_words.txt \
```

* **`input_words.txt`**: .txt file where each line is a string *
  
Input will be the following format:
```bash
lmao
love
fun
excited
```
Output will be the following format:
```bash
Metric                    Sent  Received
----------------------------------------
Total messages            1770      2004

Word                      Sent  Received
----------------------------------------
lmao                        55        90
love                        22        59
fun                         40        51
excited                     11        35
```

---

## Word Cloud Generation

1. Go to [WordClouds.com](https://www.wordclouds.com/).
2. Upload **`sent.txt`** or **`received.txt`**.
3. Upload the word cloud background image or create/modify one in photoshop
4. Tweak shape, mask, filter settings.
5. Ensure the color pallete is high contrast (white background, black text)
6. Download the word-cloud PNG.

---

## SVG Conversion

1. Visit [FreeConvert PNG-to-SVG](https://www.freeconvert.com/png-to-svg).
2. Upload your composited PNG (from Photoshop).
3. Ensure you check 'black and white' under Advanced Settings
4. Download **`wordcloud.svg`**.

---

## Pen Plotter Setup

1. **3D-print** the pen-mount using the link provided, replacing the pen holder with the one in the repo.
   
    <img width="194" alt="modified_flex_holder" src="https://github.com/user-attachments/assets/f4c8545e-f0a4-42a8-bfb8-c3b965e86fc6" />
  
3. Open the pilot G2 pen and move the small spring in the pen tip to above the ink cartrige near the top of the pen. This will allow the pen to travel in Z direction when pressed against the paper.
4. Attach the mount to your A1 Mini and insert a **Pilot G2 0.5 mm** pen with some shims to ensure it is solid.
5. In **Bambu Studio**, adjust your machine code:
   * Remove all 'machine gcode' only leaving **G28 X**
   * Remove all 'machine end gcode' only leaving **G28 X** and the printer finish sounds, if you like
   * **Z-hop** edit the nozzle settings to z-hop 5mm when retracting with the lowest travel threshold possible (0.01)
   * **Disable** edit the filament settings for zero bed and zero extruder temp
   * **Layer Height** set layer height to 0.1mm and line width to 0.15mm
6. Level your bed with the textured plate and two layers of cardstock on top (with magnets)
7. Set Z to lowest position and adjust the pen in the holder until the tip is touching the paper and 50% pressed (partial pressure on the tip via the spring).
8. Rehome.

---

## Usage

1. **Import** `wordcloud.svg` into Bambu Studio.
2. Scale the imported file such that it fits on the build plate and has a thickness of 0.11mm (one layer).
3. **Slice** and **Print**.
4. Watch bambu plot some stuff

---

## Images

1. Pen plotter assembled
![20250527_172813](https://github.com/user-attachments/assets/bdc452b6-10ee-4bc0-88b4-34fb79581315)



3. Pen plotter in action
https://github.com/user-attachments/assets/165a14ab-92b0-44fc-a954-ca418eff1e58


---

## Contributing

Contributions welcome! Please open an issue or submit a pull request for bug fixes or new features.

```
