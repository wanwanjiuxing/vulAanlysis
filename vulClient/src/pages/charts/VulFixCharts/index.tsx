import { PageContainer,} from '@ant-design/pro-layout';
import React,{useState} from "react";
import { DualAxes,Column,Line } from '@ant-design/charts';
import {  Card,Table } from 'antd';
import { vulsTotal,vulsTotalByItem,vulsTotalByType,vulsTotalByTimeRise,vulsTotalByTimeFix } from '@/services/charts/chartsApi'

const vulsTotalData =await vulsTotal();

const vulsTotalByItemData =await vulsTotalByItem();

const vulsTotalByTypeData =await vulsTotalByType();

const vulsTotalByTimeRiseData = await vulsTotalByTimeRise();

const vulsTotalByTimeFixData = await vulsTotalByTimeFix();


const VulFixCharts: React.FC = () => {

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
  const amountData = [
    {
      item: vulsTotalByItemData?.data[0].item,
      value: vulsTotalByItemData?.data[0].fixingAmount,
      type: '未整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[1].item,
      value: vulsTotalByItemData?.data[1].fixingAmount,
      type: '未整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[2].item,
      value: vulsTotalByItemData?.data[2].fixingAmount,
      type: '未整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[3].item,
      value: vulsTotalByItemData?.data[3].fixingAmount,
      type: '未整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[4].item,
      value: vulsTotalByItemData?.data[4].fixingAmount,
      type: '未整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[5].item,
      value: vulsTotalByItemData?.data[5].fixingAmount,
      type: '未整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[6].item,
      value: vulsTotalByItemData?.data[6].fixingAmount,
      type: '未整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[0].item,
      value: vulsTotalByItemData?.data[0].fixedAmount,
      type: '已整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[1].item,
      value: vulsTotalByItemData?.data[1].fixedAmount,
      type: '已整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[2].item,
      value: vulsTotalByItemData?.data[2].fixedAmount,
      type: '已整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[3].item,
      value: vulsTotalByItemData?.data[3].fixedAmount,
      type: '已整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[4].item,
      value: vulsTotalByItemData?.data[4].fixedAmount,
      type: '已整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[5].item,
      value: vulsTotalByItemData?.data[5].fixedAmount,
      type: '已整改漏洞',
    },
    {
      item: vulsTotalByItemData?.data[6].item,
      value: vulsTotalByItemData?.data[6].fixedAmount,
      type: '已整改漏洞',
    },
  ];
  const rateData = [
    {
      item: vulsTotalByItemData?.data[0].item,
      rate: vulsTotalByItemData?.data[0].fixedRate,
    },
    {
      item: vulsTotalByItemData?.data[1].item,
      rate: vulsTotalByItemData?.data[1].fixedRate,
    },
    {
      item: vulsTotalByItemData?.data[2].item,
      rate: vulsTotalByItemData?.data[2].fixedRate,
    },
    {
      item: vulsTotalByItemData?.data[3].item,
      rate: vulsTotalByItemData?.data[3].fixedRate,
    },
    {
      item: vulsTotalByItemData?.data[4].item,
      rate: vulsTotalByItemData?.data[4].fixedRate,
    },
    {
      item: vulsTotalByItemData?.data[5].item,
      rate: vulsTotalByItemData?.data[5].fixedRate,
    },
    {
      item: vulsTotalByItemData?.data[6].item,
      rate: vulsTotalByItemData?.data[6].fixedRate,
    },
  ];
  const config1 = {
    data: [amountData, rateData],
    xField: 'item',
    yField: ['value', 'rate'],
    yAxis: {
      rate:{
        min: 0,
        max: 100,
        minLimit:0,
        maxLimit: 100,
        tickCount: 11,
      },
      value:{
        tickCount: 11,
      },
    },
    meta: {
      item: {
        alias: '类别',
      },
      value: {
        alias: '漏洞数量',
      },
      rate: {
        alias: '漏洞整改率(%)',
      },
    },
    geometryOptions: [
      {
        geometry: 'column',
        isStack: true,
        seriesField: 'type',
      },
      {
        geometry: 'line',
        smooth: true,
      },
    ],
  };

  const data2 = vulsTotalByTypeData?.data;
  const config2 = {
    data:data2,
    xField: 'item',
    yField: 'amount',
    yAxis: {
      min: 0,
      minLimit:0,
      tickCount: 11,
    },
    meta: {
      item: {
        alias: '类别',
      },
      amount: {
        alias: '数量',
      },
    },
  };

  const data3 = vulsTotalByTimeRiseData?.data;
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
      minLimit:0,
      tickCount: 11,
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

  const amountData4 = vulsTotalByTimeFixData?.data?.data1;
  const rateData4 = vulsTotalByTimeFixData?.data?.data2;
  const config4 = {
    data: [amountData4, rateData4],
    xField: 'item',
    yField: ['value', 'rate'],
    yAxis: {
      rate:{
        min: 0,
        max: 100,
        minLimit:0,
        maxLimit: 100,
        tickCount: 11,
      },
      value:{
        tickCount: 11,
      },
    },
    meta: {
      item: {
        alias: '日期',
      },
      value: {
        alias: '数量',
      },
      rate: {
        alias: '未修复率(%)',
      },
    },
    geometryOptions: [
      {
        geometry: 'column',
        isStack: true,
        seriesField: 'type',

      },
      {
        geometry: 'line',
        smooth: true,
      },
    ],
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
    analysis1: <DualAxes {...config1} />,
    analysis2: <Column {...config2} />,
    analysis3: <Line {...config3} />,
    analysis4: <DualAxes {...config4} />,
  };

  const [activeTabKey2, setActiveTabKey2] = useState('analysis1');

  const onTab2Change = (key) => {
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
