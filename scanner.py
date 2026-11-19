import subprocess
import requests
import urllib.parse

def scan_target(url):
    
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    
    report = {
        'target': domain,
        'open_ports': [],
        'headers_missing': [],
        'server_info': 'Unknown',
        'status': 'Scanning Complete'
    }

  
    try:
      
        nmap_cmd = ["nmap", "-F", "--open", domain]
        result = subprocess.run(nmap_cmd, capture_output=True, text=True, timeout=120)
        
        
        for line in result.stdout.split('\n'):
            if '/tcp' in line and 'open' in line:
                port = line.split('/')[0]
                service = line.split()[2]
                report['open_ports'].append(f"Port {port} ({service})")
    except Exception as e:
        report['open_ports'].append(f"Port scan failed: {str(e)}")

  
    try:
        res = requests.get(url, timeout=10, allow_redirects=True)
        
        
        if 'Server' in res.headers:
            report['server_info'] = res.headers['Server']

        
        security_headers = [
            'X-Frame-Options', 
            'X-XSS-Protection', 
            'Content-Security-Policy',
            'Strict-Transport-Security'
        ]
        
        for header in security_headers:
            if header not in res.headers:
                report['headers_missing'].append(header)
                
    except Exception as e:
        report['headers_missing'].append(f"HTTP check failed: {str(e)}")

    return report
