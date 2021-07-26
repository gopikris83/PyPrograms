# Program to check the internet speed
import speedtest


def convert_bytes(size):
    for x in ['bytes', 'Kbps','Mbps', 'Gbps', 'Tbps']:
        if size < 1024.0:
            return "%3.1f %s" %(size, x)
        size /= 1024.0
    return size

speed = speedtest.Speedtest()
download_speed = speed.download()
upload_speed = speed.upload()

print(f'Downlad Speed is {convert_bytes(download_speed)}')
print(f'Upload Speed is {convert_bytes(upload_speed)}')


