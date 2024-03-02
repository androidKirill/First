# В классе учатся n учеников. Известен рост каждого из них в сантиметрах.
# Рост мальчиков по условию задан отрицательными числами.
# Определите средний рост мальчиков и средний рост девочек.

def main():
    n = int(input())
    m_sum = 0
    m_count = 0
    w_sum = 0
    w_count = 0

    for _ in range(n):
        value = int(input())

        if value > 0:
            w_sum += value
            w_count += 1
        elif value < 0:
            m_sum -= value
            m_count += 1

    print(m_sum // m_count, w_sum // w_count)


if __name__ == "__main__":
    main()
