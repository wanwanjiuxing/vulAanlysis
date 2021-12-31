// @ts-ignore
/* eslint-disable */
import { request } from 'umi';


/** 查询漏洞列表 GET /api/qiboVulList/ */
export async function vulList() {

  return request<API.VulList>('http://vuls.xiaowulaile.com:18888/api/qiboVulList/', {
    method: 'GET',
  });
}

/** 新建漏洞 POST /api/qiboVulList/ */
export async function addVul(options?: any) {
  console.log(JSON.stringify(options))
  return request<API.VulListItem>('http://vuls.xiaowulaile.com:18888/api/qiboVulList/', {
    method: 'POST',
    body: JSON.stringify(options),
  });
}

/** 删除漏洞 DELETE /api/qiboVulList/ */
export async function removeVul(options?: { [key: string]: any }) {
  console.log(options)
  options?.key.forEach((val:any) => {
    return request<Record<string, any>>('http://vuls.xiaowulaile.com:18888/api/qiboVulList/' + val.toString() +'/', {
      method: 'DELETE',
    });
  })

}

/** 更新漏洞 PUT /api/qiboVulList/ */
export async function updateVul(options?: any) {
  console.log(JSON.stringify(options));
  return request<API.VulListItem>('http://vuls.xiaowulaile.com:18888/api/qiboVulList/'+ options.vul_id + '/', {
    method: 'PUT',
    body: JSON.stringify(options),
  });
}

