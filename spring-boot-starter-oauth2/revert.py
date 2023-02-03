import os
import shutil

source_abspath = os.path.abspath(os.path.join(os.getcwd(), "../spring-boot-starter-oauth2/src/main/java"))

path_list = [('AlipayMiniProgram', 'spring-boot-starter-alipay-miniprogram'),
             ('AlipayOplatformWebsite', 'spring-boot-starter-alipay-oplatform'),
             ('Dingtalk', 'spring-boot-starter-dingtalk'),
             ('Gitee', 'spring-boot-starter-gitee'),
             ('GitHub', 'spring-boot-starter-github'),
             ('GitLab', 'spring-boot-starter-gitlab'),
             ('QQWebsite', 'spring-boot-starter-qq-connect'),
             ('QQMiniProgram', 'spring-boot-starter-qq-miniprogram'),
             ('WeChatMiniProgram', 'spring-boot-starter-wechat-miniprogram'),
             ('WeChatOffiaccount', 'spring-boot-starter-wechat-offiaccount'),
             ('WeChatOplatformWebsite', 'spring-boot-starter-wechat-oplatform'),
             ('WeChatWorkWebsite', 'spring-boot-starter-wechat-work'),
             ('WeiBoWebsite', 'spring-boot-starter-weibo')]

for path in path_list:
    join = os.path.join(os.getcwd(), "../" + path[1] + "/src/main/java")
    target_abspath = os.path.abspath(join)
    source_abspath_walk = os.walk(source_abspath)
    for root, dirs, files in source_abspath_walk:
        for name in files:
            source = os.path.join(root, name)
            if path[0] in source:
                target = source.replace(source_abspath, target_abspath)
                shutil.move(source, target)
