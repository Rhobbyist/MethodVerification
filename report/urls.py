from django.urls import path, include

import report.views

from django.urls import re_path as url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    # 初始界面，即验证界面
    path('', report.views.get_verification_page,name="verification"),

    # 登陆界面
    path('login', report.views.get_login_page, name="login"),

    # 登出界面
    path('logout', report.views.get_logout_page, name="logout"),

    # 报告生成界面
    path('generation', report.views.get_generation_page, name="generation"),

    # 最终报告预览界面(点击报告预览后跳转界面)
    path('report/<int:id>/<str:operation>', report.views.get_report_page, name="report"),

    # 在删除界面勾选删除选项(删除整份报告或删除一个或多个验证指标)后返回的界面，也是报告生成界面
    path('reportoperate/<int:id>', report.views.get_reportoperate_page, name="reportoperate"),

    # 在报告生成界面点击继续验证时跳转的界面
    path('verifyagain/<int:id>', report.views.get_verifyagain_page, name="verifyagain"),

    # 验证时机保存
    path('JMDsave', report.views.JMDsave, name="JMDsave"),

    # PT数据保存
    path('PTsave', report.views.PTsave, name="PTsave"),

    # 加标回收率数据保存
    path('Recyclesave', report.views.Recyclesave, name="Recyclesave"),

    # 仪器比对数据保存
    path('InstrumentComparesave', report.views.InstrumentComparesave, name="InstrumentComparesave"),

    # 方法定量限与线性范围(LOQ)数据保存
    path('LOQsave', report.views.LOQsave, name="LOQsave"),
    
    path('mssave', report.views.MSsave, name="MSsave"),
    path('lodsave', report.views.LODsave, name="LODsave"),
    
    path('amr2save', report.views.AMR2save, name="AMR2save"),
    path('amr_conclusionsave', report.views.AMR_conclusionsave, name="AMR_conclusionsave"),
    path('crrsave', report.views.CRRsave, name="CRRsave"),
    path('SampleStabilitySave', report.views.Sample_Stability_Save, name="Sample_Stability_Save"),
    
    path('verifyagain/<int:id>', report.views.verifyagain, name="verifyagain"),
    path('returnback', report.views.returnback, name="returnback"),

    # 流程表单
    path('flowchart/<int:id>', report.views.get_flowchart_page, name="flowchart"),

    # 操作日志
    path('operatelog/<int:id>', report.views.get_operatelog_page, name="operatelog"),

    # 报告提交和审核
    path('submitcheck/<int:id>/<str:checklevel>', report.views.submitcheck, name="submitcheck"),



    # 使用说明
    path('instructions', report.views.instructions, name="instructions"),



    # 仪器比对报告生成系统
    path('ICS_index', report.views.ICS_index, name="ICS_index"),

    # 定量项目仪器比对报告
    path('ICS/QuantitativeReports', report.views.ICS_QuantitativeReports, name="ICS_QuantitativeReports"),

    # 仪器比对报告生成系统 - 新建报告
    path('ICS/QuantitativeReports/Create', report.views.ICS_QuantitativeReports_Create, name="ICS_QuantitativeReports_Create"),

    # 仪器比对报告生成系统 - 新建报告 - 点击数据提交按钮后进入结果编辑页面
    path('ICS/QuantitativeReports/Edit', report.views.ICS_QuantitativeReports_Edit, name="ICS_QuantitativeReports_Edit"),

    # 仪器比对报告生成系统 - 新建报告 - 点击数据提交按钮后进入结果编辑页面
    path('ICS/QuantitativeReports/Save', report.views.ICS_QuantitativeReports_Save, name="ICS_QuantitativeReports_Save"),

    # 仪器比对报告生成系统 - 报告预览
    path('ICS/QuantitativeReports/<int:id>/<str:operation>', report.views.ICS_QuantitativeReports_Operate, name="ICS_QuantitativeReports"),

    # 仪器比对报告生成系统 - 报告删除
    path('ICS/QuantitativeReports/delete/<int:id>', report.views.ICS_QuantitativeReports_Delete, name="ICS_QuantitativeReports_Delete"),

    # 仪器比对报告生成系统 - 项目参数设置
    path('ICS/ProjectParameters', report.views.ICS_ProjectParameters, name="ICS_ProjectParameters"),

    # 仪器比对报告生成系统 - 新建参数设置
    path('ICS/ProjectParameters/Create', report.views.ICS_ProjectParameters_Create, name="ICS_ProjectParameters_Create"),

    # 仪器比对报告生成系统 - 项目参数设置 - 编辑
    path('ICS/ProjectParameters/Edit/<int:id>', report.views.ICS_ProjectParameters_Edit, name="ICS_ProjectParameters_Edit"),

    # 仪器比对报告生成系统 - 项目参数设置 - 编辑后保存
    path('ICS/ProjectParameters/EditSave', report.views.ICS_ProjectParameters_EditSave, name="ICS_ProjectParameters_EditSave"),
    
    # 仪器比对报告生成系统 - 新建参数设置 - 保存
    path('ICS/ProjectParameters/Save', report.views.ICS_ProjectParameters_Save, name="ICS_ProjectParameters_Save"),

    # path('upload', report.views.picture_upload, name="upload"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

