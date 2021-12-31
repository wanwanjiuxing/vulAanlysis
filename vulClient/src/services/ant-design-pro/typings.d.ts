// @ts-ignore
/* eslint-disable */

declare namespace API {
  type CurrentUser = {
    username?: string;
    access?: string;
  };

  type LoginResult = {
    success?: string;
    data?: LoginResultItem[];
  };
  type LoginResultItem = {
    username?: string;
    access?: string;
  };

  type PageParams = {
    current?: number;
    pageSize?: number;
  };

  type RuleListItem = {
    key?: number;
    disabled?: boolean;
    href?: string;
    avatar?: string;
    name?: string;
    owner?: string;
    desc?: string;
    callNo?: number;
    status?: number;
    updatedAt?: string;
    createdAt?: string;
    progress?: number;
  };

  type VulListItem = {
    vul_id?: string;
    vul_name?: string;
    vul_jira?: string;
    vul_sendto?: string;
    vul_fixer?: string;
    vul_sendtime?: string;
    vul_estimatefixedtime?: string;
    vul_fixedtime?: string;
    vul_isfixed?: number;
    vul_type?: number;
    vul_remarks?: string;
  };

  type RuleList = {
    data?: RuleListItem[];
    /** 列表的内容总数 */
    total?: number;
    success?: boolean;
  };

  type VulList = {
    success?: string;
    data?: VulListItem[];
  };
  type VulTotal = {
    success?: string;
    data?: VulTotalItem[];
  };
  type VulTotalItem = {
    vulsAmount?: number;
    fixedAmount?: number;
    fixingAmount?: number;
    fixedRate?: string;
  };

  type VulTotalByItem = {
    success?: string;
    data?: VulTotalByItemList[];
  };
  type VulTotalByItemList = {
    item?: string;
    fixedAmount?: number;
    fixingAmount?: number;
    fixedRate?: string;
  };

  type FakeCaptcha = {
    code?: number;
    status?: string;
  };

  type LoginParams = {
    username?: string;
    password?: string;
  };

  type ErrorResponse = {
    /** 业务约定的错误码 */
    errorCode: string;
    /** 业务上的错误信息 */
    errorMessage?: string;
    /** 业务上的请求是否成功 */
    success?: boolean;
  };

  type NoticeIconList = {
    data?: NoticeIconItem[];
    /** 列表的内容总数 */
    total?: number;
    success?: boolean;
  };

  type NoticeIconItemType = 'notification' | 'message' | 'event';

  type NoticeIconItem = {
    id?: string;
    extra?: string;
    key?: string;
    read?: boolean;
    avatar?: string;
    title?: string;
    status?: string;
    datetime?: string;
    description?: string;
    type?: NoticeIconItemType;
  };
}
