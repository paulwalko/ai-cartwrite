#!/usr/bin/env python3

import json
import os

#OCR_PATH = './ocr'
#OCR_TEXT_PATH = './ocr-text'

for pdf in os.listdir(OCR_PATH):
    os.mkdir(f'{OCR_TEXT_PATH}/{pdf}')

    for text in os.listdir(f'{OCR_PATH}/{pdf}'):
        os.mkdir(f'{OCR_TEXT_PATH}/{pdf}/{text}')

        with open(f'{OCR_PATH}/{pdf}/{text}') as f:
            r = json.load(f)['responses']
            for i in range(len(r)):
                with open(f'{OCR_TEXT_PATH}/{pdf}/{text}/{i}.txt', 'w') as fi:
                    if 'fullTextAnnotation' in r[i]:
                        fi.write(r[i]['fullTextAnnotation']['text'])
