// @ts-ignore
/* eslint-disable */
import { request } from 'umi';

/** 查询漏洞数量信息 GET /api/charts/total/ */
export async function vulsTotal() {

  return request<API2.VulTotal>('/api/charts/total/', {
    method: 'GET',
  });
}

/** 查询漏洞数量已项目归类 GET /api/charts/total/ */
export async function vulsTotalByItem() {

  return request<API2.VulTotal>('/api/charts/totalByItem/', {
    method: 'GET',
  });
}

/** 查询漏洞数量已类型归类 GET /api/charts/totalByType/ */
export async function vulsTotalByType() {

  return request<API2.VulTotalByType>('/api/charts/totalByType/', {
    method: 'GET',
  });
}

/** 查询漏洞数量已日期增长 GET /api/charts/totalByTimeRise/ */
export async function vulsTotalByTimeRise() {

  return request<API2.VulTotalByTime>('/api/charts/totalByTimeRise/', {
    method: 'GET',
  });
}

/** 查询漏洞修复率已日期增长 GET /api/charts/totalByTimeFix/ */
export async function vulsTotalByTimeFix() {

  return request<API2.VulTotalByTimeFix>('/api/charts/totalByTimeFix/', {
    method: 'GET',
  });
}
