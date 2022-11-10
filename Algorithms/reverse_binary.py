def reverseBits(n):
    def toBinaryReversed(n):
        binaryStr = ""
        while n > 0:
            binaryStr += str(n % 2)
            n = n // 2
        while len(binaryStr) != 32:
            binaryStr += "0"
        return binaryStr

    def toInt(string):
        number = 0
        for i in range(len(string)):
            if string[len(string) - i - 1] == "1":
                number += 2**i
        return number

    return toInt(toBinaryReversed(n))


print(reverseBits(43261596))
