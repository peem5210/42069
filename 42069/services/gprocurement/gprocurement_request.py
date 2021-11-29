import requests
import time


def intWithCommas(x):
    x = int(x)
    if type(x) not in [type(0)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)


def request_procurement(beginrec='', endrec='', grouppage='', project_type='', sdate='', edate='',
                        budget_start: int = 0, budget_end: int = 9e11, project_id='', dept_id=''):
    # locale.setlocale(locale.LC_ALL, 'en_US')
    budget_start = intWithCommas(budget_start) + '.00'
    budget_end = intWithCommas(budget_end) + '.00'
    print(budget_start, budget_end)
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://process.gprocurement.go.th',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://process.gprocurement.go.th/egp2procmainWeb/jsp/procsearch.sch',
        'Accept-Language': 'en-US,en;q=0.9,th;q=0.8',
    }

    data = {
        'announceType': '15',
        'budgetYear': '',
        'deptId': '',
        'deptSubId': '',
        'moiId': '',
        'methodId': '16',
        'textPath': '',
        'typeId': project_type,
        'govStatus': '',
        'project_id': '',
        'projectName': '',
        'announceSDate': sdate,
        'announceEDate': edate,
        'projectMoneyS': budget_start,
        'projectMoneyE': budget_end,
        'projectStatus': '',
        'flag': '',
        'flowHidden': '',
        'servlet': 'FPRO9965Servlet',
        'proc_id': 'FPRO9965',
        'proc_name': 'Procure',
        'retmenu': '',
        'processFlows': 'Procure',
        'mode': 'SEARCH',
        'homeflag': 'A',
        'temp_projectId': '',
        'temp_deptSubId': '',
        'temp_methodId': '',
        'temp_typeId': '',
        'temp_projectName': '',
        'temp_budgetYear': '',
        'temp_projectMoney': '',
        'temp_projectStatus': '',
        'temp_announDate': '',
        'temp_govStatus': '',
        'temp_moiId': '',
        'temp_announType': '',
        'temp_itemNo': '',
        'projectIdBidPrice': '',
        'temp_priceBuild': '',
        'pageNo': '',
        'grouppage': grouppage,
        'prevpage': '',
        'beginrec': beginrec,
        'endrec': endrec,
        'startindexloop': '',
        'url': '',
        'projectId': '',
        'pass': '',
        'templateType': '',
        'temp_Announ': '',
        'announceId': '',
        'seqNo': '',
        'resultc': '',
        'priceBuild': '',
        'ipaddress': '',
        'Owner_name_phone': '%A1%A1%D2%D1%D8%C0\u04A4%C3 %A1%BE%C0.) %A1%C3%C1%BA%AA\u0561%C5 %E2%B7%C3.02-127-7000 %B5%E8%CD 6704 4674 4958 6777 6928 6934 6800',
        'menu_flag': '',
        'type_id': '',
        'priv_status': '',
        'menusystem': '',
        'flagpage': '',
        'deptid': '',
        'offmoiid': '',
        'agencyid': '',
        'mainUserid': '',
        'mainEmployeeType': '',
        'mainRoleid': '',
        'tempsys': '',
        'flag_list': ''
    }

    page = ''
    while page == '':
        try:
            page = requests.post('http://process.gprocurement.go.th/egp2procmainWeb/jsp/procsearch.sch',
                                 headers=headers, data=data, verify=False, timeout=60)
            break
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(10)
            print("Was a nice sleep, now let me continue...")
            continue

    return page


dataSizeLimit = 50


def request_page(pageGroup, project_type, sdate, edate, budget, project_id, dept_id):
    return request_procurement((dataSizeLimit * pageGroup) + 1, ((dataSizeLimit * (pageGroup + 1)) + 1),
                               (pageGroup + 1), (project_type), sdate, edate, budget, 9e12, project_id, dept_id)





