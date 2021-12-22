import { PageContainer,} from '@ant-design/pro-layout';
import React,{useState} from "react";
import { Line } from '@ant-design/charts';
import {  Card,Table } from 'antd';
import { vulsTotal } from '@/services/charts/chartsApi'

const vulsTotalData =await vulsTotal();


const VulFixCharts: React.FC = () => {



  const data = [
    { year: '1911', value: 3 },
    { year: '1992', value: 4 },
    { year: '1993', value: 3.5 },
    { year: '1994', value: 5 },
    { year: '1995', value: 4.9 },
    { year: '1996', value: 6 },
    { year: '1997', value: 7 },
    { year: '1998', value: 9 },
    { year: '1999', value: 13 },
  ];
  const config = {
    data,
    height: 400,
    xField: 'year',
    yField: 'value',
    point: {
      size: 5,
      shape: 'diamond',
    },
  };



  const tabListNoTitle = [
    {
      key: 'analysis1',
      tab: '目睹漏洞修复情况统计',
    },
    {
      key: 'analysis2',
      tab: '目睹漏洞类型统计',
    },
    {
      key: 'analysis3',
      tab: '目睹漏洞增长趋势图',
    },
    {
      key: 'analysis4',
      tab: '目睹漏洞修复趋势图',
    },
  ];

  const contentListNoTitle = {
    analysis1: <Line {...config} />,
    analysis2: <Line {...config} />,
    analysis3: <Line {...config} />,
    analysis4: <Line {...config} />,
  };

  const [activeTabKey2, setActiveTabKey2] = useState('analysis1');

  const onTab2Change = key => {
    setActiveTabKey2(key);
  };

  const muduVulData = [
    {
      vulsAmount: vulsTotalData?.data?.vulsAmount,
      fixedAmount: vulsTotalData?.data?.fixedAmount,
      fixingAmount: vulsTotalData?.data?.fixingAmount,
      fixedRate: vulsTotalData?.data?.fixedRate,
    },
  ];

  const muduVulDataColumns = [
    {
      title: '漏洞数量',
      dataIndex: 'vulsAmount',
      key: 'vulsAmount',
    },
    {
      title: '已整改数量',
      dataIndex: 'fixedAmount',
      key: 'fixedAmount',
    },
    {
      title: '未整改数量',
      dataIndex: 'fixingAmount',
      key: 'fixingAmount',
    },
    {
      title: '整改率',
      dataIndex: 'fixedRate',
      key: 'fixedRate',
    },
  ];



  return (
    <PageContainer>
      <Card
        style={{ width: '100%' }}
        title="自查漏洞修复进度汇总"
      >
        <Table dataSource={muduVulData} columns={muduVulDataColumns} pagination={false} rowKey={muduVulDataColumns[0].dataIndex} />
      </Card>
      <br/>
      <br/>
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
