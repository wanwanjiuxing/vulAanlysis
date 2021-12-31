// @ts-ignore
/* eslint-disable */
import { request } from 'umi';

/** 查询漏洞数量信息 GET /api/charts/total/ */
export async function vulsTotal() {

  return request<API.VulTotal>('http://vuls.xiaowulaile.com:18888/api/charts/total/', {
    method: 'GET',
  });
}
