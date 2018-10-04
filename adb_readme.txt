使用adb读取 /data/data/com.myapp.web/..下的文件：

1、adb的下载
http://adbshell.com/downloads
只要下个小插件：ADB Kits (525 KB)(adb.exe AdbWinApi.dll AdbWinUsbApi.dll)

2、 两个链接对adb的介绍和使用
https://jingyan.baidu.com/article/ce4366494962083773afd3d0.html
https://blog.csdn.net/te28093163/article/details/78684712

操作如下：
adb devices
adb shell
run-as 应用包名
cd /data/data/应用包名

Android 设备的开发者选项和 USB 调试模式已开启。

	可以到「设置」-「开发者选项」-「Android 调试」查看。开发者选项，点允许usb调试，然后就可以连上电脑了

	如果在设置里找不到开发者选项，那需要通过一个彩蛋来让它显示出来：在「设置」-「关于手机」连续点击「版本号」7 次。

adb pull /sdcard/Download/company.db