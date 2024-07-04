#!/bin/bash
# bash script displaying status code of server
curl -L -s -X HEAD -w "%{http_code}" "$1"
