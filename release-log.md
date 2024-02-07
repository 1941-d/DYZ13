# v2.0.7 发布日志（开发中）

release:
- [ ] 1. 简单情绪系统
- [ ] 2. VRM支持PMX动画
- [ ] 3. 反思模块开发
- [X] 4. 角色安装包模块开发，支持加载角色安装包，让角色扮演更加符合人设，相对微调此方式更加有性价比

fixbug:
- [ ] 1. 源码部署，修改代码时，会导致重复接收和发送消息
- [ ] 2. docker无法正常连接text-generation-webui
- [X] 3. 适配最新版本的OpenAI SDK
- [X] 4. 修复Bert_vits2语音合成错误问题
- [x] 5. 优化人物模型朝向

TODO
1. text_generation_webui 适配zep的记忆存储

# v2.0.6 发布日志

release:
- [x] 1. 人物动作切换不自然
- [x] 2. 项目日志打印优化
- [x] 3. 优化项目开发文档（conda部署教程）
- [x] 4. 对话段落之间停顿时间过长（优化分段规则）

fixbug:
- [x] 1. 修复text_generation_webui聊天过程中出现，不能正常回复（改为chat模式）
- [x] 2. 修复默认语音参数错误问题
- [x] 3. 修复开启长期记忆程序报错

# v2.0.5 发布日志

release:
- [x] 1. 支持AI根据情绪调整人物动作
- [x] 2. 支持Edge（微软）、Bert-VITS2语音切换
- [x] 3. 支持保存用户上传的VRM模型
- [x] 4. 支持更换壁纸 
- [x] 5. 支持对话弹幕

fixbug:
- [x] 1. 修复对话记录不显示AI回复内容
- [x] 2. chatbot镜像文件过大（5.09G），压缩到2.7G

known issues:
- [ ] 1. 人物动作切换不自然
- [ ] 2. 对话段落之间停顿时间过长（代码逻辑需要优化）
- [ ] 3. 简单情绪系统
- [ ] 4. 项目日志打印优化
- [ ] 5. 源码部署，修改代码时，会导致重复接收和发送消息
- [ ] 6. VRM支持PMX动画

To be determined：
- [ ] 1. 支持AI根据情绪调整语音的音调（koeiromap可以控制情绪，但是只支持日语，emotion-vits可以支持，还在研究）- 原开发计划

# v2.0.4 发布日志

release:
1. 支持中文语音识别

fixbug：
1. 修复B弹幕获取不了的问题
2. 修复Docker中无法使用http-proxy
3. Docker部署ARM系统兼容问题
4. Windows 安装 WSL 的FAQ说明

known issues:
1. chatbot镜像文件过大（5.09G）,待解决

# v2.0.3 发布日志

release:
1. VRM模型支持表情情感表达

fixbug:
1. 修复开启摘要，导致长期记忆存储报错问题
2. 修复text_generation的历史聊天记录不识别问题
3. 修复表情符号和特殊符号导致语音合成失败问题

known issues:
1. 语音识别，待解决

# v2.0.2 发布日志

release:
1. python升级至3.10.12
2. 优化prompt让对话更加拟人
3. text_generation 支持上下文，适配短期记忆
4. text_generation 支持流式返回数据，提高性能

fixbug:
1. 修复音频文件堆积
2. 修复多人同时讨论，长期记忆检索问题
3. 增加解决docker网络问题文档
4. 修复直播获取弹幕，用户名带*号问题

remove：
1. 移除英文角色提示模版

known issues:
1. 语音识别，待解决

注意事项：
- 本次改动更改了数据库表设计，更新代码后请执行数据库迁移操作
```shell
python manage.py makemigrations 
```
```shell
python manage.py migrate 
```
- 本次改动新增了依赖，请执行更新依赖操作
```shell
pip3 install -r requirements.txt
```