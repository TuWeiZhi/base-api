# 使用jenkins接口模块踩坑记录

1. 默认连通性不通，解决方法：
    1. 修改jenkins master的全局安全设置
    勾选匿名用户具有可读权限
    2. 调用服务后先认证信息
    get_whoami()

2. create_job 指定的config_xml必须是 utf-8编码
