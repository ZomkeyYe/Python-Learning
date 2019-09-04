# 简单的装饰器
from functools import wraps
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("装饰器内部开始")
 
        a_func()
 
        print("装饰器内部结束")
 
    return wrapTheFunction
@a_new_decorator
def a_function_requiring_decoration():
    print("我需要装饰器")
 
a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"
print(a_function_requiring_decoration.__name__)