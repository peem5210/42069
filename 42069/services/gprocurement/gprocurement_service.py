import ast
import pandas as pd
import unicodedata
from bs4 import BeautifulSoup
from cachetools import cached, TTLCache
from services.gprocurement.gprocurement_request import request_page


class GprocurementService:
    def __init__(self):
        self.TYPE_NAME = {
            "01": "ซื้อ",
            "02": "จ้างก่อสร้าง",
            "03": "จ้างทำของ/จ้างเหมาบริการ",
            "04": "เช่า",
            "05": "จ้างที่ปรึกษา",
            "06": "จ้างออกแบบ",
            "07": "จ้างควบคุมงาน",
            "08": "จ้างออกแบบและควบคุมงานก่อสร้าง"
        }

    def normalize_string(self, unicode_str):
        return unicodedata.normalize("NFKD", unicode_str).strip()

    def extract_attributes(self, tr, project_type):
        project_id_zipname = ast.literal_eval(
            "[{}]".format(str(tr.select('span')[0]).split('clkDownloadDoc(')[-1].split(")")[0]))
        dept_name = self.normalize_string(tr.select('td')[1].text)
        project_id = project_id_zipname[0]
        zipname = project_id_zipname[1]
        try:
            subdept_id = zipname.split('_')[1]
        except:
            subdept_id = ""
        zip_url = 'http://process3.gprocurement.go.th' + '/egp2procmainWeb/FPRO9965AttachServ?projectId=' + project_id + '&fileName=' + zipname
        winner_url = 'https://process3.gprocurement.go.th/egp2procmainWeb/jsp/procsearch.sch?servlet=gojsp&proc_id=ShowHTMLFile&processFlows=Procure&projectId=' + project_id + '&templateType=W2&temp_Announ=A&temp_itemNo=0&seqNo=2'
        story = self.normalize_string(tr.select('td')[2].text)
        annoucement_date = self.normalize_string(tr.select('td')[3].text)
        price = self.normalize_string(tr.select('td')[4].text)
        status = self.normalize_string(tr.select('td')[5].text)
        return (
        dept_name, subdept_id, project_id, annoucement_date, self.TYPE_NAME.get(project_type, ""), story, price, status,
        zip_url, winner_url)

    def get_trs(self, page, project_type, sdate, edate, budget=3 * 1e6, project_id='', dept_id=''):
        print("requesting page {}".format(page))
        response = request_page(page, project_type, sdate, edate, budget, project_id, dept_id)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.select('.tr0') + soup.select('.tr1')

    @cached(cache=TTLCache(maxsize=1000, ttl=60 * 60 * 24))
    def get_ebidding(self, page: int = 0,
                     project_type: str = '01',
                     sdate: str = '',
                     edate: str = '',
                     budget: int = 0,
                     project_id: str = '',
                     dept_id: str = ''):
        columns = ['dept_name', 'subdept_id', 'project_id', 'annoucement_date', 'type', 'story', 'price', 'status',
                   'zip_url', 'winner_url']
        trs = self.get_trs(page, project_type, sdate, edate, budget, project_id, dept_id)
        extracted_data = [self.extract_attributes(tr, project_type) for tr in trs]
        df = pd.DataFrame(data=extracted_data, columns=columns)
        return df.to_dict('records')
