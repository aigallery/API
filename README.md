# 计算器 API 文档

该 API 提供了一个简单的计算器功能，包括加法和乘法操作。在使用该 API 之前，需要提供有效的 API 密钥进行身份验证。

## 接口列表

- 加法操作
- 乘法操作

## 加法操作

### 请求

- URL: /add
- 方法: POST
- Headers:
  - API-Key: `<Your API Key>`
  - Content-Type: application/json
- 请求体示例:

```json
{
  "a": 3,
  "b": 5
}
```
### 响应

- 响应示例:
```json
{
  "result": 8
}
```

- 状态码:
  - 200: 成功
  - 400: 参数错误
  - 401: API 密钥无效

## 乘法操作

### 请求

- URL: /multiply
- 方法: POST
- Headers:
  - API-Key: `<Your API Key>`
  - Content-Type: application/json

- 请求体示例:
```json
{
  "a": 3,
  "b": 5
}
```

### 响应

- 响应示例:
```json
{
  "result": 15
}
```

- 状态码:
  - 200: 成功
  - 400: 参数错误
  - 401: API 密钥无效