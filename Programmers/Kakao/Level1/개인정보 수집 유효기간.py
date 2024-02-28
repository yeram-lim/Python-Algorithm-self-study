def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    today_year, today_month, today_day = today.split('.')
    today_year = int(today_year)
    today_month = int(today_month)
    today_day = int(today_day)
    for term in terms:
        term_type, period = term.split(' ')
        terms_dict[term_type] = int(period)

    for index, privacy in enumerate(privacies):
        date, privacy_term = privacy.split(' ')
        year, month, day = date.split('.')
        year = int(year)
        month = int(month)
        day = int(day)

        limit_month = month + terms_dict[privacy_term]
        if limit_month > 12:
            extra_month = limit_month // 12 if limit_month % 12 != 0 else limit_month // 12 - 1
            year += extra_month

        if limit_month % 12 != 0:
            month = limit_month % 12
        else:
            month = 12
        if day != 1:
            day -= 1
        else:
            day = 28
            if month != 1:
                month -= 1
            else:
                month = 12
                year -= 1
        if year < today_year or (year == today_year and month < today_month) or (year == today_year and month == today_month and day < today_day):
            answer.append(index + 1)
    return answer

# a = solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
b = solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
print(b)