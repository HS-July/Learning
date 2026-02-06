def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("오류: 0으로 나눌 수 없습니다.")
        return None
    return a / b


def power(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        print("오류: 0으로 나눌 수 없습니다.")
        return None
    return a % b


def compound_interest(principal, rate, years):
    return principal * (1 + rate / 100) ** years


def format_number(n):
    if n == int(n):
        return f"{int(n):,}"
    return f"{n:,.10f}".rstrip("0").rstrip(".")


def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("**", power),
        "6": ("%", modulo),
    }

    while True:
        print("\n===== 계산기 =====")
        print("1. 더하기 (+)")
        print("2. 빼기 (-)")
        print("3. 곱하기 (*)")
        print("4. 나누기 (/)")
        print("5. 제곱 (**)")
        print("6. 나머지 (%)")
        print("7. 복리 계산")
        print("0. 종료")

        choice = input("\n연산을 선택하세요: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break

        if choice == "7":
            try:
                principal = float(input("원금: "))
                rate = float(input("연이율 (%): "))
                years = float(input("기간 (년): "))
            except ValueError:
                print("올바른 숫자를 입력하세요.")
                continue
            result = compound_interest(principal, rate, years)
            profit = result - principal
            print(f"\n--- 복리 계산 결과 ---")
            print(f"원금:       {format_number(principal)}원")
            print(f"연이율:     {format_number(rate)}%")
            print(f"기간:       {format_number(years)}년")
            print(f"최종 금액:  {format_number(result)}원")
            print(f"수익:       {format_number(profit)}원")
            continue

        if choice not in operations:
            print("잘못된 입력입니다. 다시 선택하세요.")
            continue

        try:
            a = float(input("첫 번째 숫자: "))
            b = float(input("두 번째 숫자: "))
        except ValueError:
            print("올바른 숫자를 입력하세요.")
            continue

        symbol, func = operations[choice]
        result = func(a, b)
        if result is not None:
            print(f"\n결과: {format_number(a)} {symbol} {format_number(b)} = {format_number(result)}")


if __name__ == "__main__":
    main()
