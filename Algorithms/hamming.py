def hammingWeight(n):
    def toBinary(n):
        binaryStr = ""
        while n > 0:
            binaryStr += str(n % 2)
            n = n // 2
        return binaryStr

    number = toBinary(n)
    count = 0
    for n in number:
        if n == "1":
            count += 1

    return count


print(hammingWeight(15))
