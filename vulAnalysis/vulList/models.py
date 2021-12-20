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
    vul_remarks = models.CharField(max_length=255,verbose_name="备注")

