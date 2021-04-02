一. 使用allure运行测试用例
    1. 在项目根目录执行命令
    pytest ./testcases/test_user_register.py --alluredir ./reports
    2. allure serve ./reports

二. 本地打开jpress项目
    1. 安装tomcat
    2. 下载jpress
    3. 安装mysql
    4. jpress 解压缩至apache-tomcat-xxxx webapp目录下，并将其重命名为jpress
    5. 切换至apache-tomcat-xxxx目录，启动bin目录下startup.sh文件(macOS, sh ./bin/startup.sh)
    6. 打开localhost:8080/jpress, 第一次登录需配置数据库
