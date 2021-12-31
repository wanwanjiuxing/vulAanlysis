import { PageContainer,} from '@ant-design/pro-layout';
import React,{useState} from "react";
import { Line } from '@ant-design/charts';
import {  Card } from 'antd';
import { vulsTotalByTimeType1Rise,vulsTotalByTimeType2Rise,vulsTotalByTimeType3Rise,vulsTotalByTimeType4Rise,vulsTotalByTimeType5Rise,vulsTotalByTimeType6Rise,vulsTotalByTimeType7Rise,vulsTotalByTimeType8Rise,vulsTotalByTimeType9Rise } from '@/services/charts/chartsApi'



const vulsTotalByTimeType1RiseData = await vulsTotalByTimeType1Rise();
const vulsTotalByTimeType2RiseData = await vulsTotalByTimeType2Rise();
const vulsTotalByTimeType3RiseData = await vulsTotalByTimeType3Rise();
const vulsTotalByTimeType4RiseData = await vulsTotalByTimeType4Rise();
const vulsTotalByTimeType5RiseData = await vulsTotalByTimeType5Rise();
const vulsTotalByTimeType6RiseData = await vulsTotalByTimeType6Rise();
const vulsTotalByTimeType7RiseData = await vulsTotalByTimeType7Rise();
const vulsTotalByTimeType8RiseData = await vulsTotalByTimeType8Rise();
const vulsTotalByTimeType9RiseData = await vulsTotalByTimeType9Rise();




const VulFixCharts: React.FC = () => {


  const data1 = vulsTotalByTimeType1RiseData?.data;
  const data2 = vulsTotalByTimeType2RiseData?.data;
  const data3 = vulsTotalByTimeType3RiseData?.data;
  const data4 = vulsTotalByTimeType4RiseData?.data;
  const data5 = vulsTotalByTimeType5RiseData?.data;
  const data6 = vulsTotalByTimeType6RiseData?.data;
  const data7 = vulsTotalByTimeType7RiseData?.data;
  const data8 = vulsTotalByTimeType8RiseData?.data;
  const data9 = vulsTotalByTimeType9RiseData?.data;


  const config1 = {
    data:data1,
    height: 400,
    xField: 'data_id',
    yField: 'vuls_amount',
    point: {
      size: 5,
      shape: 'diamond',
    },
    yAxis: {
      min: 0,
      max:20,
      tickCount: 11,
      tickInterval: 2,
    },
    meta: {
      data_id: {
        alias: '日期',
      },
      vuls_amount: {
        alias: '漏洞数量',
      },
    },
  };
  const config2 = {
    data:data2,
    height: 400,
    xField: 'data_id',
    yField: 'vuls_amount',
    point: {
      size: 5,
      shape: 'diamond',
    },
    yAxis: {
      min: 0,
      max:20,
      tickCount: 11,
      tickInterval: 2,
    },
    meta: {
      data_id: {
        alias: '日期',
      },
      vuls_amount: {
        alias: '漏洞数量',
      },
    },
  };
  const config3 = {
    data:data3,
    height: 400,
    xField: 'data_id',
    yField: 'vuls_amount',
    point: {
      size: 5,
      shape: 'diamond',
    },
    yAxis: {
      min: 0,
      max:20,
      tickCount: 11,
      tickInterval: 2,
    },
    meta: {
      data_id: {
        alias: '日期',
      },
      vuls_amount: {
        alias: '漏洞数量',
      },
    },
  };
  const config4 = {
    data:data4,
    height: 400,
    xField: 'data_id',
    yField: 'vuls_amount',
    point: {
      size: 5,
      shape: 'diamond',
    },
    yAxis: {
      min: 0,
      max:20,
      tickCount: 11,
      tickInterval: 2,
    },
    meta: {
      data_id: {
        alias: '日期',
      },
      vuls_amount: {
        alias: '漏洞数量',
      },
    },
  };
  const config5 = {
    data:data5,
    height: 400,
    xField: 'data_id',
    yField: 'vuls_amount',
    point: {
      size: 5,
      shape: 'diamond',
    },
    yAxis: {
      min: 0,
      max:20,
      tickCount: 11,
      tickInterval: 2,
    },
    meta: {
      data_id: {
        alias: '日期',
      },
      vuls_amount: {
        alias: '漏洞数量',
      },
    },
  };
  const config6 = {
    data:data6,
    height: 400,
    xField: 'data_id',
    yField: 'vuls_amount',
    point: {
      size: 5,
      shape: 'diamond',
    },
    yAxis: {
      min: 0,
      max:20,
      tickCount: 11,
      tickInterval: 2,
    },
    meta: {
      data_id: {
        alias: '日期',
      },
      vuls_amount: {
        alias: '漏洞数量',
      },
    },
  };
  const config7 = {
    data:data7,
    height: 400,
    xField: 'data_id',
    yField: 'vuls_amount',
    point: {
      size: 5,
      shape: 'diamond',
    },
    yAxis: {
      min: 0,
      max:20,
      tickCount: 11,
      tickInterval: 2,
    },
    meta: {
      data_id: {
        alias: '日期',
      },
      vuls_amount: {
        alias: '漏洞数量',
      },
    },
  };
  const config8 = {
    data:data8,
    height: 400,
    xField: 'data_id',
    yField: 'vuls_amount',
    point: {
      size: 5,
      shape: 'diamond',
    },
    yAxis: {
      min: 0,
      max:20,
      tickCount: 11,
      tickInterval: 2,
    },
    meta: {
      data_id: {
        alias: '日期',
      },
      vuls_amount: {
        alias: '漏洞数量',
      },
    },
  };
  const config9 = {
    data:data9,
    height: 400,
    xField: 'data_id',
    yField: 'vuls_amount',
    point: {
      size: 5,
      shape: 'diamond',
    },
    yAxis: {
      min: 0,
      max:20,
      tickCount: 11,
      tickInterval: 2,
    },
    meta: {
      data_id: {
        alias: '日期',
      },
      vuls_amount: {
        alias: '漏洞数量',
      },
    },
  };



  const tabListNoTitle = [
    {
      key: 'type1',
      tab: '输入输出',
    },
    {
      key: 'type2',
      tab: '用户权限',
    },
    {
      key: 'type3',
      tab: '第三方组件',
    },
    {
      key: 'type4',
      tab: '安全配置',
    },
    {
      key: 'type5',
      tab: '文件上传下载',
    },
    {
      key: 'type6',
      tab: '命令执行&代码执行',
    },
    {
      key: 'type7',
      tab: '业务逻辑',
    },
    {
      key: 'type8',
      tab: '弱口令',
    },
    {
      key: 'type9',
      tab: '其他',
    },
  ];
  const contentListNoTitle = {
    type1: <Line {...config1} />,
    type2: <Line {...config2} />,
    type3: <Line {...config3} />,
    type4: <Line {...config4} />,
    type5: <Line {...config5} />,
    type6: <Line {...config6} />,
    type7: <Line {...config7} />,
    type8: <Line {...config8} />,
    type9: <Line {...config9} />,
  };

  const [activeTabKey2, setActiveTabKey2] = useState('type1');

  const onTab2Change = (key) => {
    setActiveTabKey2(key);
  };

  return (
    <PageContainer>
      <Card
        style={{ width: '100%' }}
        tabList={tabListNoTitle}
        activeTabKey={activeTabKey2}
        onTabChange={key => {
          onTab2Change(key);
        }}
      >
        {contentListNoTitle[activeTabKey2]}
      </Card>
    </PageContainer>
  )
};

export default VulFixCharts;
