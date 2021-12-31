import { useIntl } from 'umi';
import { DefaultFooter } from '@ant-design/pro-layout';

const Footer: React.FC = () => {
  const intl = useIntl();
  const defaultMessage = intl.formatMessage({
    id: 'app.copyright.produced',
    defaultMessage: '蚂蚁集团体验技术部出品',
  });

  const currentYear = new Date().getFullYear();

  return (
    <DefaultFooter
      copyright={`${currentYear} ${defaultMessage}`}
      links={[
        {
          key: '直播',
          title: '直播',
          href: 'https://mudu.tv/login',
          blankTarget: true,
        },
        {
          key: '企播',
          title: '企播',
          href: 'http://bugu.mudu.tv/login',
          blankTarget: true,
        },
      ]}
    />
  );
};

export default Footer;
