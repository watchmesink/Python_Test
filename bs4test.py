import bs4
import requests

res = requests.get('https://www.amazon.de/-/en/dp/024134848X/?coliid=I2ZOLXPGB7PEJG&colid=ZWC2ZWRURM8K&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
soup.select('')