import doctest

class KettlebellPhysics:
    def __init__(self, kettlebell_weight:float, kettlebell_density:float ):
        """
        Создание и подготовка к работе объекта "Физические свойства шара для боулинга"
        :param kettlebell_weight: Масса шара для боулинга
        :param kettlebell_density: Плотность шара для боулинга
        Примеры:
        >>> kettlebell = KettlebellPhysics(10.0, 10.0) # инициализация экземпляра класса
        """
        if not isinstance(kettlebell_weight, (int, float)):
            raise TypeError("Масса шара для боулинга должна быть типа int или float")
        if kettlebell_weight < 0:
            raise ValueError("Масса шара для боулинга должна быть положительным числом больше нуля")
        self.kettlebell_weight = kettlebell_weight
        if not isinstance(kettlebell_density, (int, float)):
            raise TypeError("Плотность шара для боулинга должна быть int или float ")
        if kettlebell_density < 0:
            raise ValueError("Плотность шара для боулинга должна быть положительным числом больше нуля")
        self.kettlebell_density = kettlebell_density

    def ability_lift_kettlebell(self) -> bool:
        """
        Функция которая определяет может ли человек поднять шар для боулинга
        :return: Может или не может
        Примеры:
        >>> kettlebell = KettlebellPhysics(10.0, 10.0)
        >>> kettlebell.ability_lift_kettlebell()
        """

    def ability_break_kettlebell (self,kettlebell_force: int) -> bool:
        """
        Функция которая определяет можно ли сломать шар для боулинга
        :param kettlebell_force: Сила удара по шару, Н
        :return: Сломается или нет
        Примеры:
        >>> kettlebell = KettlebellPhysics(10.0, 10.0)
        >>> kettlebell.ability_break_kettlebell(99)
        """
        if not isinstance(kettlebell_force , (int, float)):
            raise TypeError("Сила удара должна быть типа int или float")
        if kettlebell_force < 0:
            raise ValueError("Сила удара должна быть положительным числом")
class KettlebellAppearance:
    def __init__(self, kettlebell_colour: str, kettlebell_shape: str):
        """
        Создание и подготовка к работе объекта "Внешний вид шара для боулинга"
        :param kettlebell_colour: Цвет шара для боулинга
        :param kettlebell_shape: Форма шара для боулинга
        Примеры:
        >>> kettlebell = KettlebellAppearance('зеленый', 'круглый')  # инициализация экземпляра класса
        """
        if not isinstance(kettlebell_colour, str):
            raise TypeError("Цвет шара для боулинга должен быть типа str")
        self.kettlebell_colour = kettlebell_colour
        if not isinstance(kettlebell_shape, str):
            raise TypeError("Форма шара для боулинга должна быть типа str")
    def beauty_kettlebell (self) -> bool:
        """
        Функция которая определяет входит ли этот шар для боулинга в список красивых шаров
        :return: Красивый шар или нет
        Примеры:
        >>> kettlebell = KettlebellAppearance('зеленый', 'круглый')
        >>> kettlebell.beauty_kettlebell()
        """

    def rolling_kettlebell(self) -> float:
        """
        Функция которая считает вероятность того, что шар для боулинга указанной формы покатится
        :return: Вероятность качения
        Примеры:
        >>> kettlebell = KettlebellAppearance('зеленый', 'круглый')
        >>> kettlebell.rolling_kettlebell()
        """

class KettlebellСollection:
    def __init__(self, kettlebell_number:int, kettlebell_price:float ):
        """
        Создание и подготовка к работе объекта "Коллекция шаров для боулинга"
        :param kettlebell_number: Колличество шаров для боулинга в коллекции
        :param kettlebell_price: Стоимость всех шаров
         Примеры:
        >>> kettlebell = KettlebellСollection(999, 189000)  # инициализация экземпляра класса
        """
        if not isinstance(kettlebell_number, int):
            raise TypeError("Число шаров для боулинга в коллекции должно быть типа int")
        if kettlebell_number < 0:
            raise ValueError("Число шаров для боулинга в коллекции должно быть положительным числом")
        self.kettlebell_number = kettlebell_number
        if not isinstance(kettlebell_price, (int, float)):
            raise TypeError("Цена шаров для боулинга в коллекции должна быть типа int или float")
        if kettlebell_price < 0:
            raise ValueError("Цена шаров для боулинга в коллекции должна быть положительным числом")
        self.kettlebell_price = kettlebell_price
    def single_kettlebell (self) -> float:
        """
        Функция которая определяет цену одноого шара для боулинга
        :return: Цена одного шара для боулинга
        Примеры:
        >>> kettlebell  = KettlebellСollection(999, 189000)
        >>> kettlebell.single_kettlebell()
        """
        ...
    def comparison_collections (self,largest_collection:int ) -> bool:
        """
         Функция которая определяет больше ли моя коллекция шаров для боулинга самой большой коллекции шаров
         :param largest_collection: Наибольшая известная коллекция шаров для боулинга, число шаров
         :return: Да или нет
        Примеры:
        >>> kettlebell = KettlebellСollection(999, 189000)
        >>> kettlebell.comparison_collections(10)
        """
        if not isinstance(largest_collection, int):
            raise TypeError("Число шаров для боулинга наибольшей коллекции должно быть типа int")
        if largest_collection < 0:
            raise ValueError("Число шаров для боулинга наибольшей коллекции должено быть положительным числом")

if __name__ == "__main__":
    doctest.testmod()