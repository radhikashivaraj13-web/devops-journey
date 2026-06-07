import subprocess 
result=subprocess.run("ping 8.8.8.8 -n 2",shell=True,capture_output =True,text=True)
print(result.stdout)
if result.returncode==0:
    print("Internet is working")
else:
    print("Internet is not working")  