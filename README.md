# Virtual Assistant for Linux

## Introduction

It's a simple virtual assistant for Linux (Ubuntu). You can start applications or ask the current time with voice instruction.
I just made for fun.

## Description

Application uses Google Speech Recognition API free version.
Support language is only Hungarian.

Supported instructions:
* <em>'fájl'</em> - open file browser (nautilus)
* <em>'level'</em> or <em>'levél'</em> - open email client (thunderbird)
* <em>'terminál'</em> - open terminal(gnome-terminal)
* <em>'zene'</em> or <em>'zené'</em> open spotify
* <em>'óra'</em> or <em>'pontos idő'</em> - say the current time (hours, minutes)
* <em>'keress rá'</em> and after only <em>'keywords'</em> - open chrome and start searching for keywords 
* <em>'pihenj'</em> - switch off virtual assistant

## Usage

<p>Always start instructions with <em>'ubuntu'</em>. This activates the virtual assistant. Then continue with the instruction.</p>
 e.g.: <em>'Hé ubuntu, nyisd meg a <b>terminál</b>t!'</em></p>
 e.g.: <em>'Hé ubuntu, <b>zené</b>t akarok hallgatni!'</em></p>
 e.g.: <em>'Ubuntu, mennyi a <b>pontos idő</b>?'</em></p>
 e.g.: <em>'Ubuntu <b>keress rá eger budapest buszmenetrend</b>'</em></p>

## Installation

1. Clone the repo:
```bash
git clone https://github.com/tothgeza/VirtualAssistant.git
```
2. Move to project folder:
```bash
cd VirtualAssistant
```
3. Install virtual environment:
```bash
virtualenv -p python3 venv
```
4. Start virtual environment:
```bash 
source venv/bin/activate
```
5. Install packages:
```bash
pip install -r requirements.txt
```
4. Run application:
```bash
python3 main.py
```



