color A
c:
cd C:\Windows\System32
curl.exe "https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe" -o C:\Users\%username%\Downloads\pythonSetupVA.exe
echo "Python Setup Downloaded !!"
cd C:\Users\%username%\Downloads
pythonSetupVA.exe /passive InstallAllUsers=1 PrependPath=1 Include_test=0
pause