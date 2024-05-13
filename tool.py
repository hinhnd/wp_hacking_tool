import re
from flask import Flask, send_file, render_template, request
import subprocess
import time
from urllib.parse import urlparse

app = Flask(__name__)
@app.route('/txt')
def txt():
    return send_file('scripts/output/wpscan_output.txt', as_attachment=True)
@app.route('/html')
def html():
    return send_file('scripts/output/wpscan_output.html', as_attachment=True)
@app.route('/')
def index():
    return send_file('home.html')
@app.route('/viewwpscan')
def index1():
    return send_file('wpscan.html')
@app.route('/viewnmap')
def index2():
    return send_file('scripts/output/nmap_out.html')
@app.route('/run', methods=['POST'])
def run():
    target = request.form['target']
    
    # Kiểm tra và thêm giao thức mặc định nếu cần
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target  # Sử dụng http nếu không có giao thức

    # Phân tích URL để lấy tên miền chính xác
    parsed_url = urlparse(target)
    domain = parsed_url.netloc  # Lấy tên miền
    target = domain
    # Tạo URL của Censys sử dụng tên miền
    domains = 'https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=' + domain
    
    # In URL hoặc thực hiện các bước tiếp theo
    print(domains)
    



    start_time_nmap = time.time()  # Ghi lại thời điểm bắt đầu thực thi
    result = subprocess.run(['bash', 'scripts/nmap_scan.sh', target], capture_output=True, text=True)
    end_time_nmap = time.time()  # Ghi lại thời điểm kết thúc thực thi
    execution_time_nmap = end_time_nmap - start_time_nmap  # Tính thời gian chạy
    time_nmap = 'Done (Execution time: {:.2f} seconds)'.format(execution_time_nmap)
    print("done nmap")
    start_time_waf = time.time()  # Ghi lại thời điểm bắt đầu thực thi
    result2 = subprocess.run(['bash', 'scripts/waf_scan.sh', target], capture_output=True, text=True)
    end_time_waf = time.time()  # Ghi lại thời điểm kết thúc thực thi
    execution_time_waf = end_time_waf - start_time_waf  # Tính thời gian chạy
    time_waf = 'Done (Execution time: {:.2f} seconds)'.format(execution_time_waf)
    print("done waf")

    start_time_wpscan = time.time()  # Ghi lại thời điểm bắt đầu thực thi
    result3 = subprocess.run(['bash', 'scripts/wpscan.sh', target], capture_output=True, text=True)
    end_time_wpscan = time.time()  # Ghi lại thời điểm kết thúc thực thi
    execution_time_wpscan = end_time_wpscan - start_time_wpscan  # Tính thời gian chạy
    time_wpscan = 'Done (Execution time: {:.2f} seconds)'.format(execution_time_wpscan)
    print("done wpscan")
    start_time_brute = time.time()  # Ghi lại thời điểm bắt đầu thực thi
    result4 = subprocess.run(['bash', 'scripts/brute-force-run.sh', target], capture_output=True, text=True)
    end_time_brute = time.time()  # Ghi lại thời điểm kết thúc thực thi
    execution_time_brute = end_time_brute - start_time_brute  # Tính thời gian chạy
    time_brute = 'Done (Execution time: {:.2f} seconds)'.format(execution_time_brute)
    print("brute-force")



    with open('scripts/output/waf_out.txt', 'r') as file:
        data_waf = file.read()
    data_brute = []
    with open('scripts/output/brute-force-output.txt', 'r') as file:
        for line in file:
            if 'password' in line:
                data_brute .append(line.strip())
            if 'SUCCES' in line:
                data_brute .append(line.strip())
    # Đường dẫn đến tệp văn bản
        return render_template('table.html',url = domains,time_brute=time_brute,time_waf=time_waf, time_nmap=time_nmap,time_wpscan=time_wpscan, data_waf=data_waf, data_brute  = data_brute ) 

if __name__ == '__main__':
    app.run()
