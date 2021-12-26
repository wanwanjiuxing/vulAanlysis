from django.db import models

# Create your models here.
class Youke_VulModel(models.Model):
    vul_id = models.CharField(max_length=128,verbose_name="漏洞编号",default="0000000000")
    vul_name = models.CharField(max_length=128,verbose_name="漏洞名称",default="默认漏洞")
    vul_jira = models.CharField(max_length=128,verbose_name="Jira工单编号",default="默认jira工单")
    vul_sendto = models.CharField(max_length=128,verbose_name="发送对象",default="默认")
    vul_fixer = models.CharField(max_length=128,verbose_name="整改人员",default="默认")
    vul_sendtime = models.CharField(max_length=128,verbose_name="发送时间",default="2020-10-10 01:01:00")
    vul_estimatefixedtime = models.CharField(max_length=128,verbose_name="预计修复时间",default="2020-10-10 01:01:00")
    vul_fixedtime = models.CharField(max_length=128,verbose_name="完成修复时间",default="2020-10-10 01:01:00")
    vul_isfixed = models.IntegerField(verbose_name="是否修复",default=0)
    vul_type = models.IntegerField(verbose_name="漏洞类型",default=0)
    vul_remarks = models.CharField(max_length=128,verbose_name="备注",default="--")


class Zhibo_VulModel(models.Model):
    vul_id = models.CharField(max_length=128,verbose_name="漏洞编号",default="0000000000")
    vul_name = models.CharField(max_length=128,verbose_name="漏洞名称",default="默认漏洞")
    vul_jira = models.CharField(max_length=128,verbose_name="Jira工单编号",default="默认jira工单")
    vul_sendto = models.CharField(max_length=128,verbose_name="发送对象",default="默认")
    vul_fixer = models.CharField(max_length=128,verbose_name="整改人员",default="默认")
    vul_sendtime = models.CharField(max_length=128,verbose_name="发送时间",default="2020-10-10 01:01:00")
    vul_estimatefixedtime = models.CharField(max_length=128,verbose_name="预计修复时间",default="2020-10-10 01:01:00")
    vul_fixedtime = models.CharField(max_length=128,verbose_name="完成修复时间",default="2020-10-10 01:01:00")
    vul_isfixed = models.IntegerField(verbose_name="是否修复",default=0)
    vul_type = models.IntegerField(verbose_name="漏洞类型",default=0)
    vul_remarks = models.CharField(max_length=128,verbose_name="备注",default="--")

class Qibo_VulModel(models.Model):
    vul_id = models.CharField(max_length=128,verbose_name="漏洞编号",default="0000000000")
    vul_name = models.CharField(max_length=128,verbose_name="漏洞名称",default="默认漏洞")
    vul_jira = models.CharField(max_length=128,verbose_name="Jira工单编号",default="默认jira工单")
    vul_sendto = models.CharField(max_length=128,verbose_name="发送对象",default="默认")
    vul_fixer = models.CharField(max_length=128,verbose_name="整改人员",default="默认")
    vul_sendtime = models.CharField(max_length=128,verbose_name="发送时间",default="2020-10-10 01:01:00")
    vul_estimatefixedtime = models.CharField(max_length=128,verbose_name="预计修复时间",default="2020-10-10 01:01:00")
    vul_fixedtime = models.CharField(max_length=128,verbose_name="完成修复时间",default="2020-10-10 01:01:00")
    vul_isfixed = models.IntegerField(verbose_name="是否修复",default=0)
    vul_type = models.IntegerField(verbose_name="漏洞类型",default=0)
    vul_remarks = models.CharField(max_length=128,verbose_name="备注",default="--")

class Myun_VulModel(models.Model):
    vul_id = models.CharField(max_length=128,verbose_name="漏洞编号",default="0000000000")
    vul_name = models.CharField(max_length=128,verbose_name="漏洞名称",default="默认漏洞")
    vul_jira = models.CharField(max_length=128,verbose_name="Jira工单编号",default="默认jira工单")
    vul_sendto = models.CharField(max_length=128,verbose_name="发送对象",default="默认")
    vul_fixer = models.CharField(max_length=128,verbose_name="整改人员",default="默认")
    vul_sendtime = models.CharField(max_length=128,verbose_name="发送时间",default="2020-10-10 01:01:00")
    vul_estimatefixedtime = models.CharField(max_length=128,verbose_name="预计修复时间",default="2020-10-10 01:01:00")
    vul_fixedtime = models.CharField(max_length=128,verbose_name="完成修复时间",default="2020-10-10 01:01:00")
    vul_isfixed = models.IntegerField(verbose_name="是否修复",default=0)
    vul_type = models.IntegerField(verbose_name="漏洞类型",default=0)
    vul_remarks = models.CharField(max_length=128,verbose_name="备注",default="--")

class Mdn_VulModel(models.Model):
    vul_id = models.CharField(max_length=128,verbose_name="漏洞编号",default="0000000000")
    vul_name = models.CharField(max_length=128,verbose_name="漏洞名称",default="默认漏洞")
    vul_jira = models.CharField(max_length=128,verbose_name="Jira工单编号",default="默认jira工单")
    vul_sendto = models.CharField(max_length=128,verbose_name="发送对象",default="默认")
    vul_fixer = models.CharField(max_length=128,verbose_name="整改人员",default="默认")
    vul_sendtime = models.CharField(max_length=128,verbose_name="发送时间",default="2020-10-10 01:01:00")
    vul_estimatefixedtime = models.CharField(max_length=128,verbose_name="预计修复时间",default="2020-10-10 01:01:00")
    vul_fixedtime = models.CharField(max_length=128,verbose_name="完成修复时间",default="2020-10-10 01:01:00")
    vul_isfixed = models.IntegerField(verbose_name="是否修复",default=0)
    vul_type = models.IntegerField(verbose_name="漏洞类型",default=0)
    vul_remarks = models.CharField(max_length=128,verbose_name="备注",default="--")

class Mdc_VulModel(models.Model):
    vul_id = models.CharField(max_length=128,verbose_name="漏洞编号",default="0000000000")
    vul_name = models.CharField(max_length=128,verbose_name="漏洞名称",default="默认漏洞")
    vul_jira = models.CharField(max_length=128,verbose_name="Jira工单编号",default="默认jira工单")
    vul_sendto = models.CharField(max_length=128,verbose_name="发送对象",default="默认")
    vul_fixer = models.CharField(max_length=128,verbose_name="整改人员",default="默认")
    vul_sendtime = models.CharField(max_length=128,verbose_name="发送时间",default="2020-10-10 01:01:00")
    vul_estimatefixedtime = models.CharField(max_length=128,verbose_name="预计修复时间",default="2020-10-10 01:01:00")
    vul_fixedtime = models.CharField(max_length=128,verbose_name="完成修复时间",default="2020-10-10 01:01:00")
    vul_isfixed = models.IntegerField(verbose_name="是否修复",default=0)
    vul_type = models.IntegerField(verbose_name="漏洞类型",default=0)
    vul_remarks = models.CharField(max_length=128,verbose_name="备注",default="--")

class Other_VulModel(models.Model):
    vul_id = models.CharField(max_length=128,verbose_name="漏洞编号",default="0000000000")
    vul_name = models.CharField(max_length=128,verbose_name="漏洞名称",default="默认漏洞")
    vul_jira = models.CharField(max_length=128,verbose_name="Jira工单编号",default="默认jira工单")
    vul_sendto = models.CharField(max_length=128,verbose_name="发送对象",default="默认")
    vul_fixer = models.CharField(max_length=128,verbose_name="整改人员",default="默认")
    vul_sendtime = models.CharField(max_length=128,verbose_name="发送时间",default="2020-10-10 01:01:00")
    vul_estimatefixedtime = models.CharField(max_length=128,verbose_name="预计修复时间",default="2020-10-10 01:01:00")
    vul_fixedtime = models.CharField(max_length=128,verbose_name="完成修复时间",default="2020-10-10 01:01:00")
    vul_isfixed = models.IntegerField(verbose_name="是否修复",default=0)
    vul_type = models.IntegerField(verbose_name="漏洞类型",default=0)
    vul_remarks = models.CharField(max_length=128,verbose_name="备注",default="--")

class Total_VulModel(models.Model):
    vul_id = models.CharField(max_length=128,verbose_name="漏洞编号",default="0000000000")
    vul_name = models.CharField(max_length=128,verbose_name="漏洞名称",default="默认漏洞")
    vul_jira = models.CharField(max_length=128,verbose_name="Jira工单编号",default="默认jira工单")
    vul_sendto = models.CharField(max_length=128,verbose_name="发送对象",default="默认")
    vul_fixer = models.CharField(max_length=128,verbose_name="整改人员",default="默认")
    vul_sendtime = models.CharField(max_length=128,verbose_name="发送时间",default="2020-10-10 01:01:00")
    vul_estimatefixedtime = models.CharField(max_length=128,verbose_name="预计修复时间",default="2020-10-10 01:01:00")
    vul_fixedtime = models.CharField(max_length=128,verbose_name="完成修复时间",default="2020-10-10 01:01:00")
    vul_isfixed = models.IntegerField(verbose_name="是否修复",default=0)
    vul_type = models.IntegerField(verbose_name="漏洞类型",default=0)
    vul_remarks = models.CharField(max_length=128,verbose_name="备注",default="--")

class Total_vulsRiseModel(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    vuls_amount = models.IntegerField(verbose_name="漏洞数量", default=0)
#    漏洞增长趋势图模型--输入输出
class Total_vulsRiseType1Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    vuls_amount = models.IntegerField(verbose_name="漏洞数量", default=0)
#    漏洞增长趋势图模型--用户权限
class Total_vulsRiseType2Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    vuls_amount = models.IntegerField(verbose_name="漏洞数量", default=0)
#    漏洞增长趋势图模型--第三方组件
class Total_vulsRiseType3Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    vuls_amount = models.IntegerField(verbose_name="漏洞数量", default=0)
#    漏洞增长趋势图模型--安全配置
class Total_vulsRiseType4Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    vuls_amount = models.IntegerField(verbose_name="漏洞数量", default=0)
#    漏洞增长趋势图模型--文件上传下载
class Total_vulsRiseType5Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    vuls_amount = models.IntegerField(verbose_name="漏洞数量", default=0)
#    漏洞增长趋势图模型--命令执行&代码执行
class Total_vulsRiseType6Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    vuls_amount = models.IntegerField(verbose_name="漏洞数量", default=0)
#    漏洞增长趋势图模型--业务逻辑
class Total_vulsRiseType7Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    vuls_amount = models.IntegerField(verbose_name="漏洞数量", default=0)
#    漏洞增长趋势图模型--弱口令
class Total_vulsRiseType8Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    vuls_amount = models.IntegerField(verbose_name="漏洞数量", default=0)
#    漏洞增长趋势图模型--其他
class Total_vulsRiseType9Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    vuls_amount = models.IntegerField(verbose_name="漏洞数量", default=0)

# 漏洞修复趋势图
class Total_vulsFixModel(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    fixed_amount = models.IntegerField(verbose_name="已整改漏洞", default=0)
    fixing_amount = models.IntegerField(verbose_name="未整改漏洞", default=0)

# 漏洞修复趋势图by项目--有课
class Total_vulsFixItem1Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    fixed_amount = models.IntegerField(verbose_name="已整改漏洞", default=0)
    fixing_amount = models.IntegerField(verbose_name="未整改漏洞", default=0)
# 漏洞修复趋势图by项目--官网
class Total_vulsFixItem2Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    fixed_amount = models.IntegerField(verbose_name="已整改漏洞", default=0)
    fixing_amount = models.IntegerField(verbose_name="未整改漏洞", default=0)
# 漏洞修复趋势图by项目--企播
class Total_vulsFixItem3Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    fixed_amount = models.IntegerField(verbose_name="已整改漏洞", default=0)
    fixing_amount = models.IntegerField(verbose_name="未整改漏洞", default=0)
# 漏洞修复趋势图by项目--直播
class Total_vulsFixItem4Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    fixed_amount = models.IntegerField(verbose_name="已整改漏洞", default=0)
    fixing_amount = models.IntegerField(verbose_name="未整改漏洞", default=0)
# 漏洞修复趋势图by项目--目睹云
class Total_vulsFixItem5Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    fixed_amount = models.IntegerField(verbose_name="已整改漏洞", default=0)
    fixing_amount = models.IntegerField(verbose_name="未整改漏洞", default=0)
# 漏洞修复趋势图by项目--MDN
class Total_vulsFixItem6Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    fixed_amount = models.IntegerField(verbose_name="已整改漏洞", default=0)
    fixing_amount = models.IntegerField(verbose_name="未整改漏洞", default=0)
# 漏洞修复趋势图by项目--MDC
class Total_vulsFixItem7Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    fixed_amount = models.IntegerField(verbose_name="已整改漏洞", default=0)
    fixing_amount = models.IntegerField(verbose_name="未整改漏洞", default=0)
# 漏洞修复趋势图by项目--互联网
class Total_vulsFixItem8Model(models.Model):
    data_id = models.CharField(max_length=128, verbose_name="日期", default="1/1")
    fixed_amount = models.IntegerField(verbose_name="已整改漏洞", default=0)
    fixing_amount = models.IntegerField(verbose_name="未整改漏洞", default=0)
