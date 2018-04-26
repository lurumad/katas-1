# -*- coding: utf-8 -*-

from expects import *

DECIMAL_TO_ROMAN_NUMBERS = { 1000: "M", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I" }

def convert_to_roman_from_decimal(decimal_number):
    print(decimal_number)
    result = ""
    last_roman_numeral = ""
    for decimal, roman_numeral in sorted(DECIMAL_TO_ROMAN_NUMBERS.items(), reverse=True):
        number_of_similar_symbols = 0
        current_result = ""
        if decimal_number == decimal:
            result += DECIMAL_TO_ROMAN_NUMBERS.get(decimal)
            break
        while decimal_number / decimal >= 1:
            print("{} is bigger than {}".format(decimal_number, decimal))
            current_symbol = DECIMAL_TO_ROMAN_NUMBERS.get(decimal)
            current_result += current_symbol
            decimal_number -= decimal
            number_of_similar_symbols += 1
            if number_of_similar_symbols == 4:
                current_result = current_symbol + last_roman_numeral
                break
            print("current_result: {}".format(current_result))
        # result += current_result
        last_roman_numeral = roman_numeral
    number_of_similar_symbols = 0
    result += current_result
    return result


with describe('Roman Numerals'):
    with context('from decimal number to roman numeral'):
        with it('converts 1 to I'):
            decimal_number = convert_to_roman_from_decimal(1)

            expect(decimal_number).to(equal("I"))

        with it('converts 2 to II'):
            decimal_number = convert_to_roman_from_decimal(2)

            expect(decimal_number).to(equal("II"))

        with it('converts 3 to III'):
            decimal_number = convert_to_roman_from_decimal(3)

            expect(decimal_number).to(equal("III"))

        with it('converts 4 to IV'):
            decimal_number = convert_to_roman_from_decimal(4)

            expect(decimal_number).to(equal("IV"))

        with it('converts 5 to V'):
            decimal_number = convert_to_roman_from_decimal(5)

            expect(decimal_number).to(equal("V"))

        # with it('converts 24 to XXIV'):
        #     decimal_number = convert_to_roman_from_decimal(24)

        #     expect(decimal_number).to(equal("XXIV"))

        with it('converts 50 to L'):
            decimal_number = convert_to_roman_from_decimal(50)

            expect(decimal_number).to(equal("L"))

        with it('converts 100 to C'):
            decimal_number = convert_to_roman_from_decimal(100)

            expect(decimal_number).to(equal("C"))

        with it('converts 1000 to M'):
            decimal_number = convert_to_roman_from_decimal(1000)

            expect(decimal_number).to(equal("M"))

    with context('from roman numeral to decimal number'):
        with _it('TODO'):
            pass