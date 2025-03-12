from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    rates = [10, 20, 30, 40]
    discounted_prices = []
    #최적의 이모티콘 할인율 구하기 위한 조합
    #len이 2일때 discounted = [[10, 20], [10,30], [10, 40],,, []]
    discounts = list(product(rates, repeat = len(emoticons)))
    #해당 할인율에서의 가격
    for discount_idx, discount in enumerate(discounts):
        new_cost = []
        for d_idx, d in enumerate(discount):
            new_cost.append(emoticons[d_idx]*(100-d)/100)
        discounted_prices.append(new_cost)
        
    #할인된 가격에서의 구매력 검증
    for discount_idx, discount in enumerate(discounts):
        plus_user = 0
        profit = 0
        for user in users:
            emoticon_buy = 0
            for d_idx, d in enumerate(discount):
                if d >= user[0]:
                    emoticon_buy += discounted_prices[discount_idx][d_idx]
            if emoticon_buy >= user[1]:
                plus_user += 1
            else: profit += emoticon_buy
        if answer[0] < plus_user: answer = [plus_user, profit]
        elif answer[0] == plus_user:
            if answer[1] < profit: answer = [plus_user, profit]
                            
    return answer