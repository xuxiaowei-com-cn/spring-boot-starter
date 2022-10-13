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
        <img alt="企业微信群" src="static/企业微信群.jpg" height="100"/>
    </a>
</div>

1. [支持 OAuth 2.1 JWT 授权的钉钉dingtalk开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-dingtalk)
2. [支持 OAuth 2.1 JWT 授权的码云gitee开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-gitee)
3. [支持 OAuth 2.1 JWT 授权的github开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-github)
4. [支持 OAuth 2.1 JWT 授权的gitlab开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-gitlab)
5. [支持 OAuth 2.1 JWT 授权的QQ开放平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-qq-connect)
6. [支持 OAuth 2.1 JWT 授权的QQ小程序平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-qq-miniprogram)
7. [支持 OAuth 2.1 JWT 授权的微信小程序开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-miniprogram)
8. [支持 OAuth 2.1 JWT 授权的微信公众平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-offiaccount)
9. [支持 OAuth 2.1 JWT 授权的微信开放平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-oplatform)
10. [支持 OAuth 2.1 JWT 授权的企业微信平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-work)
11. [支持 OAuth 2.1 JWT 授权的微博weibo平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-weibo)
12. [一个基于 Spring Boot Redis 的幂等组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-idempotent)

## 分支

- main
    - 支持 JDK 8、11
- next
    - 支持 JDK 17

## 子模块 submodule

```shell
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-dingtalk.git spring-boot-starter-dingtalk
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-gitee.git spring-boot-starter-gitee
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-github.git spring-boot-starter-github
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-gitlab.git spring-boot-starter-gitlab
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-qq-connect.git spring-boot-starter-qq-connect
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-qq-miniprogram.git spring-boot-starter-qq-miniprogram
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-miniprogram.git spring-boot-starter-wechat-miniprogram
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-offiaccount.git spring-boot-starter-wechat-offiaccount
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-oplatform.git spring-boot-starter-wechat-oplatform
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-work.git spring-boot-starter-wechat-work
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-weibo.git spring-boot-starter-weibo
git submodule add -b next https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-idempotent.git spring-boot-starter-idempotent
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

## 批量推送到远端仓库

<details>
<summary>点击展开</summary>
cd spring-boot-starter-dingtalk

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-gitee

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-github

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-gitlab

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-idempotent

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-qq-connect

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-qq-miniprogram

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-wechat-miniprogram

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-wechat-offiaccount

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-wechat-oplatform

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-wechat-work

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

cd spring-boot-starter-weibo

git.exe fetch -v --progress "gitee"

git.exe push --all --progress "gitee"

git.exe push --all --progress "gitlab"

git.exe push --all --progress "jihulab"

git.exe push --all --progress "github"

git.exe push --all --progress "gitcode"

git.exe push --all --progress "gitlink"

cd ..

git.exe fetch -v --progress "origin"

git.exe push --all --progress "origin"

</details>
