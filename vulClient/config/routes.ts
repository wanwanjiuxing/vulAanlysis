export default [
  {
    path: '/user',
    layout: false,
    routes: [
      {
        path: '/user',
        routes: [
          {
            name: 'login',
            path: '/user/login',
            component: './user/Login',
          },
        ],
      },
      {
        component: './404',
      },
    ],
  },
  {
    path: '/welcome',
    name: 'welcome',
    icon: 'smile',
    component: './Welcome',
  },
  {
    path: '/charts',
    name: 'charts',
    icon: 'table',
    routes: [
      {
        path: '/charts/vulFixCharts',
        name: 'vulFix',
        icon: 'smile',
        component: './charts/VulFixCharts',
      },
      // {
      //   path: '/charts/vulType',
      //   name: 'vulType',
      //   icon: 'smile',
      //   component: './charts/VulType',
      // },
      {
        component: './404',
      },
    ],
  },
  {
    path: '/vuls',
    name: 'vuls',
    icon: 'table',
    routes: [
      {
        path: '/vuls/total',
        name: 'total',
        icon: 'smile',
        component: './VulList',
      },
      {
        path: '/vuls/youke',
        name: 'youke',
        icon: 'smile',
        component: './YoukeVulList',
      },
      {
        path: '/vuls/qibo',
        name: 'qibo',
        icon: 'smile',
        component: './QiboVulList',
      },
      {
        path: '/vuls/zhibo',
        name: 'zhibo',
        icon: 'smile',
        component: './ZhiboVulList',
      },
      {
        path: '/vuls/myun',
        name: 'myun',
        icon: 'smile',
        component: './MyunVulList',
      },
      {
        path: '/vuls/mdn',
        name: 'mdn',
        icon: 'smile',
        component: './MdnVulList',
      },
      {
        path: '/vuls/mdc',
        name: 'mdc',
        icon: 'smile',
        component: './MdcVulList',
      },
      {
        path: '/vuls/other',
        name: 'other',
        icon: 'smile',
        component: './OtherVulList',
      },
      {
        component: './404',
      },
    ],
  },

  // {
  //   name: 'list.table-list',
  //   icon: 'table',
  //   path: '/list',
  //   component: './TableList',
  // },
  // {
  //   name: 'list.vul-list',
  //   icon: 'table',
  //   path: '/vullist',
  //   component: './VulList',
  // },
  {
    path: '/',
    redirect: '/welcome',
  },
  {
    component: './404',
  },
];
