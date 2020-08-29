#!/usr/bin/env python3

import os

#OCR_TEXT_PATH = './ocr-text'

for pdf in os.listdir(OCR_TEXT_PATH):
    for output in os.listdir(f'{OCR_TEXT_PATH}/{pdf}'):
        for text in os.listdir(f'{OCR_TEXT_PATH}/{pdf}/{output}'):
            page = int(output.split('-')[1]) +  int(text.rstrip('.txt'))
            os.rename(f'{OCR_TEXT_PATH}/{pdf}/{output}/{text}', f'{OCR_TEXT_PATH}/{pdf}/{page}.txt')
