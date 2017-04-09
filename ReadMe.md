### Python Kivy 生成APP
```Shell
cd /opt
git clone https://github.com/kivy/buildozer.git 
cd buildozer/
python setup.py install
#cd main.py 所有目录
buildozer init
gedit buildozer.spec
buildozer -v android debug deploy run logcat
```
