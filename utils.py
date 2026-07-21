import sys

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return uptime_seconds

def get_hostname():
    with open('/etc/hostname', 'r') as f:
        hostname = f.read().strip()

    return hostname

def get_python_version():
    return sys.version
