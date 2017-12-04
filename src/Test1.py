from konlpy.tag import *
# from konlpy.tag import Twitter


text = '안녕하세요 오늘은 월요일입니다 무엇을 하고 계세요 저는 잡니다 저두요'
# text = '안녕하세요. 오늘은 월요일입니다. 무엇을 하고 계세요? 저는 잡니다! 저두요.'

# analy = Kkma()
# analy = Twitter()

names = ['꼬고마', '트위터', '한나눔']
# names = ['꼬고마', '트위터', '한나눔', '코모란', '메캡']

analys = []
analys.append(Kkma())
analys = analys + [Twitter(), Hannanum()]
# analys = analys + [Twitter(), Hannanum(), Komoran(), Mecab()]

# sentences = analy.sentences(text)
#
# print('sentences', type(sentences))
# print(sentences)

# for i in range(len(analys)):
#     print(names[i], '결과:')
#     analy = analys[i]
#     nouns = analy.nouns(text)
#     print('nouns', type(nouns))
#     print(nouns)

# 형태소 단위로 추출한 결과
# for i in range(len(analys)):
#     print(names[i], '결과:')
#     analy = analys[i]
#     morphs = analy.morphs(text)
#     print('morphs', type(morphs))
#     print(morphs)

# 형태소 태깅하여 출력한 결과
for i in range(len(analys)):
    print(names[i], '결과:')
    analy = analys[i]
    pos = analy.pos(text)
    print('pos', type(pos))
    print(pos)