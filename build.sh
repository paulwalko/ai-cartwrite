#!/bin/bash

do_ocr () {
  for file in $(ls original); do
    gcloud ml vision detect-text-pdf gs://ai-cartwrite-trogs/original/"$file"  gs://ai-cartwrite-trogs/ocr/"$file"/
  done
}

parse_ocr () {
  for file in $(ls ocr/**); do
    echo $file
  done
}


$@
