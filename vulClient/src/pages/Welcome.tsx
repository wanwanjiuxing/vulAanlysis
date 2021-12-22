import React from 'react';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, Alert } from 'antd';
import { useIntl, } from 'umi';


// const CodePreview: React.FC = ({ children }) => (
//   <pre className={styles.pre}>
//     <code>
//       <Typography.Text copyable>{children}</Typography.Text>
//     </code>
//   </pre>
// );

const Welcome: React.FC = () => {
  const intl = useIntl();
  return (
    <PageContainer>
      <Card>
        <Alert
          message={intl.formatMessage({
            id: 'pages.welcome.Message',
            defaultMessage: '欢迎使用，更多产品功能开发中。。。',
          })}
          type="success"
          showIcon
          banner
          style={{
            margin: -12,
            marginBottom: 48,
          }}
        />
        {/*<Typography.Text strong>*/}
        {/*  <FormattedMessage id="pages.welcome.advancedComponent" defaultMessage="Advanced Form" />{' '}*/}
        {/*  <a*/}
        {/*    href="https://procomponents.ant.design/components/table"*/}
        {/*    rel="noopener noreferrer"*/}
        {/*    target="__blank"*/}
        {/*  >*/}
        {/*    <FormattedMessage id="pages.welcome.link" defaultMessage="Welcome" />*/}
        {/*  </a>*/}
        {/*</Typography.Text>*/}
        {/*<CodePreview>yarn add @ant-design/pro-table</CodePreview>*/}
        {/*<Typography.Text*/}
        {/*  strong*/}
        {/*  style={{*/}
        {/*    marginBottom: 12,*/}
        {/*  }}*/}
        {/*>*/}
        {/*  <FormattedMessage id="pages.welcome.advancedLayout" defaultMessage="Advanced layout" />{' '}*/}
        {/*  <a*/}
        {/*    href="https://procomponents.ant.design/components/layout"*/}
        {/*    rel="noopener noreferrer"*/}
        {/*    target="__blank"*/}
        {/*  >*/}
        {/*    <FormattedMessage id="pages.welcome.link" defaultMessage="Welcome" />*/}
        {/*  </a>*/}
        {/*</Typography.Text>*/}
        {/*<CodePreview>yarn add @ant-design/pro-layout</CodePreview>*/}
      </Card>
    </PageContainer>
  );
};

export default Welcome;
