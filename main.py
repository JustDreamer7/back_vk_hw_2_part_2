import re

"""Домашняя работа №2 - 2-ая часть"""
class CustomMeta(type):
    """Кастомный метакласс, который и заменяет методы в CustomClass"""

    def __call__(self, *args, **kwargs):
        cls_obj = super().__call__(*args, **kwargs)
        attr_to_change = {}
        for item in dir(cls_obj):
            if not re.fullmatch(r'^__\w+__$', item):
                attr_to_change[item] = getattr(cls_obj, item)
        print(attr_to_change)
        for attr, logic_of_attr in attr_to_change.items():
            setattr(cls_obj, "custom_" + attr, logic_of_attr)
            try:
                delattr(self, attr)
            except AttributeError:
                delattr(cls_obj, attr)
        return cls_obj


class CustomClass(metaclass=CustomMeta):
    """Кастомный класс, основанный на метаклассе, в котором все методы
       с префиксом custom_"""
    x = 50

    def __init__(self, val=99):
        self.val = val

    def __add__(self, other):
        return 1

    @staticmethod
    def line():

        """Просто рандомный метод, чтобы его заменить на кастомный"""
        return 100


if __name__ == "__main__":
    inst = CustomClass(val=10)
    inst.custom_x
    inst.custom_val
    inst.custom_line()

    print(dir(inst))

    inst.x  # ошибка
    inst.val  # ошибка
    inst.line()  # ошибка
