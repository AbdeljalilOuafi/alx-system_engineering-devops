#!/usr/bin/env bash
#this script takes in a URL, sends a request to that URL,
#and displays the size of the body of the response

url=$1
size=$(curl -s "$url" | wc -c)
echo "$size"

