import { PlusOutlined } from '@ant-design/icons';
import { Button, message , Drawer } from 'antd';
import React, { useState, useRef } from 'react';
import { useIntl, FormattedMessage } from 'umi';
import { PageContainer, FooterToolbar } from '@ant-design/pro-layout';
import type { ProColumns, ActionType } from '@ant-design/pro-table';
import ProTable from '@ant-design/pro-table';
import {ModalForm, ProFormSelect, ProFormText,} from '@ant-design/pro-form';
import type { ProDescriptionsItemProps } from '@ant-design/pro-descriptions';
import ProDescriptions from '@ant-design/pro-descriptions';
import type { FormValueType } from './components/UpdateForm';
import UpdateForm from './components/UpdateForm';
import { updateVul, removeVul, vulList, addVul } from '@/services/ant-design-pro/myunApi';

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
    message.success('添加成功');
    return true;
  } catch (error) {
    hide();
    message.error('添加失败, 请重新尝试');
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
  console.log(fields);
  const hide = message.loading('Configuring');
  try {
    await updateVul(fields);
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
const handleRemove = async (selectedRows: API.VulListItem[]) => {
  const hide = message.loading('正在删除');
  if (!selectedRows) return true;
  try {
    await removeVul({
      key: selectedRows.map((row) => row.vul_id),
    });
    hide();
    message.success('删除成功，重新加载中');
    return true;
  } catch (error) {
    hide();
    message.error('删除失败, 请重新尝试');
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
  const [currentRow, setCurrentRow] = useState<API.VulListItem>();
  const [selectedRowsState, setSelectedRows] = useState<API.VulListItem[]>([]);

  /**
   * @en-US International configuration
   * @zh-CN 国际化配置
   * */
  const intl = useIntl();
  const rowList: API.VulListItem[] = [];

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
      renderText: (val: string) => {
        if(val == '1'){
          return (
            intl.formatMessage({
              id: 'pages.searchTable.isFixed',
              defaultMessage: ' 是 ',
            })
          );
        }else{
          return (
            intl.formatMessage({
              id: 'pages.searchTable.unFixed',
              defaultMessage: ' 否 ',
            })
          );
        }
      },
    },
    {
      title: <FormattedMessage id="pages.searchTable.vul_type" defaultMessage="vul type" />,
      dataIndex: 'vul_type',
      valueType: 'textarea',
      renderText: (val: number) => {
        console.log(val);
        switch(val){
          case 1:
            return (
              intl.formatMessage({
                id: 'pages.searchTable.type1',
                defaultMessage: ' 输入输出 ',
              })
            );
            break;
          case 2:
            return (
              intl.formatMessage({
                id: 'pages.searchTable.type2',
                defaultMessage: ' 用户权限 ',
              })
            );
            break;
          case 3:
            return (
              intl.formatMessage({
                id: 'pages.searchTable.type3',
                defaultMessage: ' 第三方组件 ',
              })
            );
            break;
          case 4:
            return (
              intl.formatMessage({
                id: 'pages.searchTable.type4',
                defaultMessage: ' 安全配置 ',
              })
            );
            break;
          case 5:
            return (
              intl.formatMessage({
                id: 'pages.searchTable.type5',
                defaultMessage: ' 文件上传下载 ',
              })
            );
            break;
          case 6:
            return (
              intl.formatMessage({
                id: 'pages.searchTable.type6',
                defaultMessage: ' 命令执行&代码执行 ',
              })
            );
            break;
          case 7:
            return (
              intl.formatMessage({
                id: 'pages.searchTable.type7',
                defaultMessage: ' 业务逻辑 ',
              })
            );
            break;
          case 8:
            return (
              intl.formatMessage({
                id: 'pages.searchTable.type8',
                defaultMessage: ' 弱口令 ',
              })
            );
          default:
            return (
              intl.formatMessage({
                id: 'pages.searchTable.type9',
                defaultMessage: ' 其他 ',
              })
            );
        }
      },
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
          <FormattedMessage id="pages.searchTable.config" defaultMessage="edition" />
        </a>,
        <a
          key="deleteVul"
          onClick={async () => {
            rowList.push(record);
            await handleRemove(rowList);
            setSelectedRows([]);
            actionRef.current?.reloadAndRest?.();
          }}>
          <FormattedMessage
            id="pages.searchTable.deleteVulOption"
            defaultMessage="deleteVulOption"
          />
        </a>,
      ],
    },
  ];

  return (
    <PageContainer>
      <ProTable<API.VulListItem,API.PageParams>
        headerTitle={intl.formatMessage({
          id: 'pages.searchTable.vulList',
          defaultMessage: 'vul List',
        })}
        actionRef={actionRef}
        rowKey="vul_id"
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
        search={false}
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
            </div>
          }
        >
          <Button
            onClick={async () => {
              await handleRemove(selectedRowsState);
              setSelectedRows([]);
              actionRef.current?.reloadAndRest?.();
            }}
            type="primary"
          >
            <FormattedMessage
              id="pages.searchTable.batchDeletion"
              defaultMessage="Batch deletion"
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
                  id="pages.searchTable1.vul_id"
                  defaultMessage="漏洞编号必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_id"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_id',
            defaultMessage: '漏洞编号',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_name"
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
                  id="pages.searchTable1.vul_jira"
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
                  id="pages.searchTable1.vul_sendto"
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
                  id="pages.searchTable1.vul_fixer"
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
                  id="pages.searchTable1.vul_sendtime"
                  defaultMessage="发送时间必填"
                />
              ),
            },
          ]}
          width="md"
          name="vul_sendtime"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_sendtime',
            defaultMessage: '发送时间',
          })}
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_estimatefixedtime"
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
                  id="pages.searchTable1.vul_fixedtime"
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
        <ProFormSelect
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_isfixed"
                  defaultMessage="是否修复必填"
                />
              ),
            },
          ]}
          width="md"
          placeholder="请选择是否修复"
          name="vul_isfixed"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_isfixed',
            defaultMessage: '是否修复',
          })}
          valueEnum={{
            1:'是',
            0:'否',
          }}
        />
        <ProFormSelect
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_type"
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
          valueEnum={{
            1:'输入输出',
            2:'用户权限',
            3:'第三方组件',
            4:'安全配置',
            5:'文件上传下载',
            6:'命令执行&代码执行',
            7:'业务逻辑',
            8:'弱口令',
            9:'其他',
          }}
          placeholder="请选择漏洞类别"
        />
        <ProFormText
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_remarks"
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
        {currentRow?.vul_id && (
          <ProDescriptions<API.VulListItem>
            column={2}
            title={currentRow?.vul_id}
            request={async () => ({
              data: currentRow || {},
            })}
            params={{
              id: currentRow?.vul_id,
            }}
            columns={columns as ProDescriptionsItemProps<API.VulListItem>[]}
          />
        )}
      </Drawer>
    </PageContainer>
  );
};

export default TableList;
