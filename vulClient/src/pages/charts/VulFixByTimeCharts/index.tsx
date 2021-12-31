import { PageContainer,} from '@ant-design/pro-layout';
import React,{useState} from "react";
import { DualAxes } from '@ant-design/charts';
import {  Card } from 'antd';
import { vulsTotalByTimeFixItem1,vulsTotalByTimeFixItem2,vulsTotalByTimeFixItem3,vulsTotalByTimeFixItem4,vulsTotalByTimeFixItem5,vulsTotalByTimeFixItem6,vulsTotalByTimeFixItem7,vulsTotalByTimeFixItem8 } from '@/services/charts/chartsApi'


const vulsTotalByTimeFixItem1Data = await vulsTotalByTimeFixItem1();
const vulsTotalByTimeFixItem2Data = await vulsTotalByTimeFixItem2();
const vulsTotalByTimeFixItem3Data = await vulsTotalByTimeFixItem3();
const vulsTotalByTimeFixItem4Data = await vulsTotalByTimeFixItem4();
const vulsTotalByTimeFixItem5Data = await vulsTotalByTimeFixItem5();
const vulsTotalByTimeFixItem6Data = await vulsTotalByTimeFixItem6();
const vulsTotalByTimeFixItem7Data = await vulsTotalByTimeFixItem7();
const vulsTotalByTimeFixItem8Data = await vulsTotalByTimeFixItem8();


const VulFixCharts: React.FC = () => {

  const amountData1 = vulsTotalByTimeFixItem1Data?.data?.data1;
  const rateData1 = vulsTotalByTimeFixItem1Data?.data?.data2;
  const config1 = {
    data: [amountData1, rateData1],
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

  const amountData2 = vulsTotalByTimeFixItem2Data?.data?.data1;
  const rateData2 = vulsTotalByTimeFixItem2Data?.data?.data2;
  const config2 = {
    data: [amountData2, rateData2],
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

  const amountData3 = vulsTotalByTimeFixItem3Data?.data?.data1;
  const rateData3 = vulsTotalByTimeFixItem3Data?.data?.data2;
  const config3 = {
    data: [amountData3, rateData3],
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

  const amountData4 = vulsTotalByTimeFixItem4Data?.data?.data1;
  const rateData4 = vulsTotalByTimeFixItem4Data?.data?.data2;
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

  const amountData5 = vulsTotalByTimeFixItem5Data?.data?.data1;
  const rateData5 = vulsTotalByTimeFixItem5Data?.data?.data2;
  const config5 = {
    data: [amountData5, rateData5],
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

  const amountData6 = vulsTotalByTimeFixItem6Data?.data?.data1;
  const rateData6 = vulsTotalByTimeFixItem6Data?.data?.data2;
  const config6 = {
    data: [amountData6, rateData6],
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

  const amountData7 = vulsTotalByTimeFixItem7Data?.data?.data1;
  const rateData7 = vulsTotalByTimeFixItem7Data?.data?.data2;
  const config7 = {
    data: [amountData7, rateData7],
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

  const amountData8 = vulsTotalByTimeFixItem8Data?.data?.data1;
  const rateData8 = vulsTotalByTimeFixItem8Data?.data?.data2;
  const config8 = {
    data: [amountData8, rateData8],
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
      key: 'item1',
      tab: '有课',
    },
    {
      key: 'item2',
      tab: '官网',
    },
    {
      key: 'item3',
      tab: '企播',
    },
    {
      key: 'item4',
      tab: '直播',
    },
    {
      key: 'item5',
      tab: '目睹云',
    },
    {
      key: 'item6',
      tab: 'MDN',
    },
    {
      key: 'item7',
      tab: 'MDC',
    },
    {
      key: 'item8',
      tab: '互联网',
    },
  ];
  const contentListNoTitle = {
    item1: <DualAxes {...config1} />,
    item2: <DualAxes {...config2} />,
    item3: <DualAxes {...config3} />,
    item4: <DualAxes {...config4} />,
    item5: <DualAxes {...config5} />,
    item6: <DualAxes {...config6} />,
    item7: <DualAxes {...config7} />,
    item8: <DualAxes {...config8} />,
  };

  const [activeTabKey2, setActiveTabKey2] = useState('item1');

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
