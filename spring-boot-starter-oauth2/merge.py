import os
import shutil

path_list = ['spring-boot-starter-alipay-miniprogram',
             'spring-boot-starter-alipay-oplatform',
             'spring-boot-starter-dingtalk',
             'spring-boot-starter-gitee',
             'spring-boot-starter-github',
             'spring-boot-starter-gitlab',
             'spring-boot-starter-qq-connect',
             'spring-boot-starter-qq-miniprogram',
             'spring-boot-starter-wechat-miniprogram',
             'spring-boot-starter-wechat-offiaccount',
             'spring-boot-starter-wechat-oplatform',
             'spring-boot-starter-wechat-work',
             'spring-boot-starter-weibo']

cwd = os.getcwd()

target_abspath = os.path.abspath(os.path.join(os.getcwd(), "../spring-boot-starter-oauth2/src/main/java"))

for path in path_list:
    join = os.path.join(os.getcwd(), "../" + path + "/src/main/java")
    source_abspath = os.path.abspath(join)
    source_abspath_walk = os.walk(source_abspath)
    for root, dirs, files in source_abspath_walk:
        for name in files:
            source = os.path.join(root, name)
            target = source.replace(source_abspath, target_abspath)
            target_dirname = os.path.dirname(target)

            if not os.path.exists(target_dirname):
                os.makedirs(target_dirname)

            shutil.copy(source, target)
