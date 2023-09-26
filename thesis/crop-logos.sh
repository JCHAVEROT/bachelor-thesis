#!/bin/sh

command -v pdfcrop >/dev/null 2>&1 || {
  echo >&2 "pdfcrop executable not found in PATH:"
  echo >&2 "${PATH}"
  exit 1
}

LOGOS="epfl-black epfl-red epfl-white"

for logo in ${LOGOS}
do
  pdfcrop "logos/${logo}.pdf" "logos/${logo}.pdf"
done