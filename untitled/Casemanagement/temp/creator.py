from abc import ABC, abstractmethod


# 下面的类为工厂类接口及其子类
class Creator(ABC):
    @abstractmethod
    def factory_a(self):
        pass

    @abstractmethod
    def factory_b(self):
        pass

    @staticmethod
    def get_creator(option):
        if option == '1':
            return ConcreteCreatorA()
        elif option == '2':
            return ConcreteCreatorB()


class ConcreteCreatorA(Creator):
    def factory_a(self):
        return ProductA1()

    def factory_b(self):
        return ProductB1()


class ConcreteCreatorB(Creator):
    def factory_a(self):
        return ProductA2()

    def factory_b(self):
        return ProductB2()


# 以下类为产品类接口及其实现子类代码：
class ProductA(ABC):
    @abstractmethod
    def get_product(self):
        pass


class ProductA1(ProductA):
    def get_product(self):
        return "ProductA1"


class ProductA2(ProductA):
    def get_product(self):
        return "ProductA2"


class ProductB(ABC):
    @abstractmethod
    def get_product(self):
        pass


class ProductB1(ProductB):
    def get_product(self):
        return "ProductB1"


class ProductB2(ProductB):
    def get_product(self):
        return "ProductB2"


class Client:
    @staticmethod
    def main():
        # 获取产品类型和种类
        product_class = input("产品种类：").upper()
        product_type = input("产品类型：")
        # 获取具体工厂子类对象
        creator = Creator.get_creator(product_type)
        # 获取具体的产品对象
        if product_class == "A":
            product = creator.factory_a()
            print(product.get_product())
        elif product_class == "B":
            product = creator.factory_b()
            print(product.get_product())


if __name__ == "__main__":
    import os
    print(os.path.dirname(__file__))
    print(os.path.join(os.path.dirname(__file__),"store_id"))
    aim_path = os.path.join(os.path.dirname(__file__),"store_id")
    print(os.path.exists(aim_path))
    os.mkdir(aim_path)
    print(os.path.exists(aim_path))
