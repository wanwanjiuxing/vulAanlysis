// @ts-ignore
/* eslint-disable */
import { request } from 'umi';


/** 查询漏洞列表 GET /api/mdnVulList/ */
export async function vulList() {

  return request<API.VulList>('/api/mdnVulList/', {
    method: 'GET',
  });
}

/** 新建漏洞 POST /api/mdnVulList/ */
export async function addVul(options?: any) {
  console.log(JSON.stringify(options))
  return request<API.VulListItem>('/api/mdnVulList/', {
    method: 'POST',
    body: JSON.stringify(options),
  });
}

/** 删除漏洞 DELETE /api/mdnVulList/ */
export async function removeVul(options?: { [key: string]: any }) {
  console.log(options)
  options?.key.forEach((val:any) => {
    return request<Record<string, any>>('/api/mdnVulList/' + val.toString() +'/', {
      method: 'DELETE',
    });
  })

}

/** 更新漏洞 PUT /api/mdnVulList/ */
export async function updateVul(options?: any) {
  console.log(JSON.stringify(options));
  return request<API.VulListItem>('/api/mdnVulList/'+ options.vul_id + '/', {
    method: 'PUT',
    body: JSON.stringify(options),
  });
}

