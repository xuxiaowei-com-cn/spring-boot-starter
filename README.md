<div align="center" style="text-align: center;">
    <h1>spring-boot-starter</h1>
    <h3>Spring Boot 开发组件（git 父模块）</h3>
    <a target="_blank" href="https://github.com/996icu/996.ICU/blob/master/LICENSE">
        <img alt="License-Anti" src="https://img.shields.io/badge/License-Anti 996-blue.svg">
    </a>
    <a target="_blank" href="https://996.icu/#/zh_CN">
        <img alt="Link-996" src="https://img.shields.io/badge/Link-996.icu-red.svg">
    </a>
    <a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=ZieC6s1WB4njfVbrDHYgoNS8YpT26VtF&jump_from=webapi">
        <img alt="QQ群" src="https://img.shields.io/badge/QQ群-696503132-blue.svg"/>
    </a>
</div>

<p></p>

<div align="center" style="text-align: center;">
    <a target="_blank" href="https://work.weixin.qq.com/gm/75cfc47d6a341047e4b6aca7389bdfa8">
        <img alt="企业微信群" src="static/wechat-work.jpg" height="100"/>
    </a>
</div>

1. [支持 OAuth 2.1 JWT 授权的支付宝小程序开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-alipay-miniprogram.git)
2. [支持 OAuth 2.1 JWT 授权的支付宝开放平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-alipay-oplatform.git)
3. [支持 OAuth 2.1 JWT 授权的钉钉dingtalk开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-dingtalk)
4. [支持 OAuth 2.1 JWT 授权的飞书平台网页应用开发组件](https://github.com/xuxiaowei-com-cn/spring-boot-starter-feishu-webpage)
5. [支持 OAuth 2.1 JWT 授权的码云gitee开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-gitee)
6. [支持 OAuth 2.1 JWT 授权的github开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-github)
7. [支持 OAuth 2.1 JWT 授权的gitlab开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-gitlab)
8. [支持 OAuth 2.1 JWT 授权的QQ开放平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-qq-connect)
9. [支持 OAuth 2.1 JWT 授权的QQ小程序平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-qq-miniprogram)
10. [支持 OAuth 2.1 JWT 授权的微信小程序开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-miniprogram)
11. [支持 OAuth 2.1 JWT 授权的微信公众平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-offiaccount)
12. [支持 OAuth 2.1 JWT 授权的微信开放平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-oplatform)
13. [支持 OAuth 2.1 JWT 授权的企业微信平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-work)
14. [支持 OAuth 2.1 JWT 授权的微博weibo平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-weibo)
15. [将以上 OAuth 2.1 组件打包成一个 jar 包](spring-boot-starter-oauth2)
16. [一个基于 Spring Boot Redis 的幂等组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-idempotent)
17. [Redis 序列化/反序列化 组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-redis)

## [OAuth 2.1 组件 使用文档](https://www.yuque.com/xuxiaowei-com-cn/xuxiaowei-cloud/third-party-login)

## 分支

- main
    - 支持 JDK 8、11
- next
    - 支持 JDK 17

## 子模块 submodule

### 为何使用Git子模块？

1. 2021年2月26日 发布第一个 spring-boot-starter-idempotent 版本，使用独立的Git仓库
2. 2022年7月14日 发布第一个 spring-boot-starter-wechat-miniprogram 版本，使用独立的Git仓库
3. 后来创建了几个其他与 spring-boot-starter-wechat-miniprogram 相同的项目类型，用于拓展 OAuth2.1 的授权，并且也使用了独立仓库。
4. 为了统一管理、将所学应用于实践，所以创建了这个Git模块的父项目。

### 为何不将拓展 OAuth2.1 的授权登录合并成一个项目，提取公共部分减少冗余代码？

1. 拓展 OAuth2.1 的授权的项目，起初只是为了拓展 OAuth2.1 的登录而拓展，没想到会做这么多种
2. 考虑到后期可能会将除了登录意外的其他接口一并做了，放在一个项目中过于臃肿
3. 虽然各厂商（微信、QQ、微博、码云、GitLab等）大都使用的都是 OAuth 2.0 的协议，但差别较大，比如：
    1. 返回数据的`Content-Type`应该为`application/json`，而微信使用了`text/html`
    2. 网站类型与小程序类型授权方式与流程天然不同，无法轻易整合
    3. QQ扫码登录返回数据格式虽然可以设置为`JSON`，但是当参数有问题时，返回数据就不是`JSON`了
    4. 微信返回`access_token`时携带用户唯一标识`openid`、`unionid`（绑定了开放平台后返回`unionid`
       ）；QQ使用三个接口完了获取`access_token`、`openid`、`unionid`；码云返回`access_token`
       时无用户唯一标识，需要使用`access_token`来获取用户唯一标识
    5. 微信等应用的客户唯一标识使用的是`appid`，码云等应用使用的是`client_id`
    6. 有些厂商获取`access_token`时需要`redirect_uri`，有些厂商不需要
4. 考虑到使用者可能会使用 [GitLab](https://gitlab.com)、[极狐](https://jihulab.com) 或自建 `GitLab`，针对于 `GitLab`
   授权，需要自定义域名
5. 每种授权使用独立的`jar`包，使用者上手方便，学习成本低，容易排查问题（宁愿开发者自己麻烦，不想提高使用者的成本）
6. 拓展 OAuth2.1 的授权的项目维护虽然复杂了，但是像这种第三方授权流程，一旦做完了，万年不变（除了更新一下 OAuth 2.1 的依赖而已）
7. 考虑新增组件 [spring-boot-starter-oauth2](spring-boot-starter-oauth2)，将 OAuth 2.1 组件打包成一个 jar 包，方便引用

```shell
git submodule add -b main ../spring-boot-starter-alipay-miniprogram.git spring-boot-starter-alipay-miniprogram
git submodule add -b main ../spring-boot-starter-alipay-oplatform.git spring-boot-starter-alipay-oplatform
git submodule add -b main ../spring-boot-starter-dingtalk.git spring-boot-starter-dingtalk
git submodule add -b main ../spring-boot-starter-feishu-webpage.git spring-boot-starter-feishu-webpage
git submodule add -b main ../spring-boot-starter-gitee.git spring-boot-starter-gitee
git submodule add -b main ../spring-boot-starter-github.git spring-boot-starter-github
git submodule add -b main ../spring-boot-starter-gitlab.git spring-boot-starter-gitlab
git submodule add -b main ../spring-boot-starter-qq-connect.git spring-boot-starter-qq-connect
git submodule add -b main ../spring-boot-starter-qq-miniprogram.git spring-boot-starter-qq-miniprogram
git submodule add -b main ../spring-boot-starter-wechat-miniprogram.git spring-boot-starter-wechat-miniprogram
git submodule add -b main ../spring-boot-starter-wechat-offiaccount.git spring-boot-starter-wechat-offiaccount
git submodule add -b main ../spring-boot-starter-wechat-oplatform.git spring-boot-starter-wechat-oplatform
git submodule add -b main ../spring-boot-starter-wechat-work.git spring-boot-starter-wechat-work
git submodule add -b main ../spring-boot-starter-weibo.git spring-boot-starter-weibo
git submodule add -b main ../spring-boot-starter-idempotent.git spring-boot-starter-idempotent
git submodule add -b main ../spring-boot-starter-redis.git spring-boot-starter-redis
```

## 克隆 clone

```shell
git clone https://gitee.com/xuxiaowei-com-cn/spring-boot-starter.git --recursive
```

```shell
git clone https://gitee.com/xuxiaowei-com-cn/spring-boot-starter.git
cd spring-boot-starter
git submodule
git submodule init
git submodule update
```

## 更新 update

```shell
git submodule update
git submodule update --remote
```

## 批量添加远端仓库地址

<details>
<summary>点击展开</summary>
git remote add gitee https://gitee.com/xuxiaowei-com-cn/spring-boot-starter.git

git remote add gitlab https://gitlab.com/xuxiaowei-com-cn/spring-boot-starter.git

git remote add jihulab https://jihulab.com/xuxiaowei-com-cn/spring-boot-starter.git

git remote add github https://github.com/xuxiaowei-com-cn/spring-boot-starter.git

git remote add gitcode https://gitcode.net/xuxiaowei-com-cn/spring-boot-starter.git

git remote add gitlink https://gitlink.org.cn/xuxiaowei-com-cn/spring-boot-starter.git
</details>

## 批量推送到远端仓库

<details>
<summary>点击展开</summary>

git fetch "origin" next:next
git fetch "origin" main:main

cd spring-boot-starter-alipay-miniprogram

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-alipay-oplatform

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-dingtalk

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-feishu-webpage

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-gitee

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-github

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-gitlab

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-qq-connect

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-qq-miniprogram

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-wechat-miniprogram

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-wechat-offiaccount

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-wechat-oplatform

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-wechat-work

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-weibo

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-idempotent

git fetch "gitee" next:next
git fetch "gitee" main:main

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-redis

cd ..

git.exe fetch -v --progress "origin"

git.exe push --all --progress "origin"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

</details>
