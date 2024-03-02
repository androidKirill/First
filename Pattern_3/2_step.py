# В классе учатся n учеников. Известен рост каждого из них в сантиметрах.
# Рост мальчиков по условию задан отрицательными числами.
# Определите средний рост мальчиков и средний рост девочек.

def main():
    heights = []
    men_heights = []
    women_heights = []

    n = int(input())
    for _ in range(n):
        heights.append(int(input()))

    for value in heights:
        if value > 0:
            women_heights.append(value)
        elif value < 0:
            men_heights.append(-value)

    men_avg_height = sum(men_heights) // len(men_heights)
    women_avg_height = sum(women_heights) // len(women_heights)

    print(men_avg_height, women_avg_height)


if __name__ == "__main__":
    main()
