from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

# 在这里定义您的有效的 API 密钥列表
valid_api_keys = ["123456"]


# 校验 API 密钥的装饰器
def validate_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        API 密钥验证装饰器

        校验传入请求的 API 密钥是否有效。

        Args:
            func (function): 被装饰的函数

        Returns:
            function: 被装饰的函数或错误响应

        """
        api_key = request.headers.get('API-Key')
        if not api_key or api_key not in valid_api_keys:
            return jsonify({'error': 'Invalid API Key'}), 401
        return func(*args, **kwargs)
    return wrapper


# 计算加法
def add_numbers(a, b):
    """
    加法计算

    对传入的两个数字进行加法运算。

    Args:
        a (int): 第一个操作数
        b (int): 第二个操作数

    Returns:
        int: 加法结果

    """
    return a + b


# 计算乘法
def multiply_numbers(a, b):
    """
     乘法计算

    对传入的两个数字进行乘法运算。

    Args:
        a (int): 第一个操作数
        b (int): 第二个操作数

    Returns:
        int: 乘法结果

    """
    return a * b


# 加法路由
@app.route('/add', methods=['POST'])
@validate_api_key
def add():
    """
    加法 API

    提供加法功能的 API。传入的 JSON 数据中应包含 'a' 和 'b' 两个参数。

    Returns:
        json: 包含加法结果的 JSON 响应

    """
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')

    if a is None or b is None:
        return jsonify({'error': 'Invalid parameters'}), 400

    result = add_numbers(a, b)
    return jsonify({'result': result}), 200


# 乘法路由
@app.route('/multiply', methods=['POST'])
@validate_api_key
def multiply():
    """
    乘法 API

    提供乘法功能的 API。传入的 JSON 数据中应包含 'a' 和 'b' 两个参数。

    Returns:
        json: 包含乘法结果的 JSON 响应

    """
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')

    if a is None or b is None:
        return jsonify({'error': 'Invalid parameters'}), 400

    result = multiply_numbers(a, b)
    return jsonify({'result': result}), 200


if __name__ == '__main__':
    app.run()
