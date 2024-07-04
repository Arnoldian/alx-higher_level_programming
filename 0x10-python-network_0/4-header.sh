#!/bin/bash
# script sending custom headers to servers
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
