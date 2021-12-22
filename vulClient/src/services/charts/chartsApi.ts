// @ts-ignore
/* eslint-disable */
import { request } from 'umi';

/** 查询漏洞数量信息 GET /api/charts/total/ */
export async function vulsTotal() {

  return request<API2.VulTotal>('/api/charts/total/', {
    method: 'GET',
  });
}
