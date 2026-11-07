import heapq
import math
from itertools import count


def binary_to_decimal(bits):
    result = 0
    for bit in bits:
        result = result * 2 + int(bit)
    return result


def min_bits(alphabet_size):
    return math.ceil(math.log2(alphabet_size))


def decode_prefix(message, code_table):
    reverse = {v: k for k, v in code_table.items()}
    result = []
    buffer = ""
    for bit in message:
        buffer += bit
        if buffer in reverse:
            result.append(reverse[buffer])
            buffer = ""
    return "".join(result), buffer


def huffman_lengths(freqs):
    counter = count()
    heap = [(p, next(counter), {s: 0}) for s, p in freqs.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        p1, _, d1 = heapq.heappop(heap)
        p2, _, d2 = heapq.heappop(heap)
        merged = {s: l + 1 for s, l in {**d1, **d2}.items()}
        heapq.heappush(heap, (p1 + p2, next(counter), merged))
    return heap[0][2]


def huffman_codes(freqs):
    counter = count()
    heap = [(p, next(counter), {s: ""}) for s, p in freqs.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        p1, _, d1 = heapq.heappop(heap)
        p2, _, d2 = heapq.heappop(heap)
        merged = {s: "0" + c for s, c in d1.items()}
        merged.update({s: "1" + c for s, c in d2.items()})
        heapq.heappush(heap, (p1 + p2, next(counter), merged))
    return heap[0][2]


def average_length(freqs, code_table):
    return sum(freqs[s] * len(code_table[s]) for s in freqs)


def kraft_sum(lengths):
    return sum(2 ** (-l) for l in lengths)


def seminar8_task3():
    print("Семинар 8, самостоятельная работа, задание 3")
    number = "100110"
    print(f"Двоичное число {number} -> десятичное: {binary_to_decimal(number)}")
    print(f"Проверка через int(): {int(number, 2)}")
    print()


def seminar9_student3():
    print("Семинар 9, 3 студент")

    print("\nЗадание 1")
    alphabet_size = 79
    bits = min_bits(alphabet_size)
    print(f"Алфавит: {alphabet_size} символов")
    print(f"Минимум бит на символ: ceil(log2({alphabet_size})) = {bits}")

    print("\nЗадание 2")
    code_table = {"A": "0", "B": "10", "C": "110", "D": "111"}
    message = "10110111010"
    decoded, rest = decode_prefix(message, code_table)
    print(f"Сообщение: {message}")
    print(f"Расшифровка: {decoded}")
    print(f"Остаток: '{rest}'")

    print("\nЗадание 3")
    length = 4000
    freqs = {"A": 0.25, "B": 0.20, "C": 0.15, "D": 0.15, "E": 0.10, "F": 0.10, "G": 0.05}
    uniform_bits = min_bits(len(freqs))
    codes = huffman_codes(freqs)
    avg = average_length(freqs, codes)
    print(f"Длина сообщения: {length}")
    print(f"Равномерный код: {uniform_bits} бит * {length} = {uniform_bits * length} бит")
    print("Код Хаффмана:")
    for symbol in freqs:
        print(f"  {symbol}: {codes[symbol]}")
    print(f"Средняя длина: {avg:.2f} бит/символ")
    print(f"Всего бит: {round(avg * length)}")

    print("\nЗадание 4")
    freqs4 = {"A": 0.45, "B": 0.20, "C": 0.20, "D": 0.10, "E": 0.05}
    code_a = {"A": "0", "B": "10", "C": "110", "D": "1110", "E": "1111"}
    code_b = {"A": "00", "B": "01", "C": "10", "D": "110", "E": "111"}
    avg_a = average_length(freqs4, code_a)
    avg_b = average_length(freqs4, code_b)
    print(f"Код A: средняя длина = {avg_a:.2f}")
    print(f"Код B: средняя длина = {avg_b:.2f}")
    better = "Код A" if avg_a < avg_b else "Код B"
    print(f"Более эффективный: {better}")

    print("\nЗадание 6")
    lengths = [2, 3, 3, 4, 5, 6, 7, 8]
    total = kraft_sum(lengths)
    print(f"Длины кодовых слов: {lengths}")
    print(f"Сумма Крафта: {total:.6f}")
    if total <= 1:
        print(f"Неравенство Крафта выполняется, префиксный код существует")
        print(f"Максимальное количество символов: {len(lengths)}")
    else:
        print("Неравенство Крафта не выполняется")


def main():
    seminar8_task3()
    seminar9_student3()


if __name__ == "__main__":
    main()
