from django.http import HttpResponse
from django.http import HttpResponseRedirect
from report import models
from report.models import *

def MSfileread(files,reportinfo):
    for file in files:
        if '.png' in file.name or ".jpg" in file.name or ".JPG" in file.name or ".PNG" in file.name or ".jpeg" in file.name:   
            MS.objects.create(reportinfo = reportinfo,img = file,name="")

            objs_verify = MS.objects.filter(reportinfo = reportinfo)
            id=[]
            for item in objs_verify:
                id.append(item.reportinfo_id)
            
    return {"objs_verify":objs_verify,"id":id[0]}

# 基质特异性数据关联进入最终报告
def related_MS(id): 
    # 后台数据关联进入报告
    # 优先查找特殊参数设置里是否有数据，如有就调用，没有则调用通用性参数设置里的数据

    # 第一步：后台描述性内容数据提取
    # 1 根据id找到项目
    project = ReportInfo.objects.get(id=id).project

    # 2 优先查找特殊参数设置里是否有数据，如有就调用，没有则调用通用性参数设置里的数据
    # 特殊参数设置描述性内容
    textlist_special = []
    try:
        special_1 = Special.objects.get(project=project)
        special_2 = MSspecial.objects.get(special=special_1)
        if MSspecialtexts.objects.filter(mSspecial=special_2).count() > 0:
            text_special = MSspecialtexts.objects.filter(mSspecial=special_2)
            for i in text_special:
                textlist_special.append(i.text)

    except:
        pass


    # 从数据库中抓取描述性内容
    textlist_general = []
    general_1 = General.objects.get(name="通用性项目")  # 通用参数设置描述性内容
    general_2 = MSgeneral.objects.get(general=general_1)
    text_general = MSgeneraltexts.objects.filter(mSgeneral=general_2) 
    for i in text_general:
        textlist_general.append(i.text)

    MS_table = MS.objects.filter(reportinfo_id = id)
    conclusion=[]
    for item in MS_table:
        conclusion.append(item.conclusion)

    if MS_table:
        if len(textlist_special) != 0:
            return {"MS_table":MS_table,"textlist":textlist_special,"conclusion":conclusion[0],"serial":len(textlist_special)+1,
            "obj_serial":len(conclusion)}
        else:  
            return {"MS_table":MS_table,"textlist":textlist_general,"conclusion":conclusion[0],"serial":len(textlist_general)+1,
            "obj_serial":len(conclusion)}