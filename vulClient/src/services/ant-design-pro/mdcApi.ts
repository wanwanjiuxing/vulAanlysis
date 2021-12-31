// @ts-ignore
/* eslint-disable */
import { request } from 'umi';


/** 查询漏洞列表 GET /api/mdcVulList/ */
export async function vulList() {

  return request<API.VulList>('http://vuls.xiaowulaile.com:18888/api/mdcVulList/', {
    method: 'GET',
  });
}

/** 新建漏洞 POST /api/mdcVulList/ */
export async function addVul(options?: any) {
  console.log(JSON.stringify(options))
  return request<API.VulListItem>('http://vuls.xiaowulaile.com:18888/api/mdcVulList/', {
    method: 'POST',
    body: JSON.stringify(options),
  });
}

/** 删除漏洞 DELETE /api/mdcVulList/ */
export async function removeVul(options?: { [key: string]: any }) {
  console.log(options)
  options?.key.forEach((val:any) => {
    return request<Record<string, any>>('http://vuls.xiaowulaile.com:18888/api/mdcVulList/' + val.toString() +'/', {
      method: 'DELETE',
    });
  })

}

/** 更新漏洞 PUT /api/mdcVulList/ */
export async function updateVul(options?: any) {
  console.log(JSON.stringify(options));
  return request<API.VulListItem>('http://vuls.xiaowulaile.com:18888/api/mdcVulList/'+ options.vul_id + '/', {
    method: 'PUT',
    body: JSON.stringify(options),
  });
}

