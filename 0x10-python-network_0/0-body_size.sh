#!/bin/bash
# send request of URL, and display size of body of response
curl -s "$1" | wc -c
