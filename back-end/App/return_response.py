# 这个不要放在views，最好是放在其他单独的文件里，视图只写视图代码A

def return_response(succ: bool = True, data=None, info: str = '', error: str = '', code: int = 1):
    return {
        'code': code,
        'succ': succ,  # 请求标志  -True/False
        'data': data,  # 请求内容  -dict
        'info': info,  # 提示信息  -str
        'errs': error  # 错误信息  -str
    }