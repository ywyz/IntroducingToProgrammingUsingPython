'''
@Date: 2019-12-02 19:52:20
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-02 20:28:20
'''


class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def getPreviousClosing(self):
        return self.__previousClosingPrice

    def setPreviousClosing(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getChangePercent(self):
        return (self.__currentPrice - self.__previousClosingPrice
                ) * 100 / self.__previousClosingPrice


def main():
    stock = Stock("INTC", "Intel", 20.5, 20.35)
    print("The price change is ", format(stock.getChangePercent(), "5.2f"),
          "%")


main()
