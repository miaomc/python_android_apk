1. Build Environment:
(0)windows 7
(1)install virtualbox
(2)install CentOS7------install full version or development version which has "ifconfig","route" and GUI
(3)make NAT and HOST-ONLY network(我也没搞清楚，怎么就能ping通外网了)
(3)install python-pip: CentOS7 has python V2.7.5 without pip
    (a)if yum.pip has been ocuppied, "rm -rf /var/run/yum.p"
　　(b)yum -y install epel-release
       yum -y install python-pip

2. Install P4A:https://pypi.org/project/python-for-android/0.5.3/
(1)pip install python-for-android
   python-for-android recipes （测试是否成功）
(2)遇到centos没有dpkg命令（算了还是写中文好了）
   yum update  （升级了58MB）
(3)根据官方说明，不一定要用他说的命令，只要这些包都有就可以，然后有查了一下，一个叫“buildozer”的工具，也是kivy这个工作组弄的，现在还不知道“buildozer”和“python for android”的区别

3. 安装JDK和NDK
使用virtualbox的 本地共享，高级功能包，直接在virtualbox界面就能自动挂载

4. 这个遇到个问题：期初的linux只做了10个G，安装*DK不够，通过使用virutalbox动态硬盘扩容，外加lvm命令，搞定。
推荐链接：https://blog.csdn.net/xialingming/article/details/81291682
这篇文章写的不错，并且主要是归功于linux的lvm做的比较好：
磁盘扩容之后，把扩容的部分建一个区，格式化，然后加到之前那个系统目录下就好了；
是同一个电脑，中间linux需要重启一次，linux在重启的时候，会去做这个扩容的初步操作；
然后把系统目录的mapper刷新一下，就扩容好了。

5. 继续解压JDK和NDK,按照官网android-for-python解压，设置环境变量

6. 测试
p4a apk --private $HOME/code/myapp --package=org.example.myapp --name "My application" --version 0.1 --bootstrap=sdl2 --requirements=python2,kivy
出现bug（Could not find `android` or `sdkmanager` binaries in Android SDK. Exiting.），估计是JDK的环境没有搭好。
..to be continue

7. 采用Kivy的Ubantu镜像

8. *.kv文件调用不成功----就是跟类名一致，可以不考虑尾缀的‘App’
How to load KV：
（1） Kivy looks for a Kv file with the same name as your App class in lowercase, minus “App” if it ends with ‘App’
（2） or Builder.load_file('path/to/file.kv')
（3） or Builder.load_string(kv_string)

9. *。kv文件几个关键字
你可以以如下方式声明你的根控件类：
Widget:
使用如下方式声明其他控件：
<MyWidget>:
KV语言有三个特殊的关键字：
    app: 总是与你的应用关联
    root: 与当前控件的根控件关联
    self: 与控件关联


P.S.
1. kivy打包有两种工具，分别是p4a和buildozer，kivydev64使用p4a，kivydev使用buildozer。buildozer其实是对p4a做了进一步封装，换汤不换药。
2. Buildozer currently works only in Linux
3. https://kivy.org/doc/stable/guide/packaging-android.html
4. VirtualBox-共享文件夹-固定分配myxx sudo mount -t vboxsf myxx /mnt/share
5. unzip xxxx.zip
6. pip install kivy https://mirrors.aliyun.com/pypi/simple/
7. java -version