1. Build Environment:
(0)windows 7
(1)install virtualbox
(2)install CentOS7------install full version or development version which has "ifconfig","route" and GUI
(3)make NAT and HOST-ONLY network(��Ҳû���������ô����pingͨ������)
(3)install python-pip: CentOS7 has python V2.7.5 without pip
    (a)if yum.pip has been ocuppied, "rm -rf /var/run/yum.p"
����(b)yum -y install epel-release
       yum -y install python-pip

2. Install P4A:https://pypi.org/project/python-for-android/0.5.3/
(1)pip install python-for-android
   python-for-android recipes �������Ƿ�ɹ���
(2)����centosû��dpkg������˻���д���ĺ��ˣ�
   yum update  ��������58MB��
(3)���ݹٷ�˵������һ��Ҫ����˵�����ֻҪ��Щ�����оͿ��ԣ�Ȼ���в���һ�£�һ���С�buildozer���Ĺ��ߣ�Ҳ��kivy���������Ū�ģ����ڻ���֪����buildozer���͡�python for android��������

3. ��װJDK��NDK
ʹ��virtualbox�� ���ع����߼����ܰ���ֱ����virtualbox��������Զ�����

4. ������������⣺�ڳ���linuxֻ����10��G����װ*DK������ͨ��ʹ��virutalbox��̬Ӳ�����ݣ����lvm����㶨��
�Ƽ����ӣ�https://blog.csdn.net/xialingming/article/details/81291682
��ƪ����д�Ĳ���������Ҫ�ǹ鹦��linux��lvm���ıȽϺã�
��������֮�󣬰����ݵĲ��ֽ�һ��������ʽ����Ȼ��ӵ�֮ǰ�Ǹ�ϵͳĿ¼�¾ͺ��ˣ�
��ͬһ�����ԣ��м�linux��Ҫ����һ�Σ�linux��������ʱ�򣬻�ȥ��������ݵĳ���������
Ȼ���ϵͳĿ¼��mapperˢ��һ�£������ݺ��ˡ�

5. ������ѹJDK��NDK

P.S.
1. kivy��������ֹ��ߣ��ֱ���p4a��buildozer��kivydev64ʹ��p4a��kivydevʹ��buildozer��buildozer��ʵ�Ƕ�p4a���˽�һ����װ����������ҩ��
2. Buildozer currently works only in Linux
3. https://kivy.org/doc/stable/guide/packaging-android.html