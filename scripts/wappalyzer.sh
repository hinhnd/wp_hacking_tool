#!/bin/bash
# Gán đầu vào cho biến target
target="$1"
# Ví dụ về việc chạy một lệnh curl với biến target
curl 'https://hackertarget.com/whatweb-scan/' --compressed -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0' -H 'Accept: text/html, */*; q=0.01' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://hackertarget.com' -H 'Connection: keep-alive' -H 'Referer: https://hackertarget.com/whatweb-scan/' -H 'Cookie: _ga_3JZVG4J6QH=GS1.1.1715013735.5.1.1715013752.0.0.0; _ga=GA1.1.1688183288.1704885305' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'TE: trailers' --data-raw 'theinput=${target}&name_of_nonce_field=d24d07085e&_wp_http_referer=%2Fwhatweb-scan%2F&terms=checked&enumtype=wapp'  -o scripts/output/wappalyzer_out.html

