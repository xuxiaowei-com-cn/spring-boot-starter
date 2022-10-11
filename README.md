# spring-boot-starter

## Spring Boot 开发组件（git 父模块）

1. [支持 OAuth 2.1 JWT 授权的钉钉dingtalk开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-dingtalk)
2. [支持 OAuth 2.1 JWT 授权的码云gitee开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-gitee)
3. [支持 OAuth 2.1 JWT 授权的gitlab开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-gitlab)
4. [支持 OAuth 2.1 JWT 授权的QQ开放平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-qq-connect)
5. [支持 OAuth 2.1 JWT 授权的QQ小程序平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-qq-miniprogram)
6. [支持 OAuth 2.1 JWT 授权的微信小程序开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-miniprogram)
7. [支持 OAuth 2.1 JWT 授权的微信公众平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-offiaccount)
8. [支持 OAuth 2.1 JWT 授权的微信开放平台开发组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-oplatform)
9. [一个基于 Spring Boot Redis 的幂等组件](https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-idempotent)

## 分支

- main
    - 支持 JDK 8、11
- next
    - 支持 JDK 17

## 子模块 submodule

```shell
git submodule add -b main https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-dingtalk.git spring-boot-starter-dingtalk
git submodule add -b main https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-gitee.git spring-boot-starter-gitee
git submodule add -b main https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-gitlab.git spring-boot-starter-gitlab
git submodule add -b main https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-qq-connect.git spring-boot-starter-qq-connect
git submodule add -b main https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-qq-miniprogram.git spring-boot-starter-qq-miniprogram
git submodule add -b main https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-miniprogram.git spring-boot-starter-wechat-miniprogram
git submodule add -b main https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-offiaccount.git spring-boot-starter-wechat-offiaccount
git submodule add -b main https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-wechat-oplatform.git spring-boot-starter-wechat-oplatform
git submodule add -b main https://gitee.com/xuxiaowei-com-cn/spring-boot-starter-idempotent.git spring-boot-starter-idempotent
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

git.exe fetch -v --progress "origin"

git.exe push --all --progress "origin"

</details>
