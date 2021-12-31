// @ts-ignore
/* eslint-disable */
import { request } from 'umi';

/** 查询漏洞数量信息 GET /api/charts/total/ */
export async function vulsTotal() {

  return request<API2.VulTotal>('http://vuls.xiaowulaile.com:18888/api/charts/total/', {
    method: 'GET',
  });
}

/** 查询漏洞数量已项目归类 GET /api/charts/total/ */
export async function vulsTotalByItem() {

  return request<API2.VulTotal>('http://vuls.xiaowulaile.com:18888/api/charts/totalByItem/', {
    method: 'GET',
  });
}

/** 查询漏洞数量已类型归类 GET /api/charts/totalByType/ */
export async function vulsTotalByType() {

  return request<API2.VulTotalByType>('http://vuls.xiaowulaile.com:18888/api/charts/totalByType/', {
    method: 'GET',
  });
}

/** 查询漏洞数量已日期增长 GET /api/charts/totalByTimeRise/ */
export async function vulsTotalByTimeRise() {

  return request<API2.VulTotalByTime>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeRise/', {
    method: 'GET',
  });
}

/** 查询漏洞修复率已日期增长 GET /api/charts/totalByTimeFix/ */
export async function vulsTotalByTimeFix() {

  return request<API2.VulTotalByTimeFix>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeFix/', {
    method: 'GET',
  });
}

/** 查询漏洞增长趋势by时间--漏洞类型：输入输出 GET /api/charts/totalByTimeType1Rise/ */
export async function vulsTotalByTimeType1Rise() {

  return request<API2.VulTotalByTime>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeType1Rise/', {
    method: 'GET',
  });
}
/** 查询漏洞增长趋势by时间--漏洞类型：用户权限 GET /api/charts/totalByTimeType2Rise/ */
export async function vulsTotalByTimeType2Rise() {

  return request<API2.VulTotalByTime>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeType2Rise/', {
    method: 'GET',
  });
}
/** 查询漏洞增长趋势by时间--漏洞类型：第三方组件 GET /api/charts/totalByTimeType3Rise/ */
export async function vulsTotalByTimeType3Rise() {

  return request<API2.VulTotalByTime>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeType3Rise/', {
    method: 'GET',
  });
}
/** 查询漏洞增长趋势by时间--漏洞类型：安全配置 GET /api/charts/totalByTimeType4Rise/ */
export async function vulsTotalByTimeType4Rise() {

  return request<API2.VulTotalByTime>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeType4Rise/', {
    method: 'GET',
  });
}
/** 查询漏洞增长趋势by时间--漏洞类型：文件上传下载 GET /api/charts/totalByTimeType5Rise/ */
export async function vulsTotalByTimeType5Rise() {

  return request<API2.VulTotalByTime>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeType5Rise/', {
    method: 'GET',
  });
}
/** 查询漏洞增长趋势by时间--漏洞类型：命令执行&代码执行 GET /api/charts/totalByTimeType6Rise/ */
export async function vulsTotalByTimeType6Rise() {

  return request<API2.VulTotalByTime>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeType6Rise/', {
    method: 'GET',
  });
}
/** 查询漏洞增长趋势by时间--漏洞类型：业务逻辑 GET /api/charts/totalByTimeType7Rise/ */
export async function vulsTotalByTimeType7Rise() {

  return request<API2.VulTotalByTime>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeType7Rise/', {
    method: 'GET',
  });
}
/** 查询漏洞增长趋势by时间--漏洞类型：弱口令 GET /api/charts/totalByTimeType8Rise/ */
export async function vulsTotalByTimeType8Rise() {

  return request<API2.VulTotalByTime>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeType8Rise/', {
    method: 'GET',
  });
}
/** 查询漏洞增长趋势by时间--漏洞类型：其他 GET /api/charts/totalByTimeType9Rise/ */
export async function vulsTotalByTimeType9Rise() {

  return request<API2.VulTotalByTime>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeType9Rise/', {
    method: 'GET',
  });
}

/** 查询漏洞修复趋势by时间--项目：有课 GET /api/charts/totalByTimeFixItem1/ */
export async function vulsTotalByTimeFixItem1() {

  return request<API2.VulTotalByTimeFix>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeFixItem1/', {
    method: 'GET',
  });
}
/** 查询漏洞修复趋势by时间--项目：官网 GET /api/charts/totalByTimeFixItem2/ */
export async function vulsTotalByTimeFixItem2() {

  return request<API2.VulTotalByTimeFix>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeFixItem2/', {
    method: 'GET',
  });
}
/** 查询漏洞修复趋势by时间--项目：企播 GET /api/charts/totalByTimeFixItem3/ */
export async function vulsTotalByTimeFixItem3() {

  return request<API2.VulTotalByTimeFix>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeFixItem3/', {
    method: 'GET',
  });
}
/** 查询漏洞修复趋势by时间--项目：直播 GET /api/charts/totalByTimeFixItem4/ */
export async function vulsTotalByTimeFixItem4() {

  return request<API2.VulTotalByTimeFix>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeFixItem4/', {
    method: 'GET',
  });
}
/** 查询漏洞修复趋势by时间--项目：目睹云 GET /api/charts/totalByTimeFixItem5/ */
export async function vulsTotalByTimeFixItem5() {

  return request<API2.VulTotalByTimeFix>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeFixItem5/', {
    method: 'GET',
  });
}
/** 查询漏洞修复趋势by时间--项目：MDN GET /api/charts/totalByTimeFixItem6/ */
export async function vulsTotalByTimeFixItem6() {

  return request<API2.VulTotalByTimeFix>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeFixItem6/', {
    method: 'GET',
  });
}
/** 查询漏洞修复趋势by时间--项目：MDC GET /api/charts/totalByTimeFixItem7/ */
export async function vulsTotalByTimeFixItem7() {

  return request<API2.VulTotalByTimeFix>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeFixItem7/', {
    method: 'GET',
  });
}
/** 查询漏洞修复趋势by时间--项目：互联网 GET /api/charts/totalByTimeFixItem8/ */
export async function vulsTotalByTimeFixItem8() {

  return request<API2.VulTotalByTimeFix>('http://vuls.xiaowulaile.com:18888/api/charts/totalByTimeFixItem8/', {
    method: 'GET',
  });
}


