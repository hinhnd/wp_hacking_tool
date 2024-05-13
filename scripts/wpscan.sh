#!/bin/bash
target="$1"
wpscan   --url https://"${target}" --api-token  dLkFo2A2paqsqBpqyU5K7sCBpQyl9wseepYoiC4lH0c  --output scripts/output/wpscan_output.txt
wpscan   --url https://"${target}" --api-token  dLkFo2A2paqsqBpqyU5K7sCBpQyl9wseepYoiC4lH0c  --format json  --output  scripts/output/wpscan_output.json
python3 -m wpscan_out_parse scripts/output/wpscan_output.json  --format html > scripts/output/wpscan_output.html
