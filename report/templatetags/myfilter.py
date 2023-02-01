from django import template
register = template.Library()

# 根据字典的键获取对应的值
@register.filter
def get_item(dictionary, key):
    """
    根据字典的键获取对应的值
    :param dictionary: 字典对象
    :param key: 键
    :return:
    """
    return dictionary.get(key)


@register.filter
def cut222(value, arg):
    """将value中的所有arg部分切除掉"""
    return value*arg

@register.filter
def get_index(lis,index):
    return lis[index-1]

