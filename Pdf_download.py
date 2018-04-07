import wget
import os, os.path
import shutil
#urls_get = input('Введите адреса через запятую: ')
#urls = list(urls_get)

dir = 'C:/Users/pavel.golubev/Desktop/Programming/Download/'

urls = ['https://www.accenture.com/t20160824T011003Z__w__/us-en/_acnmedia/Accenture/Conversion-Assets/Outlook/Documents/2/Accenture-Outlook-Smart-Way-Open-Your-Innovation-Process.pdf',
        'https://www.accenture.com/ae-en/~/media/Accenture/Conversion-Assets/DotCom/Documents/Global/PDF/Technology_6/Accenture-Four-Ways-that-Mobility-can-Transform-Government-Solutions-v2.pdf',
        'https://www.accenture.com/t20150523T033707Z__w__/us-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Documents/Global/PDF/Dualpub_9/Accenture-Bridgemakers-Guiding-Enterprise-Disruption.pdf',
        'https://www.accenture.com/t20160804T150711Z__w__/us-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Documents/Global/PDF/Dualpub_24/Accenture-The-Digital-Future-of-Medicaid-video-transcript.pdf',
        'https://www.accenture.com/t20170629T190038Z__w__/cn-en/_acnmedia/PDF-55/Accenture-How-Artificial-Intelligence-Can-Drive-Chinas-Growth.pdf',
        'https://www.accenture.com/t00010101T000000Z__w__/au-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Documents/Local/au-en/PDF/1/Accenture-Redesigning-Government-Innovation.pdf',
        'https://www.accenture.com/t20160719T212314Z__w__/us-en/_acnmedia/PDF-1/Accenture-15362-Top-5-Trends-South-Africa-Final.pdf',
        'https://www.accenture.com/t20170217T065052Z__w__/us-en/_acnmedia/Accenture/cchange/welcome-disruption/Accenture-PSET-Report.pdf']

while len(os.listdir(dir)) < len(urls):
    for url in urls:
        wget.download(url, dir)
print('Download finished')


shutil.make_archive('output', 'zip', dir)
print('Archive is done')


