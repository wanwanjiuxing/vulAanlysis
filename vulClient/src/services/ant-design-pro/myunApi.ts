// @ts-ignore
/* eslint-disable */
import { request } from 'umi';


/** 查询漏洞列表 GET /api/myunVulList/ */
export async function vulList() {

  return request<API.VulList>('http://vuls.xiaowulaile.com:18888/api/myunVulList/', {
    method: 'GET',
  });
}

/** 新建漏洞 POST /api/myunVulList/ */
export async function addVul(options?: any) {
  console.log(JSON.stringify(options))
  return request<API.VulListItem>('http://vuls.xiaowulaile.com:18888/api/myunVulList/', {
    method: 'POST',
    body: JSON.stringify(options),
  });
}

/** 删除漏洞 DELETE /api/myunVulList/ */
export async function removeVul(options?: { [key: string]: any }) {
  console.log(options)
  options?.key.forEach((val:any) => {
    return request<Record<string, any>>('http://vuls.xiaowulaile.com:18888/api/myunVulList/' + val.toString() +'/', {
      method: 'DELETE',
    });
  })

}

/** 更新漏洞 PUT /api/myunVulList/ */
export async function updateVul(options?: any) {
  console.log(JSON.stringify(options));
  return request<API.VulListItem>('http://vuls.xiaowulaile.com:18888/api/myunVulList/'+ options.vul_id + '/', {
    method: 'PUT',
    body: JSON.stringify(options),
  });
}

