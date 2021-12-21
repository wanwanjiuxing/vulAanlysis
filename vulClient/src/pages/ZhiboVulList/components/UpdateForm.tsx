import React from 'react';
import { Modal } from 'antd';
import {
  ProFormText,
  StepsForm,
} from '@ant-design/pro-form';
import { useIntl, FormattedMessage } from 'umi';

export type FormValueType = {
  target?: string;
  template?: string;
  type?: string;
  time?: string;
  frequency?: string;
} & Partial<API.VulListItem>;

export type UpdateFormProps = {
  onCancel: (flag?: boolean, formVals?: FormValueType) => void;
  onSubmit: (values: FormValueType) => Promise<void>;
  updateModalVisible: boolean;
  values: Partial<API.VulListItem>;
};

const UpdateForm: React.FC<UpdateFormProps> = (props) => {
  const intl = useIntl();
  return (
    <StepsForm
      stepsProps={{
        size: 'small',
      }}
      stepsFormRender={(dom, submitter) => {
        return (
          <Modal
            width={640}
            bodyStyle={{ padding: '32px 40px 48px' }}
            destroyOnClose
            title={intl.formatMessage({
              id: 'pages.searchTable.updateForm.editVul',
              defaultMessage: '编辑漏洞',
            })}
            visible={props.updateModalVisible}
            footer={submitter}
            onCancel={() => {
              props.onCancel();
            }}
          >
            {dom}
          </Modal>
        );
      }}
      onFinish={props.onSubmit}
    >
      <StepsForm.StepForm
        initialValues={{
          vul_id: props.values.vul_id,
          vul_name: props.values.vul_name,
          vul_jira: props.values.vul_jira,
          vul_sendto: props.values.vul_sendto,
        }}
        title={intl.formatMessage({
          id: 'pages.searchTable.updateForm.step1',
          defaultMessage: 'step1',
        })}
      >
        <ProFormText
          name="vul_id"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_id',
            defaultMessage: '漏洞编号',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_id"
                  defaultMessage="漏洞编号为必填项"
                />
              ),
            },
          ]}
        />
        <ProFormText
          name="vul_name"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_name',
            defaultMessage: '漏洞名称',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_name"
                  defaultMessage="漏洞编号为必填项"
                />
              ),
            },
          ]}
        />
        <ProFormText
          name="vul_jira"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_jira',
            defaultMessage: 'jira工单',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_jira"
                  defaultMessage="jira工单号为必填项"
                />
              ),
            },
          ]}
        />
        <ProFormText
          name="vul_sendto"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_sendto',
            defaultMessage: '发送对象',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_sendto"
                  defaultMessage="发送对象为必填项"
                />
              ),
            },
          ]}
        />
      </StepsForm.StepForm>
      <StepsForm.StepForm
        initialValues={{
          vul_fixer: props.values.vul_fixer,
          vul_sendtime: props.values.vul_sendtime,
          vul_estimatefixedtime: props.values.vul_estimatefixedtime,
          vul_fixedtime: props.values.vul_fixedtime,
        }}
        title={intl.formatMessage({
          id: 'pages.searchTable.updateForm.step2',
          defaultMessage: 'step2',
        })}
      >
        <ProFormText
          name="vul_fixer"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_fixer',
            defaultMessage: '修复人员',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_fixer"
                  defaultMessage="修复人员为必填项"
                />
              ),
            },
          ]}
        />
        <ProFormText
          name="vul_sendtime"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_sendtime',
            defaultMessage: '发送时间',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_sendtime"
                  defaultMessage="发送时间为必填项"
                />
              ),
            },
          ]}
        />
        <ProFormText
          name="vul_estimatefixedtime"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_estimatefixedtime',
            defaultMessage: '预计修复时间',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_estimatefixedtime"
                  defaultMessage="预计修复时间为必填项"
                />
              ),
            },
          ]}
        />
        <ProFormText
          name="vul_fixedtime"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_fixedtime',
            defaultMessage: '完成修复时间',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_fixedtime"
                  defaultMessage="完成修复时间为必填项"
                />
              ),
            },
          ]}
        />
      </StepsForm.StepForm>
      <StepsForm.StepForm
        initialValues={{
          vul_isfixed: props.values.vul_isfixed,
          vul_type: props.values.vul_type,
          vul_remarks: props.values.vul_remarks,
        }}
        title={intl.formatMessage({
          id: 'pages.searchTable.updateForm.step3',
          defaultMessage: 'step3',
        })}
      >
        <ProFormText
          name="vul_isfixed"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_isfixed',
            defaultMessage: '是否修复',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_isfixed"
                  defaultMessage="是否修复为必填项"
                />
              ),
            },
          ]}
        />
        <ProFormText
          name="vul_type"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_type',
            defaultMessage: '漏洞类别',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_type"
                  defaultMessage="漏洞类别为必填项"
                />
              ),
            },
          ]}
        />
        <ProFormText
          name="vul_remarks"
          label={intl.formatMessage({
            id: 'pages.searchTable.vul_remarks',
            defaultMessage: '备注',
          })}
          width="md"
          rules={[
            {
              required: true,
              message: (
                <FormattedMessage
                  id="pages.searchTable1.vul_remarks"
                  defaultMessage="备注为必填项"
                />
              ),
            },
          ]}
        />

      </StepsForm.StepForm>
    </StepsForm>
  );
};

export default UpdateForm;
