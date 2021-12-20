import { PlusOutlined } from '@ant-design/icons';
import { Button, message, Input, Drawer } from 'antd';
import React, { useState, useRef } from 'react';
import { useIntl, FormattedMessage } from 'umi';
import { PageContainer, FooterToolbar } from '@ant-design/pro-layout';
import type { ProColumns, ActionType } from '@ant-design/pro-table';
import ProTable from '@ant-design/pro-table';
import { ModalForm, ProFormText, ProFormTextArea } from '@ant-design/pro-form';
import type { ProDescriptionsItemProps } from '@ant-design/pro-descriptions';
import ProDescriptions from '@ant-design/pro-descriptions';
import type { FormValueType } from './components/UpdateForm';
import UpdateForm from './components/UpdateForm';
import { updateRule, removeRule, vulList, addVul } from '@/services/ant-design-pro/api';

/**
 * @en-US Add node
 * @zh-CN 添加节点
 * @param fields
 */
const handleAdd = async (fields: API.VulListItem) => {
  const hide = message.loading('正在添加');
  try {
    await addVul({ ...fields });
    hide();
    message.success('Added successfully');
    return true;
  } catch (error) {
    hide();
    message.error('Adding failed, please try again!');
    return false;
  }
};

/**
 * @en-US Update node
 * @zh-CN 更新节点
 *
 * @param fields
 */
const handleUpdate = async (fields: FormValueType) => {
  const hide = message.loading('Configuring');
  try {
    await updateRule({
      name: fields.name,
      desc: fields.desc,
      key: fields.key,
    });
    hide();

    message.success('Configuration is successful');
    return true;
  } catch (error) {
    hide();
    message.error('Configuration failed, please try again!');
    return false;
  }
};

/**
 *  Delete node
 * @zh-CN 删除节点
 *
 * @param selectedRows
 */
const handleRemove = async (selectedRows: API.RuleListItem[]) => {
  const hide = message.loading('正在删除');
  if (!selectedRows) return true;
  try {
    await removeRule({
      key: selectedRows.map((row) => row.key),
    });
    hide();
    message.success('Deleted successfully and will refresh soon');
    return true;
  } catch (error) {
    hide();
    message.error('Delete failed, please try again');
    return false;
  }
};

const TableList: React.FC = () => {
  /**
   * @en-US Pop-up window of new window
   * @zh-CN 新建窗口的弹窗
   *  */
  const [createModalVisible, handleModalVisible] = useState<boolean>(false);
  /**
   * @en-US The pop-up window of the distribution update window
   * @zh-CN 分布更新窗口的弹窗
   * */
  const [updateModalVisible, handleUpdateModalVisible] = useState<boolean>(false);

  const [showDetail, setShowDetail] = useState<boolean>(false);

  const actionRef = useRef<ActionType>();
  const [currentRow, setCurrentRow] = useState<API.RuleListItem>();
  const [selectedRowsState, setSelectedRows] = useState<API.RuleListItem[]>([]);

  /**
   * @en-US International configuration
   * @zh-CN 国际化配置
   * */
  const intl = useIntl();

  const columns: ProColumns<API.VulListItem>[] = [
    {
      title: (
        <FormattedMessage
          id="pages.searchTable.updateForm.ruleName.vulid"
          defaultMessage="vul id"
        />
      ),
      dataIndex: 'vul_id',
      tip: '漏洞编号',
      render: (dom, entity) => {
        return (
          <a
            onClick={() => {
              setCurrentRow(entity);
              setShowDetail(true);
            }}
          >
            {dom}
          </a>
        );
      },
    },
    {
      title: <FormattedMessage id="pages.searchTable.vul_name" defaultMessage="vul name" />,
      dataIndex: 'vul_name',
      valueType: 'textarea',
    },
    {
      title: <FormattedMessage id="pages.searchTable.vul_jira" defaultMessage="vul jira" />,
      dataIndex: 'vul_jira',
      valueType: 'textarea',
    },
    {
      title: <FormattedMessage id="pages.searchTable.vul_sendto" defaultMessage="vul sendto" />,
      dataIndex: 'vul_sendto',
      valueType: 'textarea',
    },
    {
      title: <FormattedMessage id="pages.searchTable.vul_fixer" defaultMessage="vul fixer" />,
      dataIndex: 'vul_fixer',
      valueType: 'textarea',
    },
    {
      title: <FormattedMessage id="pages.searchTable.vul_sendtime" defaultMessage="vul sendtime" />,
      dataIndex: 'vul_sendtime',
      valueType: 'textarea',
    },
    {
      title: <FormattedMessage id="pages.searchTable.vul_estimatefixedtime" defaultMessage="vul estimatefixedtime" />,
      dataIndex: 'vul_estimatefixedtime',
      valueType: 'textarea',
    },
    {
      title: <FormattedMessage id="pages.searchTable.vul_fixedtime" defaultMessage="vul fixedtime" />,
      dataIndex: 'vul_fixedtime',
      valueType: 'textarea',
    },
    {
      title: <FormattedMessage id="pages.searchTable.vul_isfixed" defaultMessage="vul isfixed" />,
      dataIndex: 'vul_isfixed',
      valueType: 'textarea',
    },
    {
      title: <FormattedMessage id="pages.searchTable.vul_remarks" defaultMessage="vul remarks" />,
      dataIndex: 'vul_remarks',
      valueType: 'textarea',
    },


    {
      title: <FormattedMessage id="pages.searchTable.titleOption" defaultMessage="Operating" />,
      dataIndex: 'option',
      valueType: 'option',
      render: (_, record) => [
        <a
          key="config"
          onClick={() => {
            handleUpdateModalVisible(true);
            setCurrentRow(record);
          }}
        >
          <FormattedMessage id="pages.searchTable.config" defaultMessage="Configuration" />
        </a>,
        <a key="subscribeAlert" href="https://procomponents.ant.design/">
          <FormattedMessage
            id="pages.searchTable.subscribeAlert"
            defaultMessage="Subscribe to alerts"
          />
        </a>,
      ],
    },
  ];

  return (
    <PageContainer>
      <ProTable<API.VulListItem>
        headerTitle={intl.formatMessage({
          id: 'pages.searchTable.vulList',
          defaultMessage: 'vul List',
        })}
        actionRef={actionRef}
        rowKey="key"
        search={{
          labelWidth: 120,
        }}
        toolBarRender={() => [
          <Button
            type="primary"
            key="primary"
            onClick={() => {
              handleModalVisible(true);
            }}
          >
            <PlusOutlined /> <FormattedMessage id="pages.searchTable.new" defaultMessage="New" />
          </Button>,
        ]}
        request={vulList}
        columns={columns}
        rowSelection={{
          onChange: (_, selectedRows) => {
            setSelectedRows(selectedRows);
          },
        }}
      />
      {selectedRowsState?.length > 0 && (
        <FooterToolbar
          extra={
            <div>
              <FormattedMessage id="pages.searchTable.chosen" defaultMessage="Chosen" />{' '}
              <a style={{ fontWeight: 600 }}>{selectedRowsState.length}</a>{' '}
              <FormattedMessage id="pages.searchTable.item" defaultMessage="项" />
              &nbsp;&nbsp;
              <span>
                <FormattedMessage
                  id="pages.searchTable.totalServiceCalls"
                  defaultMessage="Total number of service calls"
                />{' '}
                {selectedRowsState.reduce((pre, item) => pre + item.callNo!, 0)}{' '}
                <FormattedMessage id="pages.searchTable.tenThousand" defaultMessage="万" />
              </span>
            </div>
          }
        >
          <Button
            onClick={async () => {
              await handleRemove(selectedRowsState);
              setSelectedRows([]);
              actionRef.current?.reloadAndRest?.();
            }}
          >
            <FormattedMessage
              id="pages.searchTable.batchDeletion"
              defaultMessage="Batch deletion"
            />
          </Button>
          <Button type="primary">
            <FormattedMessage
              id="pages.searchTable.batchApproval"
              defaultMessage="Batch approval"
            />
          </Button>
        </FooterToolbar>
      )}
      <ModalForm
        title={intl.formatMessage({
          id: 'pages.searchTable.createForm.newVul',
          defaultMessage: 'New vul',
        })}
        width="400px"
        visible={createModalVisible}
        onVisibleChange={handleModalVisible}
        onFinish={async (value) => {
          const success = await handleAdd(value as API.VulListItem);
          if (success) {
            handleModalVisible(false);
            if (actionRef.current) {
              actionRef.current.reload();
            }
          }
        }}
      >
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_id"
                  defaultMessage="漏洞编号必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_id"
          label={intl.formatMessage({
            id: 'pages.searchTable.updateForm.ruleName.vulid',
            defaultMessage: '漏洞编号',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_name"
                  defaultMessage="漏洞名称必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_name"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_name',
            defaultMessage: '漏洞名称',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_jira"
                  defaultMessage="jira工单为必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_jira"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_jira',
            defaultMessage: 'jira工单',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_sendto"
                  defaultMessage="发送对象必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_sendto"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_sendto',
            defaultMessage: '发送对象',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_fixer"
                  defaultMessage="修复人员必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_fixer"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_fixer',
            defaultMessage: '修复人员',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_sendtime"
                  defaultMessage="发送时间必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_sendtime"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_time',
            defaultMessage: '发送时间',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_estimatefixedtime"
                  defaultMessage="预计修复时间必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_estimatefixedtime"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_estimatefixedtime',
            defaultMessage: '预计修复时间',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_fixedtime"
                  defaultMessage="完成修复时间必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_fixedtime"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_fixedtime',
            defaultMessage: '完成修复时间',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_isfixed"
                  defaultMessage="是否修复必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_isfixed"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_isfixed',
            defaultMessage: '是否修复',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_type"
                  defaultMessage="漏洞类别必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_type"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_type',
            defaultMessage: '漏洞类别',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable.vul_remarks"
                  defaultMessage="备注必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_remarks"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_remarks',
            defaultMessage: '备注',
          })}
        />
      </ModalForm>
      <UpdateForm
        onSubmit={async (value) => {
          const success = await handleUpdate(value);
          if (success) {
            handleUpdateModalVisible(false);
            setCurrentRow(undefined);
            if (actionRef.current) {
              actionRef.current.reload();
            }
          }
        }}
        onCancel={() => {
          handleUpdateModalVisible(false);
          if (!showDetail) {
            setCurrentRow(undefined);
          }
        }}
        updateModalVisible={updateModalVisible}
        values={currentRow || {}}
      />

      <Drawer
        width={600}
        visible={showDetail}
        onClose={() => {
          setCurrentRow(undefined);
          setShowDetail(false);
        }}
        closable={false}
      >
        {currentRow?.name && (
          <ProDescriptions<API.RuleListItem>
            column={2}
            title={currentRow?.name}
            request={async () => ({
              data: currentRow || {},
            })}
            params={{
              id: currentRow?.name,
            }}
            columns={columns as ProDescriptionsItemProps<API.RuleListItem>[]}
          />
        )}
      </Drawer>
    </PageContainer>
  );
};

export default TableList;
