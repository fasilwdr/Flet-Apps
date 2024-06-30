#!/bin/bash

app="Markdown"
output="builds/ipa"
product="Markdown"
buildVersion="0.1.1"

flet build ipa "$app" --output "$output" --product "$product" --build-version "$buildVersion"
